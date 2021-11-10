import argparse
import requests
from bs4 import BeautifulSoup
import json

#doctests 

def parse_itemssold(text):
    '''
    Takes as input a string and returns the number of items sold, as specified in the string
    
    >>> parse_itemssold('38 sold')
    38
    >>> parse_itemssold('14 watchers')
    0
    >>> parse_itemssold('Almost gone')
    0
    '''
    numbers = ''
    t = text.lower()
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in t:
        return int(numbers)
    else:
        return int(0)

def parse_price(text):
    '''    
    >>> parse_price('$10.00')
    1000
    >>> parse_price('$15.99')
    1599
    >>> parse_price('$3.35')
    335

    '''
    n = ''
    for c in text:
        if c in '1234567890':
            n += c
    if '$' in text:
        n = int(n)
        return n

def parse_shipping(text): 
    '''
    >>> parse_shipping('Free shipping')
    0
    >>> parse_shipping('+$5.00 shipping')
    500
    >>> parse_shipping('+$15.80 shipping')
    1580
    '''
    
    n = ''
    for c in text:
        if c in '1234567890':
            n += c
    if '$' in text:
        n = int(n)
        return n
    elif 'Free' in text:
        return 0


# start of code

items = []


if __name__ == '__main__':

# command line arguments

    parser = argparse.ArgumentParser(description='Download information from ebay')
    parser.add_argument('search_term')
    parser.add_argument('--pgnumber', default=10)

    args = parser.parse_args()
    print("args.search_term=", args.search_term)

    # ebay search loop

    for pgnumber in range(1,int(args.pgnumber)+1):
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + args.search_term +'&_sacat=0&_pgn=' 
        url += str(pgnumber)
        url += '&rt=nc'

        # downloading url

        r = requests.get(url)
        status = r.status_code
        #print(status)

        html = r.text
        #print(html[:50])
        
        # processing html code

        soup = BeautifulSoup(html, 'html.parser')

        tags_items = soup.select('.s-item')
        for tag_item in tags_items:

            name = None
            tags_name = tag_item.select('.s-item__title')
            for tag in tags_name:
                name = tag.text

            freereturns = False
            tags_freereturns = tag_item.select('.s-item__free-returns')
            for tag in tags_freereturns:
                freereturns = True

            items_sold = None
            tags_itemssold = tag_item.select('.s-item__hotness')
            for tag in tags_itemssold:
                items_sold = parse_itemssold(tag.text)
                # print('tag=', tag)
            
            price = None
            tags_price = tag_item.select('.s-item__price')
            for tag in tags_price:
                price = parse_price(tag.text)

            shipping = None
            tags_shipping = tag_item.select('.s-item__shipping')
            for tag in tags_shipping:
                shipping = parse_shipping(tag.text)

            status = False
            tags_status = tag_item.select('.SECONDARY_INFO')
            for tag in tags_status:
                status = tag.text
    
            # formatting into items

            item = {
                'name': name,
                'free_returns': freereturns,
                'items_sold': items_sold,
                'price': price,
                'shipping': shipping,
                'status': status
            }
            items.append(item)
            
        # print('len(tags_items)=', len(tags_items))

        for item in items:
            print('item=', item)
            # print(url)

    filename = args.search_term+'.json'
    with open(filename, 'w', encoding='ascii') as f:
        f.write(json.dumps(items))