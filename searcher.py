import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from global_vars import *


def search(author, title):
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    driver.get(CATALOGUE)
    sleep(SHORT_SLEEP)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB).send_keys(author).send_keys(Keys.TAB * 2).send_keys(title).send_keys(Keys.ENTER)
    actions.perform()
    sleep(LONG_SLEEP)

    driver.switch_to.frame(driver.find_element_by_xpath('//frame[@src="/opacg/html/frame2.xml"]'))
    try:
        result = driver.find_element_by_class_name('div_margin_right').text
    except NoSuchElementException:
        result = GLITCH
    driver.close()
    return result


if __name__ == '__main__':
    search('Bataille', '')
