# Imgur-Image-Scraper
An automatic image scraper(written in Python 3) using Selenium to navigate through Imgur.com and using BeautifulSoup4 library to parse the results.

Prerequisites:
  * BeautifulSoup 4 Library
  * Python 3
  * Selenium
  * Chrome Webdriver (You can use Firefox or any other browser as well).

Usage:

1. Run the script in the Terminal(Linux/Mac), CMD(Windows) or alternatively in an IDE.
![](https://github.com/rjimpervious/Imgur-Image-Scraper/blob/master/README_images/cmd.png?raw=true)

2. After entering the desired keyword to be searched. Script will open your selected Chrome(current selected web browser) through Selenium and navigate through Imgur. If you want to use another browser. Just edit the selected browser in the script but be sure to download the corresponding webdriver for the browser.
![](https://github.com/rjimpervious/Imgur-Image-Scraper/blob/master/README_images/imgur.png?raw=true)

2.  Script will automatically download all the images(JPG) in to the 'images' folder. The script will automatically make this one for you if you don't have at your current working directory.
![](https://github.com/rjimpervious/Imgur-Image-Scraper/blob/master/README_images/cmd2.png?raw=true)
![](https://github.com/rjimpervious/Imgur-Image-Scraper/blob/master/README_images/folder_images.png?raw=true)
