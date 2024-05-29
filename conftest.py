import yaml
import pytest

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
name = testdata["username"]

@pytest.fixture()
def x_selector1():
    return """//*[@id="login"]/div[1]/label/input"""
@pytest.fixture()
def x_selector2():
    return """//*[@id="login"]/div[2]/label/input"""
@pytest.fixture()
def x_selector3():
    return """//*@id="app"]/main/div/div/div[2]/h2"""
@pytest.fixture()
def x_selector4():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""
@pytest.fixture()
def btn_login():
    return """button"""
@pytest.fixture()
def er1():
    return "401"
@pytest.fixture()
def er2():
    return "Hello, {}".format(name)

@pytest.fixture()
def er3():
    return "Just new post"

@pytest.fixture()
def title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""

@pytest.fixture()
def content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture()
def description():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""

@pytest.fixture()
def x_title():
    return """//*[@id="app"]/main/div/div[1]/h1"""

@pytest.fixture()
def btn_createpost():
    return """#create-btn"""

@pytest.fixture()
def btn_save():
    return """#create-item > div > div > div:nth-child(7) > div > button > span"""