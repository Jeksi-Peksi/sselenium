import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])

def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, er1):
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    bth = site.find_element("css", btn_selector)
    bth.click()
    err_label = site.find_element("xpath", x_selector3)
    text = err_label.text
    site.close()
    assert text == er1

def test_step2(x_selector1, x_selector2, x_selector4, btn_selector, er2):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(name)
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(passwd)
    bth = site.find_element("css", btn_selector)
    bth.click()
    user_label = site.find_element("xpath", x_selector4)
    text = user_label.text
    site.close()
    assert text == er2

