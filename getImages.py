import string
import itertools
import random
import urllib
import urllib.request
import os
import requests
from bs4 import BeautifulSoup
import cfscrape


def createRandomSixChar():
    N = 6
    randomurl = "".join(random.choices(
        string.ascii_uppercase + string.digits, k=N))
    randomurl = randomurl.lower()
    return randomurl


def createUrl(randomString):
    return "https://prnt.sc/" + randomString


def createListOfUrls(numberOfUrls):
    list_of_urls = list()
    for i in range(0, numberOfUrls):
        url = createUrl(createRandomSixChar())
        list_of_urls.append(url)
    return list_of_urls


def downloadImages(listOfUrls):
    count = 0
    for url in listOfUrls:
        scraper = cfscrape.create_scraper()
        html = scraper.get(url).text
        soup = BeautifulSoup(html, "html.parser")

        img = soup.find("img", {"id": "screenshot-image"})
        if img is not None:
            imgSrc = str(img.attrs['src'])
            if imgSrc.startswith("//") == False:
                # urllib.request.urlretrieve(imgSrc, os.path.basename(imgSrc))
                cfurl = scraper.get(imgSrc).content
                if not os.path.exists("./"+imgSrc):
                    with open("images/" + str(count)+".png", 'wb') as f:
                        f.write(cfurl)
                        f.close()
                    count += 1
                    print(count)


def main():
    listOfUrls = createListOfUrls(10000)
    downloadImages(listOfUrls)


main()
