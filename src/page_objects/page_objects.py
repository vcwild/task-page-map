from abc import ABC


class SeleniumObject:
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def quit(self):
        self.driver.quit()


class Page(ABC, SeleniumObject):
    def __init__(self, driver, url=''):
        self.driver = driver
        self.url = url
        self._reflection()

    def open(self):
        self.driver.get(self.url)

    def _reflection(self):
        for attr in dir(self):
            attr_val = getattr(self, attr)
            if isinstance(attr_val, PageElement):
                attr_val.driver = self.driver


class PageElement(ABC, SeleniumObject):
    def __init__(self, driver=None):
        self.driver = driver
