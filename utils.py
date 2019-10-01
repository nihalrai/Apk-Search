import sys
import json

from selenium import webdriver
from pyvirtualdisplay import Display

class Browser:
    def __init__(self):
        pass
    
    def set_browser(self):
        try:
            driver = webdriver.Firefox()
            return driver
        except:
            return None

    def headless_selenium(self):
        display = Display()
        display.start()
        try:
            driver = self.set_browser()
            if not driver:
                return None
            return driver, display
        except:
            display.stop()
            return None, None
    
    def run(self):
        try:
            return self.headless_selenium()
        except:
            return None
        

def display_json(content):
    try:
        return json.dumps(content, indent=4)
    except:
        return content
    
def load_json(content):
    try:
        return json.loads(content)
    except:
        return None