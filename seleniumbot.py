import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Function for logging in
def login(driver, username, password):
    driver.find_element(By.XPATH,'//*[@id="ctl00_SidePlaceHolder2_UserName"]').send_keys(username)
    driver.find_element(By.XPATH,'//*[@id="ctl00_SidePlaceHolder2_Password"]').send_keys(password)
    driver.find_element(By.XPATH,'//*[@id="ctl00_SidePlaceHolder2_LoginButton"]').click()
    time.sleep(4)
    driver.get("Your website here")
    time.sleep(4)
    
# Use pandas to read in data from a CSV file
data = pd.read_csv("your file location here",parse_dates=[6,17,21])
#data['Date of Birth'] = pd.to_datetime(data['Date of Birth'], errors='coerce')
#data['Employ. Date'] = pd.to_datetime(data['Employ. Date'], errors='coerce')
data['Date of Birth']=data['Date of Birth'].dt.strftime('%d-%m-%Y')
data['Employ. Date']=data['Employ. Date'].dt.strftime('%d-%m-%Y')
data['Date of Exit']=data['Date of Exit'].dt.strftime('%d-%m-%Y')
#data['Skill Area'] = data['Skill Area'].str.title()
data.OtherName = data.OtherName.fillna('')


# Initialize webdriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("Your website here")

# Call the login function to log in
login(driver, "Username", "Password")



# Iterate over each row of data
for n,(i,row) in enumerate(data.iterrows()):
    
    
    
        
    # Fill in the form
    driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_AddIDNo"]').send_keys(row["National/Alien_ID_No"])
    driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_AddEmpNo"]').send_keys(row["Employment No"])
    driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_AddSName"]').send_keys(row["SurName"])
    driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_AddFName"]').send_keys(row["FirstName"])
    driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_AddOName"]').send_keys(row["OtherName"])
    driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_AddDOB"]').send_keys(row["Date of Birth"])
    driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_AddKRAPIN"]').send_keys(row["KRA PIN"])
    driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_AddTitle"]').send_keys(row["Job Title"])
    driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_AddOcc"]').send_keys(row["Occupation"])
    driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_AddNationality"]').send_keys(row["Nationality"])
    driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_AddEmpDate"]').send_keys(row["Employ. Date"])
    driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_AddExitDate"]').send_keys(row["Date of Exit"])
    


    
    gender = Select(driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_nGender_List"]'))
    gender.select_by_visible_text(row["Gender"])
    marital_status = Select(driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_nMarital_List"]'))
    marital_status.select_by_visible_text(row["Marital Status"])
    disability = Select(driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_nDisable_List"]'))
    disability.select_by_visible_text(row["Disability Type"])
    academic = Select(driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_nAcad_List"]'))
    academic.select_by_visible_text(row["Highest Academic Level"])
    certificate = Select(driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_nQual_List"]'))
    certificate.select_by_visible_text(row["Professional Qualification"])
    skill = Select(driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_nSkill_List"]'))
    skill.select_by_visible_text(row["Skill Area"])
    tos = Select(driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_nTOS_List"]'))
    tos.select_by_visible_text(row["Terms_of_Service"])
    training = Select(driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_nHETrain_List"]'))
    training.select_by_visible_text(row["Highest Training by Employer"])
    training_duration = Select(driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_nDuration_List"]'))
    training_duration.select_by_visible_text('3')
    reason_for_exit = Select(driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_nExitRsn_List"]'))
    reason_for_exit.select_by_visible_text(row["Reasons_For_Exiting_Employment"])
   



    # Submit the form
    driver.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grdStaff_ctl03_btnAdd"]').click()
    print(n,row['Employment No'])
    time.sleep(2)
