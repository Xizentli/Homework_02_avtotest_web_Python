import yaml
from module import Site
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

# инициализация сайта
site = Site(testdata["address"])


def test_step1(locator_input_username, locator_input_password, locator_btn,
               locator_err_label, err_code):
    """Невозможность аутентификации с невалидными Username и Password"""

    # ввод данных в поле Username
    input1 = site.find_element("xpath", locator_input_username)
    input1.clear()
    input1.send_keys("test")

    # ввод данных в поле Password
    input2 = site.find_element("xpath", locator_input_password)
    input2.clear()
    input2.send_keys("test")

    # клик по кнопке Login
    btn = site.find_element("css", locator_btn)
    btn.click()

    # получение сообщения об ошибке
    err_label = site.find_element("xpath", locator_err_label)
    text = err_label.text

    assert text == err_code, "test1 FAIL"



def test_step2(locator_input_username, locator_input_password, locator_btn,
               locator_greeting_text, greeting_text):
    """Успешная аутентификация с валидными Username и Password"""

    # ввод данных в поле Username
    input1 = site.find_element("xpath", locator_input_username)
    input1.clear()
    input1.send_keys(testdata["username"])

    # ввод данных в поле Password
    input2 = site.find_element("xpath", locator_input_password)
    input2.clear()
    input2.send_keys(testdata["password"])

    # клик по кнопке Login
    btn = site.find_element("css", locator_btn)
    btn.click()

    # получение текста приветствия
    user_lable = site.find_element("xpath", locator_greeting_text)
    text = user_lable.text

    assert text == greeting_text, "test2 FAIL"


def test_step3(locator_create_btn,
               locator_title, locator_description, locator_content,
               locator_btn_save,
               locator_post_title):
    """Создание поста"""

    # клик по иконке Create new post
    btn = site.find_element("css", locator_create_btn)
    time.sleep(testdata["wait"])
    btn.click()
    time.sleep(testdata["wait"])

    # ввод данных в поле Title
    input1 = site.find_element("xpath", locator_title)
    input1.clear()
    input1.send_keys(testdata["title"])

    # ввод данных в поле Description
    input1 = site.find_element("xpath", locator_description)
    input1.clear()
    input1.send_keys(testdata["description"])

    # ввод данных в поле Content
    input1 = site.find_element("xpath", locator_content)
    input1.clear()
    input1.send_keys(testdata["content"])
    time.sleep(testdata["wait"])

    # клик по кнопке SAVE
    btn = site.find_element("css", locator_btn_save)
    btn.click()

    # проверяем, что пост сохранился
    time.sleep(testdata["wait"])
    post_title = site.find_element("xpath", locator_post_title)
    text = post_title.text
    assert text == testdata["title"], "test3 FAIL"


def test_step4(locator_btn_home, locator_first_post):
    """Проверка на наличие созданного поста на главной странице"""

    # клик по кнопке Home
    btn = site.find_element("css", locator_btn_home)
    btn.click()
    time.sleep(testdata["wait"])

    # поиск созданного поста
    post_title = site.find_element("xpath", locator_first_post)
    text = post_title.text

    site.close()

    assert text == testdata["title"], "test4 FAIL"
