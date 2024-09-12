from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

def test_order(driver):
    driver.get('https://www.saucedemo.com/')

    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')

    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()

    #CHECKcart
    cart_item = driver.find_element(By.XPATH, '//div[text()="Sauce Labs Backpack"]')
    assert cart_item is not None, "Товар не был добавлен в корзину"
