import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://mynickname.com/ru/generate")

links = []

while len(links) < 100:
    button_xpath = "/html/body/div[1]/div[1]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input"
    driver.find_element_by_xpath(button_xpath).click()
    link = driver.find_element_by_id('register').get_attribute('href')[37:]
    links.append(link)
    print(links)

driver.quit()

# Запись значений в текстовый файл
with open("links.txt", "w") as file:
    for link in links:
        file.write(link + "\n")


