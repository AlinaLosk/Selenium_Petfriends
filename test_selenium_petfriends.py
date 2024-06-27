import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def test_petfriends(web_browser):
    # Open PetFriends base page:
    web_browser.get("https://petfriends.skillfactory.ru/")

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = web_browser.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
    # btn_newuser = selenium.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")

    btn_newuser.click()
    time.sleep(5)

    # click existing user button
    # Ищем надпись "У меня уже есть аккаунт" и нажимаем на нее
    btn_exist_acc = web_browser.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # add email
    # Ищем поле ввода электронной почты, очищаем его, а затем вводим свой email

    field_email = web_browser.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("alina90@yandex.ru")

    # add password
    field_pass = web_browser.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("QAP167")

    # click submit button
    btn_submit = web_browser.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!
    assert  web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets',"login error"
