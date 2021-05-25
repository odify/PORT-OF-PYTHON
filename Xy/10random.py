from scraper import Scraper    


if __name__ == '__main__':
scraper = Scraper()    
proxies = scraper.scrape(size=10)  

while proxies.qsize:
proxy = proxies.get()
print(proxy)
