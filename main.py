from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


PATH = "C:\Program Files (x86)\Something\chromedriver.exe" # Path for chromedriver file
s = Service(PATH)
driver = webdriver.Chrome(service=s)

driver.get("https://www.dominos.ca/en/") # opens website

time.sleep(2) #wait for webpage to load in

delivery_Btn = driver.find_element(By.CLASS_NAME,"smart-order__cta") # finds the delivery button
delivery_Btn.click() # clicks the delivery button

time.sleep(2) #wait for webpage to load in

#here we fill in delivery info
addressType = driver.find_element(By.ID, "Address_Type_Select")
addressTypeDD = Select(addressType)
addressTypeDD.select_by_value("House") #selects house from the form options

street = driver.find_element(By.ID, "Street")
street.send_keys("") #sends street address

city = driver.find_element(By.ID, "City")
city.send_keys("") #sends city

province = driver.find_element(By.ID, "Region")
provinceDD = Select(province)
provinceDD.select_by_value("") #selects Province from form options

postalCode = driver.find_element(By.ID, "Postal_Code")
postalCode.send_keys("")

#continue for delivery
continue_for_delivery_btn = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div/div[2]/form/div/div[4]/button")
continue_for_delivery_btn.click()

time.sleep(2) #wait for webpage to load in

#order pizza! I like Extra Cheese pizza so I'll order that
originalPizza = driver.find_element(By.XPATH, '//*[@id="entreesPage"]/div[2]/div[7]/ul/li[1]/a')
originalPizza.click() #going to Domino's Pizza Builder

time.sleep(2)
addOrder = driver.find_element(By.XPATH, '//*[@id="pizzaSummaryInColumn"]/div[1]/div[2]/div[2]/button')
addOrder.click() #adding a large (14'') pizza with original hand tossed crust

time.sleep(2)
xtraCheese = driver.find_element(By.XPATH, '//*[@id="stepUpsell"]/div/button[2]')
xtraCheese.click() #adding extra cheese to pizza

time.sleep(2)
checkOut = driver.find_element(By.XPATH, '//*[@id="js-myOrderPage"]/a')
checkOut.click() #going to check out menu

time.sleep(2)
noThanks = driver.find_element(By.XPATH,'//*[@id="genericOverlay"]/section/div/div[2]/div/a')
noThanks.click() #saying no thanks to adding extra sides

time.sleep(10)
continueCheckout = driver.find_element(By.XPATH, '//*[@id="js-checkoutColumns"]/aside/div[3]/div[1]/a')
continueCheckout.click() #continue heading to checkout menu

#inserting information into billing form
firstName = driver.find_element(By.ID, 'First_Name')
firstName.send_keys("Mark")

lastName = driver.find_element(By.ID, 'Last_Name')
lastName.send_keys("Wong")

email = driver.find_element(By.ID, 'Email')
email.send_keys("markusamiwong@gmail.com")

#payment option to credit card at the door and then order!
payment = driver.find_element(By.XPATH, '//*[@id="payment-form"]/div[5]/div[1]/div[2]/div/div[2]/div[22]/div[1]/input')
payment.click()

placeOrder = driver.find_element(By.XPATH, '//*[@id="payment-form"]/div[6]/div/div/div[5]/button')
placeOrder.click()


#driver.quit()