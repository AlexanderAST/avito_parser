from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

cookies = {
    'cfidsw-avito':'4zV+OO5pasRdmsFqC1KMPP1TEXfQW0PJFmgId/Ax/CHFqRaT3bwLCwurlufbl2mCKK1HO85sSN7g4YD0xOaKHUUc3RPybjPO97anErqOXRJOekOHteDQZ+kn83ckSWpIMgVzIFQOiJ9FE/LQ8FGsKSkCer/W5x6BEHeu; gMltIuegZN2COuSe=EOFGWsm50bhh17prLqaIgdir1V0kgrvN; SEARCH_HISTORY_IDS=0%2C4%2C; v=1730646242; luri=moskva; dfp_group=100; isLegalPerson=0; cartCounter=0; f=5.b5cb31199096e27936b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a7b0d53c7afc06d0b2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b918f89022f7cbdc9f90d83bac5e6e82bd59c9621b2c0fa58f915ac1de0d03411231a1058e37535dce34d62295fceb188df88859c11ff008953de19da9ed218fe23de19da9ed218fe2e992ad2cc54b8aa87fde300814b1e8553de19da9ed218fe23de19da9ed218fe2c772035eab81f5e13de19da9ed218fe2b5b87f59517a23f2cd39050aceac4b901da3a4c5ab599670f9448f5680fb8cc2fc7741ff87bfe2368f5b74f1f9fd0a0d35b0929bad7c1ea51bd4f25f49a2ca313da86e9c7d544fef17c7721dca45217b32409498038d713c95d577eb21b91f1ae2415097439d404746b8ae4e81acb9fa786047a80c779d5146b8ae4e81acb9fabba744e6a9835c6b1cf5fc67cf4c79a92da10fb74cac1eab3fdb0d9d9f6f145bd1ce76042dff8395babde02de62b250aade7e9acbc1a5ac0; ft="TdpHbkXvVmh19I84/Svkt7DvZY4j8Mkb9nFPweMYgzJf/HSJjAbftf8hwn3Q8hLCM5XNYgCu6VkvygQOJGrUzsAMlZUubiRaMirYAv3sYn725iVYJnqwPsUP5niU76uBIYoomMKSLgWh0e/xSx7ay0JOxK3SaWETtmRRQ0zyZHZ4qTrr3zrw7ew5UcQmr/rw";', 
    'sx':'H4sIAAAAAAAC%2F6SVSXIkOw5E75LrWgAEAZL%2FNsTAUA7KQZHzt7p7W6hNKmUvqy%2Fw4ObudP67AvA2cmGFkUbv7I3qyIRSEI2or%2F75d3Vd%2FbM632Izj4vX94eezvs2tg9dH%2Fg0Xc%2Fb25VWv1ax%2BgcLQSGCjL9%2FrSABRa1VUmbLQyPxgFYZUx414TfZ%2BCQq2%2BfjvJUtbZ93n2uPNDOdod%2FyH7Jwa%2BWTLJkz1TGIwANMpOTWu2TxPNDzFxlH6%2BCJAYwSD0Ur4GNQK14DM0MyBDX%2BIR6JGy0nonMAmII2NBHGQQlJstScifTrhJ8Oh7dpbGLS%2B5g3H%2FPxEtU2k9J1LVJ%2BkIFZFvEJ3ChT7wmxNnB3zDnhoC7YrcUX%2BTbd24Y28xg2Ea31VvWY5qvvWr3eTuOFnD5tSTaQsZlX8Abs7E1ERyEDG1jsixyGtZZRoueqrKnlZiApRpPwTFkGIYvjzxMlwWJLCi6dKWqv3polb6URcQEdmal9O%2F%2FE%2Bd66r499c7ucZ397e%2B%2Fw2E7P9e3Nj%2FnVlrqQCST3qqBolpKaUCmjGFZJ1iv8seUJ52PqXLf3u%2B7nw8G2fNve4%2Fgx3Z718ULGuthClTySEfcUxUtvFcU7kiaVPLh8kd9Oj7K%2FrQ9i12tr1%2B7SnvvjR7xfYZrf3l%2FIBAs5A%2BcaI6sTtlCDTlFLx0RiffyJErp5CyUuUaFl1Ea9k1ES5pEaDjU06vazh6kQLCdMWuoSghajpEQcQlzQItLwCn9jS4L0%2B9eKsTQpopgqL%2FFJ680HMQ9TSUZfZMX91J8pUT35fMD9%2Fu2ebrePj8fjvq0VX6NMspAL9%2FBhbO5owgVgSM%2BtZiLsnb%2FI62k%2FLB%2FxvZxn5d5Ox3X1y2map81lmuznw2fOS0m4OaK1SJ4yK7SEiESFOigp9W%2FN%2FHE1353aJdrcYn6Ue0fgD98hmW6vLz4LLW6IiJgXGU0aS5YWRYOaFwaz4u2LPG3PR4Z7atPl2c8beGrvlx3dAPbb3e78P%2BSykNWzZ13GNIUPbomUS1DPnjv%2BGdi%2FeZWc03KiIkoEOY1eAsg8Je0BHWvviP1b%2FMbu10PcLnIiaZfTNXlcYK1B7wct5xfDS6n%2FJUvOKNkdhjW0Rl4ZQKGYuUv8VUloKUmj3AmChrQyhrFKTwKYBoSH5O9if5T3tu%2B7Pr9FuR1vxxlKWX%2FAbFdZ734O7KfmJcqWe6nZvOesSNRCes8iskyYd8H%2Fy3CSpYetRzdx1DGWDH0wiyROJIDN4ft3oB7NTYHVwLlEjJr6oOxDM0aPVAZk5fpaG6i%2Ff616t%2BWLIxttECk1bcmSZYnWnVL9PtFaMskVjNyQnU0riA8Lq4179uTNtdDrtiD%2F%2FrVSrjI4BkqgBHiXqqloQ%2BWsWr6HcaNpczpNvMb3eqiHzC0%2F%2Ba0eIh6yPl1e%2FJG8iHfgSFoaMgZZsQFQmRRAzVFQvsiD4j2m6f25K%2F35INtuDnUTQnaa7A12r%2BGWT7J2LFGNU7esQaQqtSIG10ak32TfpYG3TZs2O4APf5z398NZN5erZdltXzUTlk9yVMmqFKYiQSqFvFVmBUvDvr%2B2st%2Bsr7Z%2FHG67j%2F2bDb5ep13aYLueN%2FeRXjTXz9UauS7Dr1BRTAErVs3Lv4muzLX%2F1YZTW8g9emDRWkpCGTn6IIwaGKLW6%2FceBu%2Be897B7882%2BJjb8Qw%2BT9vZ19vzVl8TFPr9%2Bz8BAAD%2F%2F9U7B%2FEYCgAA; abp=0; buyer_from_page=catalog'
}

def request_data(page:int):
    url = f'https://www.avito.ru/moskva/avtomobili/toyota/camry-ASgBAgICAkTgtg20mSjitg3UoCg?cd=1&f=ASgBAgECAkTgtg20mSjitg3UoCgBRcaaDBd7ImZyb20iOjAsInRvIjoxMDAwMDAwfQ&radius=0&searchRadius=0&p={page}'
    s = requests.Session()
    r = s.get(url, headers=headers, cookies=cookies)
    
    return r.text

def contain_data(text):
    soup = BeautifulSoup(text, features="html.parser")
    list_cars = soup.find('div', {'class':'items-items-pZX46'})
    print(list_cars)
    return list_cars is not None

def take_data():
    page = 1
    
    while page < 30:
        data = request_data(page)
        if contain_data(data):
            with open(f'./result/page_{page}.html', 'w', encoding="utf-8") as output_file:
                output_file.write(data)
                page += 1
        else:
            break
        
    print("done")
    return page
