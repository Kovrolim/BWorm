import requests
from lxml import html
import sqlite3

def create_main_db():
    base = sqlite3.connect('main.db')
    base.execute('CREATE TABLE IF NOT EXISTS list_url(name, url_book, shop, price, availibility)')
    base.commit()
    base.close()

def add_items(name, url_book, shop, price, availibility):
    base = sqlite3.connect('main.db')
    cur = base.cursor()
    cur.execute('INsert into list_url (name, url_book, shop, price, availibility) values (?,?,?,?,?)',
                (name, url_book, shop, price, availibility))
    base.commit()
    base.close()

def search_by_name(name):
    result = s_labirint(name)
    return result


def s_labirint(name):
    headers = {
        'Accept-Language': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    url = 'https://www.labirint.ru/search/%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0%20%D0%BC%D1%8B%20%D0%BE%D1%81%D1%82%D0%B0%D0%B5%D0%BC%D1%81%D1%8F%20%D0%BE%D0%B4%D0%BD%D0%B8/?stype=0'
    page = requests.get(url, headers=headers)
    print(page.text)
    tree = html.fromstring(page.content)
    items = tree.xpath('//*[@class="product need-watch watched"]/@data-product-id')
    for i in items:
        f_price = tree.xpath(f'//*[@data-product-id="{i}"]//span[@class ="price-val"]/span/text()')
        f_name = tree.xpath(f'//*[@data-product-id="{i}"]//span[@class ="product-title"]/text()')

    print(price[0])
