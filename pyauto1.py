from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time
import openpyxl
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Specify the path to the chromedriver executable
s = Service('C:\chromedriver\chromedriver_win32\chromedriver.exe')
web = webdriver.Chrome(service=s)

# Open the login page
web.get('https://ka.unitetools.in/')
time.sleep(1)

# Find the username and password input fields and enter your credentials
username = web.find_element(By.ID, "user")
password = web.find_element(By.ID, "pwd")
username.send_keys(input("Enter username: "))
password.send_keys(input("Enter password: "))
time.sleep(1)

# Submit the login form
submit_button = web.find_element(By.ID, 'btnvalidatelogin')
submit_button.click()
time.sleep(1)

# Wait for the next page to load
web.implicitly_wait(1)  # Wait for 5 seconds (adjust as needed)

# Select an option on the next page
time.sleep(1)
option_button = web.find_element(By.ID, "v-pills-01-tab")
option_button.click()

time.sleep(1)
option_button1 = web.find_element(By.CSS_SELECTOR, "#v-pills-01 > ul > a:nth-child(1) > li")
option_button1.click()

# read excel file
dataframe = openpyxl.load_workbook('test.xlsx')
#print(dataframe)

for i in dataframe.index:
    entry = dataframe.iloc[i]

    #customer
    customer =web.find_element(By.ID,'CustomerTypeCode')
    customer.send_keys(entry['Customer Type*'])

    # membertype
    member_type =web.find_element(By.ID,'MemberTypeCode')
    member_type.send_keys(entry['Member Name*'])
    
    # adimission number
    Admission_input = web.find_element(By.ID, "AdmissionNo")
    integer_Admission =entry['Admission Number*']
    string_admission = str(integer_Admission)
    Admission_input.send_keys(string_admission)
    time.sleep(2)

    # surname
    surname_input = web.find_element(By.ID, "MemberSurName")
    surname_input.send_keys(entry['Surname*'])
    time.sleep(2)
    
    # member name
    membername_input = web.find_element(By.ID, "MemberName")
    membername_input.send_keys(entry['Member Name*'])
    time.sleep(2)

    # gender
    gender = web.find_element(By.ID,'GenderCode')
    gender.send_keys(entry['Gender*'])
    time.sleep(2)
    
    # sharebalance
    share_input = web.find_element(By.ID, "ShareBalance")
    int_share = entry['Share Balance ( )*']
    str_share = str(int_share)
    share_input.send_keys(str_share)
    time.sleep(2)

    # village
    village = web.find_element(By.ID,'VillageCode')
    village.send_keys(entry['Village*'])
    time.sleep(2)
    
    # Ledger Folio No.*
    legder_input = web.find_element(By.ID, "LedgerFolioNo")
    int_legder = entry['Ledger Folio No.*']
    str_legder = str(int_legder)
    legder_input.send_keys(str_legder)
    time.sleep(2)

    #Admission Date*
    admissiondate = web.find_element(By.ID,'DOB')
    admissiondate.send_keys(entry['Date of Birth'])
    time.sleep(2)
   



    # Age as on Admission Date
    Age_input = web.find_element(By.ID, "Age")
    int_Age = entry['Age as on Admission Date']
    str_Age = str(int_Age)
    legder_input.send_keys(str_Age)
    time.sleep(2)



    # Date of Birth
    parent_input = web.find_element(By.ID, "FatherName")
    parent_input.send_keys(entry['Father Name*'])
    time.sleep(2)


    
    # Father / Mother Name
    parent_input = web.find_element(By.ID, "FatherName")
    parent_input.send_keys(entry['Father Name*'])
    time.sleep(2)

    # Mobile No.
    mobile_input = web.find_element(By.ID, "ContactNo")
    int_mobile = entry['Mobile Number']
    str_mobile= str(int_mobile)
    mobile_input.send_keys(str_mobile)
    time.sleep(2)

    # Aadhaar Card No.
    adhar_input = web.find_element(By.ID, "ContactNo")
    int_adhar = entry['Mobile Number']
    str_adhar= str(int_adhar)
    mobile_input.send_keys(str_adhar)
    time.sleep(2)

    # Address
    Address_input = web.find_element(By.ID, "Address1")
    Address_input.send_keys(entry['Address'])
    time.sleep(2)

    
    # Marital Status 



    # Spouse Name 
    spouse_input = web.find_element(By.ID, "SpouseName")
    spouse_input.send_keys(entry['Spouse Name'])
    time.sleep(2)



    # Caste Community 


    # Farmer Type 


    # Dividend Amount(  )
    amt_input = web.find_element(By.ID, "DividentBalance")
    int_amt = entry['Dividend Amount ( )']
    str_amt= str(int_amt)
    amt_input.send_keys(str_amt)
    time.sleep(2)
 


    # Thrift Balance(  )
    thrift_input = web.find_element(By.ID, "ThriftBalance")
    int_thrift = entry['Thrift Balance(  )']
    str_thrift= str(int_thrift)
    thrift_input.send_keys(str_thrift)
    time.sleep(2)


    #  DCCB/StCB/Other bank SB A/c.
    DCCB_input = web.find_element(By.ID, "DCCBSBACNO")
    int_DCCB = entry['DCCB SB Account No.']
    str_DCCB= str(int_DCCB)
    DCCB_input.send_keys(str_DCCB)
    time.sleep(2)

    # saveform
    submit_btn = web.find_element(By.ID, "btnSave")
    web.execute_script("return arguments[0].click()", submit_btn)

    confirm_btn = web.find_element(By.ID, "btnSaveafterconfirm")
    web.execute_script("return arguments[0].click()", confirm_btn)