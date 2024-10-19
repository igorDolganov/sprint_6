from selenium.webdriver.common.by import By


class OrderLocators:

    title_locator = [By.XPATH, '//div[text()="Для кого самокат"]']
    first_name_field = [By.XPATH, "//input[@placeholder='* Имя']"]
    last_name_field = [By.XPATH, '//input[@placeholder="* Фамилия"]']
    adress_field = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']
    station_field = [By.CLASS_NAME, 'select-search__input']
    station = [By.XPATH, '//button[@value="1"]']
    phone_number_field = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']
    next_button = [By.XPATH, '//button[text()="Далее"]']
    date_button = [By.XPATH, '//input[contains(@class,"Input_Input__1iN_Z Input_Responsible__1jDKN")]']
    date = [By.XPATH, '//div[@aria-label="Choose суббота, 2-е ноября 2024 г."]']
    rent_button = [By.TAG_NAME, 'span']
    rent_date = [By.XPATH, '//div[text()="трое суток"]']
    order_button = [By.XPATH, '(//button[text()="Заказать"])[2]']
    yes_button = [By.XPATH, '//button[text()="Да"]']
    order_success = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']
    samokat_button = [By.CSS_SELECTOR, 'div#root>div>div>div>a:nth-of-type(2)>img']