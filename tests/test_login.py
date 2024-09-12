from pages.login_page import LoginPage


def test_login(driver):
    driver.get('https://www.saucedemo.com/')

    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')

    #CHECK login
    assert "inventory" in driver.current_url, "Не удалось авторизоваться"
