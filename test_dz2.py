import yaml
from module import Site
from selenium import webdriver
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])
name = testdata["username"]
passwd = testdata["password"]
titl = testdata["title"]
cont = testdata["content"]
descript = testdata["description"]

def test_dz(x_selector1, x_selector2, x_title, btn_login, btn_createpost, btn_save, er3, title, description, content):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(name)
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(passwd)
    bth = site.find_element("css", btn_login)
    bth.click()
    time.sleep(3)
    btn2 = site.find_element("css", btn_createpost)
    btn2.click()
    time.sleep(3)
    post_tittle = site.find_element("xpath", title)
    post_tittle.clear()
    post_tittle.send_keys(titl)
    post_content = site.find_element("xpath", content)
    post_content.clear()
    post_content.send_keys(cont)
    post_description = site.find_element("xpath", description)
    post_description.clear()
    post_description.send_keys(descript)
    btn3 = site.find_element("css", btn_save)
    btn3.click()
    time.sleep(3)
    post_label = site.find_element("xpath", x_title)
    text = post_label.text
    site.close()
    assert text == er3