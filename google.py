from selenium import webdriver
from time import sleep

print("enter what you want to search: \n")
search = input()

print("what do you want to see:  \n 1 : links \n 2 : images \n 3 : videos \n 4 : news")

c = input()



browser = webdriver.Chrome("C:/Users/asus/Downloads/chromedriver.exe")

browser.get("https://www.google.com/")
sleep(1.5)
browser.find_element_by_xpath("//input[@name=\"q\"]")\
    .send_keys(search)


if c=='1':
    browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div[1]/div[3]/center/input[1]") \
        .click()
elif c=='2':
    browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div[1]/div[3]/center/input[1]") \
        .click()
    sleep(0.4)
    browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div/div/div[1]/div/div/div[1]/div/div[2]/a") \
        .click()
elif c=='3':
    browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div[1]/div[3]/center/input[1]") \
        .click()
    sleep(0.4)
    browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div/div/div[1]/div/div/div[1]/div/div[4]/a") \
        .click()
elif c=='4':
    browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div[1]/div[3]/center/input[1]") \
        .click()
    sleep(0.4)
    browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div/div/div[1]/div/div/div[1]/div/div[5]/a") \
        .click()
else:
    print("wrong choise")






