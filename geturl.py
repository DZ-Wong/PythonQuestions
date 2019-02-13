from lxml import etree
import urllib3
import requests

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


def get_html2(url):
    s = requests.Session()
    r = s.get(url)
    return etree.HTML(r.text)

def main():  
    url = 'http://news.163.com/rank/'
    html = get_html2(url)
    # result = etree.tostring(html, encoding='gb2312')
    # print(type(html))
    # print(type(result))
    # print(result.decode('gb2312'))
    node = html.xpath('//div[@class="tabBox"]/div[@class="tabContents"]/table/tr')

    for x in node:
        print("#########")
        print(etree.tostring(x, encoding='gb2312').decode("gb2312"))
        y = x.xpath('//tr/td/a')[0].text
        print(y)
        print("---------")
        # print(etree.tostring(x, encoding='gb2312').decode("gb2312"))
        # print("--------")
    # print(node)

if __name__ == '__main__':
    main()

