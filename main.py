from request import take_data
from parse import parser
def main():
    total_page = take_data()
    parser(total_page)

if __name__ == "__main__":
    main()