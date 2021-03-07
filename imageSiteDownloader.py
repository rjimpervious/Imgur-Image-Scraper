import os, bs4, requests, re
from selenium import webdriver
from selenium.webdriver import ActionChains

os.makedirs('images', exist_ok=True)
os.chdir(r'C:\Users\RjImp\PycharmProjects\automate\imageSiteDownloader\images')

browser = webdriver.Chrome()
browser.get('https://imgur.com/')
browser.implicitly_wait(3)

agreeButton = browser.find_element_by_css_selector('#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-'
                                                   'overlay.qc-cmp2-footer-scrolled > div > button.css-flk0bs')
ActionChains(browser).click(agreeButton).perform()


browser.implicitly_wait(2)

searchBarSelector = '#root > div > div.desktop-app.App > div > ' \
                    'div.App-cover.NewCover.HomeCover.isCollapse > div.MoveContainer.Navbar.HomeNavbar > ' \
                    'div.NavbarContainer-center > div > form > input'
searchBar = browser.find_element_by_css_selector(searchBarSelector)
searchBar.send_keys('ocean')
searchBar.submit()

currentURL = browser.current_url
res = requests.get(currentURL)
soup = bs4.BeautifulSoup(res.text, 'html.parser')

imageElem = soup.select('#imagelist img')

if imageElem == []:
    print("Could not find one image at all")
else:
    for element in imageElem:
        try:
            fileSrc = element.get('src')
            imageUrl = 'https:' + fileSrc
            print("Downloading image {}".format(imageUrl))
            res.raise_for_status()

            imageFileNameRegex = re.compile(r'(i.imgur.com)(/)(\S+\.jpg)')
            fileName = imageFileNameRegex.search(fileSrc).group(3)
            imageFile = open(fileName, 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
        except AttributeError:
            pass


imageFile.close()
print("Done")



