import time
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def scroll(url):
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    actions = ActionChains(driver)
    actions = actions.send_keys(Keys.TAB)
    actions = actions.send_keys("Sacks")
    actions = actions.send_keys(Keys.TAB)
    actions = actions.send_keys(Keys.TAB)
    actions = actions.send_keys("for a hat")
    actions = actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(3)

    print(driver.page_source)

    driver.switch_to_frame(driver.find_element_by_xpath('//frame[@src="/opacg/html/frame2.xml"]'))
    print()
    print()
    print(driver.page_source)


if __name__ == '__main__':
    scroll('http://opac.rgub.ru/opacg/guest.html')
