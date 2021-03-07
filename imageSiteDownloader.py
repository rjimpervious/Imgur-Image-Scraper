import os, bs4, requests, re
from selenium import webdriver
from selenium.webdriver import ActionChains


def main():
    searchVar = input("Enter a topic or a name to be searched: \n")
    os.makedirs('images', exist_ok=True) # creates a folder for to download the images
    os.chdir(os.getcwd() + '/images')

    browser = webdriver.Chrome()
    browser.get('https://imgur.com/')
    browser.implicitly_wait(3)

    # Browser Actions to accept the cookies popup
    agreeButton = browser.find_element_by_css_selector('#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-'
                                                       'overlay.qc-cmp2-footer-scrolled > div > button.css-flk0bs')
    ActionChains(browser).click(agreeButton).perform()


    browser.implicitly_wait(2)

    searchBarSelector = '#root > div > div.desktop-app.App > div > ' \
                        'div.App-cover.NewCover.HomeCover.isCollapse > div.MoveContainer.Navbar.HomeNavbar > ' \
                        'div.NavbarContainer-center > div > form > input'
    searchBar = browser.find_element_by_css_selector(searchBarSelector)
    searchBar.send_keys(searchVar)
    searchBar.submit()

    currentURL = browser.current_url
    res = requests.get(currentURL)
    res.raise_for_status()
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
                res = requests.get(imageUrl)
                res.raise_for_status()

                # Regex to separate the image name from the URL
                imageFileNameRegex = re.compile(r'(i.imgur.com)(/)(\S+\.jpg)')
                fileName = imageFileNameRegex.search(fileSrc).group(3)
                # Writing the files
                imageFile = open(fileName, 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
            except AttributeError:
                pass

    print("Done")


if __name__ == '__main__':
    main()



