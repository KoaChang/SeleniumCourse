#This file will include a class with instance methods.
#That will be responsible to interact with our website
#After we have some results, to apply filtrations.

from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltration:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def apply_star_rating(self,*star_values):
        star_filtration_box = self.driver.find_element_by_css_selector('div[data-filters-group="class"]')
        star_child_elements = star_filtration_box.find_elements_by_css_selector('div[data-filters-item*="class:class"]')

        for star_value in star_values:
            for star_element in star_child_elements:
                if star_element.get_attribute('data-filters-item')[-1] == f'{star_value}':
                    star_element.click()

    def sort_price_lowest_first(self):
        # option 1
        element = self.driver.find_element_by_xpath('//*[@id="search_results_table"]/div[2]/div/div/div/div[1]/span/button')
        element.click()
        price_lowest = self.driver.find_element_by_css_selector('button[data-id="price"]')
        price_lowest.click()

        # option 2










