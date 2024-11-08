"""
фикстуры
"""
import pytest
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def locator_input_username():
    """Локатор поля ввода Username"""
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def locator_input_password():
    """Локатор поля ввода Password"""
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def locator_err_label():
    """Локатор кода ошибки 401"""
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def locator_btn():
    """Локатор кнопки Login"""
    return "button"


@pytest.fixture()
def err_code():
    """Код ошибки"""
    return "401"


@pytest.fixture()
def locator_greeting_text():
    """Локатор текста приветствия"""
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture()
def greeting_text():
    """Текст приветствия"""
    return "Hello, {}".format(testdata["username"])


@pytest.fixture()
def locator_create_btn():
    """Локатор кнопки создания поста"""
    return "#create-btn"


@pytest.fixture()
def locator_title():
    """Локатор поля Title"""
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def locator_description():
    """Локатор поля Description"""
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def locator_content():
    """Локатор поля Content"""
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def locator_btn_save():
    """Локатор кнопки SAVE"""
    return ".button"


@pytest.fixture()
def locator_post_title():
    """Локатор заголовка нового поста на странице поста"""
    return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture()
def locator_btn_home():
    """Локатор кнопки Home"""
    return "span"


@pytest.fixture()
def locator_first_post():
    """Локатор заголовка первого поста на главной странице"""
    return """//*[@id="app"]/main/div/div[3]/div[1]/a[1]/h2"""
