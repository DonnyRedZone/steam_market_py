import requests
import configparser

def set_cookies(cookie):
    config = configparser.ConfigParser()
    cookie = cookie.replace('%','%%')
    config['Cookie'] = {'Cookie': f'{cookie}'}
    with open(r'cookie.ini', 'w') as configfile:
        config.write(configfile)

def iniate_cookies() :
    global cookiejar
    config = configparser.ConfigParser()
    config.read('cookie.ini')
    cookie = str(config['Cookie']['cookie'])
    cookiejar = {'steamLoginSecure': cookie}

def get_hash_name (appid,query) :
    results = requests.get(f'https://steamcommunity.com/market/search/render/?query={query}&appid={appid}&start=0&count=100&norender=1').json()

    if bool(results['success']) != True :
        print('An error occured while fetching search')

    elif results['searchdata']['total_count'] == 0 :
        print ('Item Not Found')

    else :
        return (results['results'][0]['hash_name'])


def get_current_price(appid, hash_name, mode=1, currency=1):
    global cookiejar
    if mode == 1 :
        data = requests.get(f'https://steamcommunity.com/market/priceoverview/?appid={appid}&currency={currency}&market_hash_name={hash_name}', cookies = cookiejar).json()
        return data['lowest_price']
    elif mode == 2 :
        results = requests.get(f'https://steamcommunity.com/market/search/render/?query={hash_name}&appid={appid}&start=0&count=100&norender=1').json()
        if bool(results['success']) != True:
            print('error while loading data, likely no connection')
        else:
            price = results['results'][0]['sell_price']
            return price/100
    elif mode == 3 :
        data = requests.get(f'https://steamcommunity.com/market/pricehistory/?appid={appid}&currency=0&market_hash_name={hash_name}',cookies=cookiejar).json()
        return data['prices'][-1][-2]
    else :
        raise Exception('Please select 1 or 2 or 3 as your mode')

def get_price_history(appid ,hash_name ) :
    global cookiejar
    data = requests.get(f'https://steamcommunity.com/market/pricehistory/?appid={appid}&currency=0&market_hash_name={hash_name}',cookies=cookiejar).json()

    return {'prices' : data['prices']}

def get_listings(appid , hash_name) :
    results = requests.get(f'https://steamcommunity.com/market/search/render/?query={hash_name}&appid={appid}&start=0&count=100&norender=1').json()
    return results['results'][0]['sell_listings']

def get_median_price(appid , hash_name , currency = 1) :
    global cookiejar
    data = requests.get(f'https://steamcommunity.com/market/priceoverview/?appid={appid}&currency={currency}&market_hash_name={hash_name}', cookies = cookiejar).json()
    return data['median_price']








