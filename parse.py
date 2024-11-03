from bs4 import BeautifulSoup
import re
import csv
import os

FIELDS = ['name', 'year', 'mileage', 'price']

def read_file(filename):
    with open(filename) as input_file:
        text = input_file.read()
    return text

def parse_to_table(filename):
    result = []
    text = read_file(filename)
    
    soup = BeautifulSoup(text, features="html.parser")
    
    
    list_cars = soup.find('div', {'class': 'items-items-pZX46'})
    if not list_cars:
        return result
    
    items = list_cars.find_all('div', {'class': 'iva-item-body-GQomw'})
    for item in items:
        announcement_name = item.find('div', {'class': 'iva-item-title-CdRXl'}).find('a').text.replace('\xa0', '').replace('битый', '')
        prices = item.find('div', {'class': 'price-price-j2OjU'}).find('p').text.replace('\xa0', '')
        match = re.search(r'(.*)\,\s+(.*)\,\s+(.*)', announcement_name)
        
        if match:
            result.append({
                'name': match.group(1),
                'year': match.group(2),
                'mileage': match.group(3),
                'price': prices
            })
    return result

def parser(total_page):
    all_results = []
    page = 1
    
    for _ in range(total_page - 1):
        filename = f"./result/page_{page}.html"
        page_result = parse_to_table(filename)
        all_results.extend(page_result) 
        page += 1

    with open('./result/cars.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        
        for row in all_results:
            try:
                writer.writerow(row)
            except Exception as e:
                print(f"Ошибка при записи строки {row}: {e}")
                
    
    for i in range(1, total_page):
        try:
            os.remove(f"./result/page_{i}.html")
        except OSError:
            print(f"Файл page_{i}.html не найден для удаления")
    
    print("done")
