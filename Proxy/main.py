#!/usr/bin/env python3



import requests
import random
from bs4 import BeautifulSoup as bs

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # get the HTTP response and construct soup object
    soup = bs(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return proxies


def get_session(proxies):
    # construct an HTTP session
    session = requests.Session()
    # choose one random proxy
    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session


if __name__ == "__main__":
    # proxies = get_free_proxies()
    proxies = [
        '167.172.248.53:3128',
        '194.226.34.132:5555',
        '203.202.245.62:80',
        '141.0.70.211:8080',
        '118.69.50.155:80',
        '201.55.164.177:3128',
        '51.15.166.107:3128',
        '91.205.218.64:80',
        '128.199.237.57:8080',
    ]
    for i in range(5):
        s = get_session(proxies)
        try:
            print("Request page with IP:", s.get("http://icanhazip.com", timeout=1.5).text.strip())
        except Exception as e:
            continue


MULTI_TOR=

import requests
from stem.control import Controller
from stem import Signal

def get_tor_session():
    # initialize a requests Session
    session = requests.Session()
    # setting the proxy of both http & https to the localhost:9050 
    # (Tor service must be installed and started in your machine)
    session.proxies = {"http": "socks5://localhost:9050", "https": "socks5://localhost:9050"}
    return session

def renew_connection():
    with Controller.from_port(port=9051) as c:
        c.authenticate()
        # send NEWNYM signal to establish a new clean connection through the Tor network
        c.signal(Signal.NEWNYM)


if __name__ == "__main__":
    s = get_tor_session()
    ip = s.get("http://icanhazip.com").text
    print("IP:", ip)
    renew_connection()
    s = get_tor_session()
    ip = s.get("http://icanhazip.com").text
    print("IP:", ip)


TOR=

import requests


def get_tor_session():
    # initialize a requests Session
    session = requests.Session()
    # this requires a running Tor service in your machine and listening on port 9050 (by default)
    session.proxies = {"http": "socks5://localhost:9050", "https": "socks5://localhost:9050"}
    return session


if __name__ == "__main__":
    s = get_tor_session()
    ip = s.get("http://icanhazip.com").text
    print("IP:", ip)


CRAWLERA=

import requests

url = "http://icanhazip.com"
proxy_host = "proxy.crawlera.com"
proxy_port = "8010"
proxy_auth = ":"
proxies = {
       "https": f"https://{proxy_auth}@{proxy_host}:{proxy_port}/",
       "http": f"http://{proxy_auth}@{proxy_host}:{proxy_port}/"
}

r = requests.get(url, proxies=proxies, verify=False)
