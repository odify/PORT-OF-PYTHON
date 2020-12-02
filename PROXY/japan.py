from scraper import Scraper


if __name__ == '__main__':
 scraper = Scraper()    
 proxies = scraper.scrape(country='Japan', size=3)
    
 while proxies.qsize:
  proxy = proxies.get()
  print(proxy)
