from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#enter the link to the website you want to automate login.
website_link="https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&gmb=exp&biz=true&flowName=GlifWebSignIn&flowEntry=SignUp"
#enter your first name
firstname="Testname"
#enter your last name
lastname="Testname"
#enter your login password
email="THEREwillBEradomTEXTsoon"
#enter your login password
password="VerySafePassword321"
#enter your login password again
password_check="VerySafePassword321"

###########################################################

#enter the element for username input field
element_for_firstname="firstName"
#enter the element for password input field
element_for_lastname="lastName"
#enter the element for submit button
element_for_email="username"
#enter the element for submit button
element_for_password="Passwd"
#enter the element for submit button
element_for_password_check="ConfirmPasswd"
#enter the element for submit button
element_for_submit="/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span"



###########################################################

browser = webdriver.Chrome()
browser.get(('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&gmb=exp&biz=true&flowName=GlifWebSignIn&flowEntry=SignUp'))

# fill in username and hit the next button

s_firstname = browser.find_element_by_id(element_for_firstname)
s_firstname.send_keys(firstname)

s_lastname = browser.find_element_by_id(element_for_lastname)
s_lastname.send_keys(lastname)

s_email = browser.find_element_by_id(element_for_email)
s_email.send_keys(email)

s_password = browser.find_element_by_name(element_for_password)
s_password.send_keys(password)

s_passwordb = browser.find_element_by_name(element_for_password_check)
s_passwordb.send_keys(password_check)

nextButton = browser.find_element_by_xpath(element_for_submit)
nextButton.click()
