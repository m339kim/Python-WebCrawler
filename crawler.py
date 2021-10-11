from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium/webdriver.common.desired_capabilities import DesiredCapabilities 

class craigslist_crawler(object):
    # if called, query and max_price goes into the corresponding position of the url.
    def __init__(self, query, max_price):
        self.max_price = max_price
        self.query = query
        self.url = f"https://kitchener.craigslist.org/search/sss?query={query}&max_price={max_price}"
        self.driver = webdriver.Chrome(C:/Driverchromedriver.exe) # Chome WebDriver, name and location in computer

    def load_page(self):
        driver = self.driver
        driver.get(self.url) # access via url
        all_data = driver.find_elements_by_class_name("result-row")
        # applied to each result-row
        for data in all_data:
            title = data.text.split("$")
            if title[0] == "":
                title=title[1]
            else:
                title=title[0]
            
            title=data.text.split("\n")
            price = title[0]
            title=title[-1] #last
            
            title=title.split(" ")
            month = title[0]
            day = title [1]

            title = .join(" ")title[2:] #title only
            date = month + " " + day # jan 16

            print(title)

    def close_webdriver(self):
        self.driver.close()
        print("good bye")

query = "iphone"
max_price = 500
crawler = craigslist_crawler(query, max_price)
crawler.load_page()
