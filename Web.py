
from cv import *
from selenium import webdriver
import os
from bs4 import BeautifulSoup
import time

chromedriver_location = "C:/Users/stark/Downloads/chromedriver"

driver = webdriver.Chrome(chromedriver_location)
driver.get('https://captcha.com/demos/features/captcha-demo.aspx')

captcha_img = '//*[@id="demoCaptcha_CaptchaImage"]'

input_box = '//*[@id="captchaCode"]'

submit_button = '//*[@id="validateCaptchaButton"]'

result = '/html/body/div[1]/div[1]/div[1]/form/fieldset[1]/div[2]/span/span'
result_id = 'validationResult'

#performing action


with open('Captcha.png', 'wb') as file:
    file.write(driver.find_element_by_xpath(captcha_img).screenshot_as_png)

driver.find_element_by_xpath(input_box).send_keys(pipeline())
driver.find_element_by_xpath(submit_button).click()

time.sleep(2)

html_source = driver.page_source


#driver.get(os.getcwd() +"\\test.html")


#soup_file=driver.page_source
soup = BeautifulSoup(html_source,"html.parser")

print(soup.find(id='validationResult').get_text())
#print(html_source)

#html_output = driver.page_source
#soup = BeautifulSoup(html_output)
'''text = driver.find_element_by_id(result_id).text
text2 = driver.getAttribute("")
print(text)
for tag in soup.find_all('title'):
    print(tag.text)'''

#title = soup.find("span", attrs={"id": 'validationResult'})
#print(title)

#output = soup.find_all('validationResult')
#print(output)

'''if soup.find_all("div", {"class": "incorrect"}):
    print("incorrect")'''
'''else:
    print("correct")'''

'''if soup.find('li', {'class': 'text'})'''