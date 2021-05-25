from scraper import Scraper


if __name__ == '__main__':
 scraper = Scraper()    
 proxies = scraper.scrape(protocol='SSL')
    
 while proxies.qsize:
  proxy = proxies.get()
  print(proxy)
