from selenium import webdriver
import os
from booking import constants as const
from webdriver_manager.chrome import ChromeDriverManager
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from selenium.webdriver.chrome.options import Options
from prettytable import PrettyTable
import pandas as pd
import time

class Booking(webdriver.Chrome):
    def __init__(self,teardown=False):
        options = Options()
        options.headless = False

        self.teardown = teardown
        super(Booking,self).__init__(ChromeDriverManager().install(),options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def change_currency(self,currency):
        currency_element = self.find_element_by_xpath('//*[@id="b2indexPage"]/header/nav[1]/div[2]/div[1]/button')
        currency_element.click()
        selected_currency_element = self.find_element_by_css_selector(f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_currency_element.click()

    def select_place_to_go(self,place_to_go):
        search_field = self.find_element_by_xpath('//*[@id="ss"]')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element_by_xpath('//*[@id="frm"]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]')
        first_result.click()

    def select_dates(self,check_in_date,check_out_date):
        # messing around with ways to change date calendar to get exactly the dates you want
        # next_button = self.find_element_by_xpath('//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[2]')
        # while self.find_element_by_css_selector('div[class="bui-calendar__month"]').text != 'January 2023':
        #     next_button.click()

        check_in_element = self.find_element_by_css_selector(f'td[data-date="{check_in_date}"]')
        check_in_element.click()
        check_out_element = self.find_element_by_css_selector(f'td[data-date="{check_out_date}"]')
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element_by_id('xp__guests__toggle')
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adults_element.click()
            # If the value of adults reaches 1, then we should get out
            # of the while loop
            adults_value_element = self.find_element_by_id('group_adults')
            adults_value = adults_value_element.get_attribute(
                'value'
            )  # Should give back the adults count

            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )

        for _ in range(count - 1):
            increase_button_element.click()

    def click_search(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(3,4,5)
        filtration.sort_price_lowest_first()

    def report_results(self):
        hotel_boxes = self.find_element_by_class_name('d4924c9e74')
        report = BookingReport(hotel_boxes)

        titles = ['Hotel Name','Hotel Price','Hotel Score']
        table = PrettyTable(field_names=titles)
        list_of_lists = report.pull_deal_box_attributes()
        table.add_rows(list_of_lists)
        print(table)

        list_of_lists = [titles] + list_of_lists
        df = pd.DataFrame(list_of_lists)
        df.to_csv('table.csv',header=False,index=False)



