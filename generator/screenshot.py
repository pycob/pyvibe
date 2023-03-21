from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Get the current directory
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print("dir_path = ", dir_path)

# Remove the last folder from the path
dir_path = os.path.dirname(dir_path)
print("dir_path = ", dir_path)

global driver
driver = None

def take_screenshot(name: str):
    global driver
    if driver is None:
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("window-size=1024,768")
        options.add_argument("--hide-scrollbars")
        # Here Chrome will be used
        driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)

    # URL of website
    url = "file://" + dir_path + "/docs/gallery/" + name + ".html"

    # Opening the website
    driver.get(url)
    driver.save_screenshot(f"docs/img/{name}.png")

# Get all the html files in the dir_path + "/docs/gallery" folder
import glob
files = glob.glob(dir_path + "/docs/gallery/*.html")
for file in files:
    # Get the name of the file
    name = os.path.basename(file)
    # Remove the .html extension
    name = os.path.splitext(name)[0]
    print("screenshotting = ", name)
    take_screenshot(name)