# Fake User-Agent helps to avoid being blocked while scraping. 
# So, its better for me to use Fake User-Agent while scraping even it is small or big website. 
# FOR INSTALLATION: pip install fake-useragent.
from fake_useragent import UserAgent  
import requests
import time
url='''https://www.flipkart.com/search?q=headset&sid=0pm%2Cfcn&as=on&as-show=on&otracker=AS_QueryStore_Organic
AutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&as-pos=1&as-type=RECENT&suggestionId=headset%7C
Headset&requestId=c046f397-6340-4516-8325-f67a39892858&as-searchtext=headset&sort=popularity'''
session=requests.Session()
headers={
    "User-Agent" : UserAgent().random,
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "Referer": "https://www.Google.com/"
}
# You can further use proxy. The method is mentioned below.
# proxy="Whatever your proxy API is:"
# proxies={
    # "http": f"http//:{proxy}"     # 1st proxy is used for "http".
    # "https": f"http//:{proxy}"    # 2nd proxy is used for "https".
# }
time.sleep(2)
response=session.get(url,headers=headers)  # Use this: (proxies=proxies) here, if you are using proxy.
# I have used {encoding="utf-8"}. Because in this file, there are some characters which are not available on windows so it will help in achieving it.
with open("FILE.html","w",encoding="utf-8") as f:  
    f.write(response.text)