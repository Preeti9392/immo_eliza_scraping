import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
class ImmowebScraper:
    def __init__(self, pages):
        self.urls_list=[]
        self.pages=pages
        self.immoweb_url=[]
        
        self.features=[]
        
        
    
        self.headers =  {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) '
                'Gecko/20100101 Firefox/115.0'
            ),
            'Accept': (
                'text/html,application/xhtml+xml,application/xml;q=0.9,'
                'image/avif,image/webp,*/*;q=0.8'
            ),
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers',
            }
    
    def get_urls_list(self):
        
        for i in range(1, self.pages+1):
            url_house = f"https://www.immoweb.be/en/search/house/for-sale?countries=BE&page={i}"
            url_apartment = f"https://www.immoweb.be/en/search/apartment/for-sale?countries=BE&page={i}"
            self.urls_list.append(url_house)
            self.urls_list.append(url_apartment)
   
        print(f'Number of Base URLs generated: {len(self.urls_list)}')
        return(self.urls_list)
    
    def immoweb_url_list(self,url):
        time.sleep(0.1)
        lst=[]
        try:    
            response=requests.get(url, headers=self.headers)
            content=response.content
            soup=BeautifulSoup(content, "html.parser")
            #print(soup.prettify())
                
            for tag in soup.find_all("a", attrs={"class": "card__title-link"}):
                href=tag.get("href")
                if "new-real-estate-project" not in href:
                    lst.append(href)
                    
        except Exception as e:
            print(f"error occured: {e}")
        
        return (lst)   
        
        
    def immoweb_url_thread(self):
        #self.urls_list = self.get_urls_list()
        with ThreadPoolExecutor(max_workers=9) as executor:
            
            results = executor.map(lambda url: self.immoweb_url_list(url), self.urls_list)
            for result in results:
                self.immoweb_url.extend(result)
        print(self.immoweb_url)
        df=pd.DataFrame({"immoweb_url":self.immoweb_url})
        df.to_csv("immoweb_url_file.csv")
        return self.immoweb_url
    
   
    
    def get_attribute_value(self, url):
        dictionary={}
        try:    
            response=requests.get(url, headers=self.headers)
            print(response.status_code)
            content=response.content
            soup=BeautifulSoup(content, "html.parser")
            tr_tag=(soup.find_all("tr", attrs={"class":"classified-table__row" }))
            print(tr_tag)
        except Exception as e:
            print(e)
        
        try:    
            for tag in tr_tag:
                th_tag=tag.find("th")
                td_tag=tag.find("td")
                
                print(th_tag, td_tag)
               
                header_name=th_tag.get_text(strip=True)
                header_data=(td_tag.get_text(strip=True))
                print("__________________________")
                print(f"HEADER NAME:{header_name}")
                print(f" HEADER DATA  :{header_data}")
                dictionary[header_name]= header_data
        except Exception as e:
            print(f"error is {e}")
        
        return(dictionary)
        
            
    def thread_for_attrvalue(self):
        X=pd.read_csv("./immoweb_url_file1.csv")
        self.immoweb_url=X["immoweb_url"][:1].to_list()  
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(lambda url: self.get_attribute_value(url), self.immoweb_url)
            try:    
                for result in results:
                    self.features.append(result)
            except:
                pass
                
        print(self.features)
        df1=pd.DataFrame(self.features)
        df1.to_csv("dataset_file.csv")
        return self.features
    
        
    
        