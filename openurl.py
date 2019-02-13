import urllib3
import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        # 使用代理
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        html = response.data
        # print(response.status)
        return html
    except Exception as e:
        print(e)
        return None


def get_soup(url):
    if not url:
        return None
    try:
        soup = BeautifulSoup(get_html(url), 'html.parser')# 指定解析器
    except Exception as e:
        print(e)
        return None
    return soup


def get_ele(soup, selector):
    try:
        ele = soup.select(selector)
        return ele
    except Exception as e:
        print(e)
    return None

def main():  
    url = 'http://news.163.com/rank/'
    soup = get_soup(url)
    # ele = get_ele(soup, )
    print(soup.title)
    # print(soup)
    # for k in soup.find_all('div', class_ ='tabBox'):
    #     for j in k.find_all('div', class_ = 'tabContents' ):
    #         for i in j.find_all('tr'):
    #             for x in i.find_all('td', class_ = 'cBlue'):
    #                 if int(x.string) > 1000 :
    #                     for y in i.find_all('a'):
    #                         print(y['href'] + ' ' + y.string)
    #                         print(x.string)
                
                    
        # print(k)
    print()
    for target in soup.find_all('div', class_ = 'taxBox') \
                        .find('div', class_ = 'tabContents') \
                        .find('tr'):
                        for x in target.find_all('td', class_ = 'cBlue'):
                            if int(x.string) > 1000 :
                                for y in target.find_all('a'):
                                    print(y['href'] + ' ' + y.string)
                                    print(x.string)

if __name__ == '__main__':
    main()