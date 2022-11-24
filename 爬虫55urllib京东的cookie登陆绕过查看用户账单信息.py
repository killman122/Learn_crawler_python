import urllib.parse
import urllib.request
import json
import random
import requests
import urllib.error
def get_ua():
    first_num=random.randint(55,102)
    third_num=random.randint(0,5005)
    fourth_num=random.randint(0,140)
    three_num=random.randint(0,1245)
    four_num=random.randint(0,44)
    os_type=[
        '(Windows NT 10.0; Win64; x64)','(Windows NT6.1; Win64; x64)','(iPhone; CPU iPhone OS 10_3_1 like Mac OS X)','(X11; Linux x86_64)','(Macintosh; Intel Mac OS X 10_12_6)'
    ]
    edge_version='Edg/{}.0.{}.{}'.format(first_num,three_num,four_num)
    chorme_version='Chrome/{}.0.{}.{}'.format(first_num,third_num,fourth_num)
    ua=''.join(['Mozilla/5.0 ',random.choice(os_type),' AppleWebKit/537.36 ', '(KHTML, like Gecko) ',chorme_version,' Safari/537.36 ',edge_version])
    return ua
ua=get_ua()
#print(ua)
headers={
    'User-Agent':ua,
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'cookie': '__jdu=16324518192341062793036; shshshfpa=2665e25e-3a63-c142-aa47-52e2caf365f2-1632451822; pinId=aOSlPckL8a0U7Zta7IoZj7V9-x-f3wj7; pin=jd_6f09619712870; unick=6f0%E7%8E%8B%E9%81%93; _tp=qk9uWcjtimpRuAKZFtTTZH%2F2sICJ07GncQhiDIxAYSs%3D; _pst=jd_6f09619712870; user-key=285721b2-422a-4259-bce1-ab3b6b34981a; shshshfpb=s4mUJHWXRE67ZAU3MPSN9iw%3D%3D; __jdv=122270672%7Ckong%7Ct_2013114075_%7Cjingfen%7C0fe2e0f593da4676821ac194b57c7217%7C1655574468054; unpl=JF8EAJ9nNSttDE9SVhMASxQRTV1RWw9cHEcFamVVAVVcGVAMGwUZRhR7XlVdXhRKEB9sbhRUVFNLVA4aCisSEHtdVV9eDkIQAmthNWRVUCVUSBtsGHwQBhAZbl4IexcCX2cCVl5dT1QMGwoYEBVLXFNdWwBJFgFoVzVUW2h7ZAQrAysTIAAzVRNdD0kUBmtnDFRVW0lRBRoFGBQYSVxWWW0JexQ; PCSYCityID=CN_650000_650100_0; shshshfp=c7f4f892e8bce5a1b4c02bc44aa322d7; shshshsID=053be1df193329efc327da28f7231399_2_1656411085008; __jda=122270672.16324518192341062793036.1632451819.1655574441.1656411070.50; __jdc=122270672; ipLoc-djd=31-2652-0-0; areaId=31; wlfstk_smdl=vbq5b1521iv0i35z6howjzkt3zf44tmz; TrackID=1mJE9XkV8emcnFJZ3RnVGlGPV3avRP5tnuecADHbRd_c7YaH8krr-ld-7kIny5K-GOHPDovGO1kFt7TZae4zka2i23vPkeeERjjBYYyo60-nCdaTjooU_pPuuFQVSFQ40q26TqmFGgdDSZB8VuVt8AA; thor=7C6FF34CFE87F5485F6D363FCFE67C3B9D44EE885FC4487745A15C9BC5713F36B3B3FFFED184E1EB9C809CFBC1924CCE2FC2211E550D91BABA32393ED02BA47618C764DFEA1262197B7B19C54F7AEDAC9863476C8A21FA968AF85A7F87C9A452B1533745BAC7E64977BB6DD539C3B3E655F7D6448CCA9F965DFC6DA41540B9AAC98B37B5BE6E7EA6A504DD1137FEE9E4385CA4040143966C9E4BACD35EE89760; ceshi3.com=201; __jdb=122270672.9.16324518192341062793036|50.1656411070; 3AB9D23F7A4B3C9B=5JRV6BSWBJKG3KQS6JKXAROGFYZQ23YH5EDLH4AVILREO4NBJIGN6PZR4ODKYJ6EY65A2BJZHG6JE7TMODYVUUQRDE',
    'pragma': 'no-cache',
    'referer': 'https://order.jd.com/center/list.action',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
}
url='https://order.jd.com/center/list.action'
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)

