from booking.booking import Booking
from webdriver_manager.chrome import ChromeDriverManager

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='USD')
    bot.select_place_to_go('New York')
    bot.select_dates(check_in_date='2022-07-21',check_out_date='2022-08-15')
    bot.select_adults(10)
    bot.click_search()
    bot.apply_filtrations()
    bot.refresh() #workoutaround to make sure bot grabs hotel names properly
    bot.report_results()








