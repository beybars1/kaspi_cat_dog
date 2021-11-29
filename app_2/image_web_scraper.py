import bs4
import requests
from selenium import webdriver
import os
import time

# creating a directory to save images
folder_name = 'cat'
# folder_name = 'dog'

if not os.path.isdir(folder_name):
    os.makedirs(folder_name)


def download_image(url, folder_name, num):
    # write image to file
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder_name, str(num) + ".jpg"), 'wb') as file:
            file.write(response.content)

# chrome driver initialization
chromePath = r'chromedriver.exe'
driver = webdriver.Chrome(chromePath)

# google image search URL
search_URL = "https://www.google.com/search?q=cat&tbm=isch&ved=2ahUKEwiTkszL2LX0AhUNwSoKHYAbDNwQ2-cCegQIABAA&oq=cat&gs_lcp=CgNpbWcQAzIHCAAQsQMQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzoICAAQgAQQsQM6BQgAEIAEUMUEWMQIYJMLaABwAHgAgAGBAYgB3wOSAQMwLjSYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=xaWgYdObB42CqwGAt7DgDQ&bih=739&biw=1536"
driver.get(search_URL)

# wait command, you need to scroll down the page to the maximum and then press any button
a = input("Waiting...")

# scrolling all the way up
driver.execute_script("window.scrollTo(0, 0);")

page_html = driver.page_source
pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
containers = pageSoup.findAll('div', {'class': "isv-r PNCib MSM1fd BUooTd"})

print(len(containers))

len_containers = len(containers)

for i in range(1, len_containers + 1):
    if i % 25 == 0:
        continue

    xPath = """//*[@id="islrg"]/div[1]/div[%s]""" % (i)
    previewImageXPath = """//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img""" % (i)

    try:
        previewImageElement = driver.find_element_by_xpath(previewImageXPath)
        previewImageURL = previewImageElement.get_attribute("src")
    except:
        print("here")
        continue

    driver.find_element_by_xpath(xPath).click()
    timeStarted = time.time()
    try:
        imageElement = driver.find_element_by_xpath(
            """//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img""")
        imageURL = imageElement.get_attribute('src')
    except:
        continue
    # Downloading image
    try:
        download_image(imageURL, folder_name, i)
        print("Downloaded element %s out of %s total. URL: %s" % (i, len_containers + 1, imageURL))
    except:
        print("Couldn't download an image %s, continuing downloading the next one" % (i))

