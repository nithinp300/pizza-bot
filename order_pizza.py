# selenium for web driving
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# to pause between navigation
import time

# for file management
import os

driver = webdriver.Chrome('/Users/nithin/Downloads/chromedriver')
driver.get('https://www.pizzahut.com/index.php#/home')
time.sleep(3)
driver.get('https://www.pizzahut.com/index.php#/localize/pizza/');
time.sleep(3)
carryout = driver.find_element_by_id('find-occasion-carryout')
carryout.click()
time.sleep(3)
zip_input = driver.find_element_by_name('carryOutZip')
zip_input.send_keys('75034')
time.sleep(3)
find_a_store = driver.find_element_by_id('ph-find-store')
find_a_store.click()
time.sleep(5)
order_carryout = driver.find_element_by_link_text('Order Carryout')
order_carryout.click()
time.sleep(5)
select = Select(driver.find_element_by_id('crust-cheese-pizza'))
select.select_by_value('P')
time.sleep(3)
add_to_order = driver.find_element_by_id('ato-cheese-pizza')
add_to_order.click()
time.sleep(5)
cart = driver.find_element_by_id('cart-quantity-icon')
cart.click()
time.sleep(5)
checkout = driver.find_element_by_id('checkout-bottom-os')
checkout.click()
time.sleep(5)
# we get password for pizzahut
php = ''
with open('/Users/nithin/Documents/php.txt', 'r') as file:
    php = file.read()
email = driver.find_element_by_name('email')
password = driver.find_element_by_name('password')
login_button = driver.find_element_by_id('ph-login')
# we send text input to email and password fields
email.send_keys('nithinp300@gmail.com')
time.sleep(3)
password.send_keys(php)
time.sleep(3)
login_button.click()
time.sleep(6)
payment = driver.find_element_by_id('ph-co-2-continue')
payment.click()
time.sleep(5)
pay_in_store = driver.find_element_by_css_selector("input[value='ca']")
pay_in_store.click()
time.sleep(4)
sign_out = driver.find_element_by_id('ph-sign-out')
sign_out.click()
time.sleep(5)
driver.quit()
