import time
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


CATALOGUE = 'http://opac.rgub.ru/opacg/guest.html'


def search(author, title):
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    driver.get(CATALOGUE)
    time.sleep(5)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB).send_keys(author).send_keys(Keys.TAB * 2).send_keys(title).send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(5)

    driver.switch_to.frame(driver.find_element_by_xpath('//frame[@src="/opacg/html/frame2.xml"]'))
    result = driver.find_element_by_class_name('div_margin_right').text
    # print(result.text)
    # "Базовый Расширенный Профессиональный"
    # "По данному запросу ничего не найдено"
    return result


if __name__ == '__main__':
    r = search('Diamond', '')
    print(r)
