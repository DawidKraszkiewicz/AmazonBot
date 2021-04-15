from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.chrome.service import Service
options = Options()
options.page_load_strategy = 'eager'
service = Service("path to your chrome webdriver")
service.start()
login_url = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
item_url = "https://www.amazon.com/dp/B08J6F174Z?smid=ATVPDKIKX0DER&tag=data20-20#aod"

def purchase(username, password):
    address_xpath = '//*[@id="address-book-entry-0"]/div[2]/span/a'
    order_xpath = '//*[@id="hlb-ptc-btn-native"]'
    payment_xpath = '//*[@id="placeYourOrder"]/span/input'
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    driver.get(login_url)

    driver.find_element_by_xpath(
        '//*[@id="ap_email"]').send_keys(username + Keys.RETURN)
    time.sleep(5)
    driver.find_element_by_xpath(
        '//*[@id="ap_password"]').send_keys(password + Keys.RETURN)
    time.sleep(20)
    driver.refresh()
    driver.get(item_url)


    while not driver.find_elements_by_xpath('//*[@id="add-to-cart-button"]'):
        driver.refresh()
        time.sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="add-to-cart-button"]').click()

    place_your_order = wait.until(
        presence_of_element_located((By.XPATH, order_xpath)))
    place_your_order.click()

    payment_in_pln = wait.until(
        presence_of_element_located((By.XPATH, payment_xpath)))
    payment_in_pln.click()



purchase('email', 'password')