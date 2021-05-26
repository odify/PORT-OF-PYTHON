#!/usr/bin/env python3


from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs


session = HTMLSession()


def get_video_info(url):

    response = session.get(url)
    response.html.render(sleep=1)
    soup = bs(response.html.html, "html.parser")
    open("index.html", "w").write(response.html.html)
    result = {}
    result["title"] = soup.find("h1").text.strip()
    result["views"] = int(''.join([ c for c in soup.find("span", attrs={"class": "view-count"}).text if c.isdigit() ]))
    result["description"] = soup.find("yt-formatted-string", {"class": "content"}).text
    result["date_published"] = soup.find("div", {"id": "date"}).text[1:]
    result["duration"] = soup.find("span", {"class": "ytp-time-duration"}).text
    result["tags"] = ', '.join([ meta.attrs.get("content") for meta in soup.find_all("meta", {"property": "og:video:tag"}) ])
    text_yt_formatted_strings = soup.find_all("yt-formatted-string", {"id": "text", "class": "ytd-toggle-button-renderer"})
    result["likes"] = ''.join([ c for c in text_yt_formatted_strings[0].attrs.get("aria-label") if c.isdigit() ])
    result["likes"] = 0 if result['likes'] == '' else int(result['likes'])
    result["dislikes"] = ''.join([ c for c in text_yt_formatted_strings[1].attrs.get("aria-label") if c.isdigit() ])
    result['dislikes'] = 0 if result['dislikes'] == '' else int(result['dislikes'])
    channel_tag = soup.find("yt-formatted-string", {"class": "ytd-channel-name"}).find("a")
    channel_name = channel_tag.text
    channel_url = f"https://www.youtube.com{channel_tag['href']}"
    channel_subscribers = soup.find("yt-formatted-string", {"id": "owner-sub-count"}).text.strip()
    result['channel'] = {'name': channel_name, 'url': channel_url, 'subscribers': channel_subscribers}
    return result

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="YouTube Video Informations")
    parser.add_argument("url", help="VIDEO URL")


    args = parser.parse_args()
    url = args.url
    data = get_video_info(url)


    print("_________________________________________________________________________")

    print(f"Title: {data['title']}")

    print(f"Views: {data['views']}")

    print(f"Published at: {data['date_published']}")
    print(f"Video Duration: {data['duration']}")

    print(f"Video tags: {data['tags']}")
    print(f"Likes: {data['likes']}")
    print(f"Dislikes: {data['dislikes']}")
    print(f"\nDescription: {data['description']}\n")

    print(f"\nChannel Name: {data['channel']['name']}")
    print(f"Channel URL: {data['channel']['url']}")

    print(f"Channel Subscribers: {data['channel']['subscribers']}")
    print("-------------------------------------------------------------------------")


