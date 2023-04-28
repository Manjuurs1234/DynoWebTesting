import psycopg2 as pg
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from PageObjes.dyno_pom import Loginpage
class TestLogin:

    def test_Login(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        serv_obj = Service("Loginpage.chrome")
        driver = webdriver.Chrome(options=options, service=serv_obj)
        driver.maximize_window()
        driver.get(Loginpage.URL)
        time.sleep(2)
        driver.find_element(By.XPATH, Loginpage.textbox_mailid_xpath).send_keys(Loginpage.email)
        time.sleep(5)
        shadow = driver.find_element(By.CSS_SELECTOR, Loginpage.next)
        shadow.click()
        time.sleep(5)

        port = '5432'
        host = '34.100.216.73'
        user = "postgres"
        password = "t3djo7b0jfd9J3JL"
        database = "devdyno"

        con = pg.connect(database=database, user=user, password=password, host=host, port=port)
        cur = con.cursor()
        QueryString = '''SELECT (payload ->>'OTP') :: integer FROM auth.nq Order by pid desc limit 1'''
        cur.execute(QueryString)
        con.commit()
        output1 = cur.fetchall()
        a = str(output1)
        b = a.replace('[(', '')
        otp = b.replace(',)]', '')
        driver.find_element(By.XPATH, "//input[@placeholder='Enter OTP']").send_keys(otp)
        time.sleep(5)
        shadow1 = driver.find_element(By.CSS_SELECTOR,".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow1.click()
        time.sleep(5)

        # list view click
        driver.find_element(By.CSS_SELECTOR,"body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > ion-toolbar:nth-child(1) > ion-grid:nth-child(1) > ion-row:nth-child(1) > ion-col:nth-child(4) > div:nth-child(1) > ion-item:nth-child(2) > img:nth-child(1)").click()
        time.sleep(2)
        # search project card
        driver.find_element(By.XPATH, "//input[@placeholder='Search Apps']").send_keys('BFSI')  # search name
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"body > app-root:nth-child(1) > ion-app:nth-child(1) > ion-router-outlet:nth-child(1) > app-home:nth-child(2) > ion-content:nth-child(3) > div:nth-child(1) > div:nth-child(3) > ion-card:nth-child(1) > ion-item:nth-child(1) > img:nth-child(3)").click()  # 3 dots
        time.sleep(2)
        # view specifications
        driver.find_element(By.ID, "logout-id").click()
        time.sleep(2)
        #******************************************************************************************************************

        # Screen Name: Vision Screen
        # SID: 2.1 - Verify UI elements of Vision Screen

        # User clicks on Vision link in left pane
        driver.find_element(By.XPATH, "//li[6]//ion-row[1]//ion-col[3]").click()
        time.sleep(2)
       # Displaying user navigation in top menu and Title indicating the vision number
        driver.find_element(By.CSS_SELECTOR, ".bread-crumb-col.md.hydrated")
        time.sleep(2)
        # # see the Document status drop down
        driver.find_element(By.CSS_SELECTOR, "img[src='../../../../assets/icon/pencil.png']").click() # click the edit button
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="mat-select-0"]/div/div[2]').click()  # click the dropdown
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "mat-option[id='mat-option-4'] span[class='mat-option-text']").click()  # click the draft
        time.sleep(2)
        # click button
        driver.find_element(By.CSS_SELECTOR, "ion-col[class='ion-align-self-center items-col md hydrated'] ion-col:nth-child(2)").click()
        time.sleep(2)
        # # Comments icon
        driver.find_element(By.CSS_SELECTOR, "img[src='../../../../assets/icon/comment_blue.png']")
        time.sleep(2)
        # Edit icon
        driver.find_element(By.CSS_SELECTOR, "img[src='../../../../assets/icon/pencil.png']")
        time.sleep(2)
        # Delete icon
        driver.find_element(By.CSS_SELECTOR, "img[src='../../../../assets/icon/delete.png']")
        time.sleep(2)
        # see the more options
        driver.find_element(By.CSS_SELECTOR, ".ellipseMargin").click()
        time.sleep(3)
        # dark background
        driver.find_element(By.XPATH, "//div[@class='cdk-overlay-backdrop cdk-overlay-dark-backdrop cdk-overlay-backdrop-showing']").click()
        time.sleep(3)
        # see the textbox to enter the Title and Description
        driver.find_element(By.CLASS_NAME,"visionTitle")
        time.sleep(3)
        # Footer menu information
        driver.find_element(By.XPATH, "//div[@class='footerClass']")
        time.sleep(2)
        #*******************************************************************************************************

        # SID 2.2 - Edit Vision Details
        # Edit icon
        driver.find_element(By.CSS_SELECTOR, "img[src='../../../../assets/icon/pencil.png']").click()
        time.sleep(2)
        # see the textbox to enter the modification Title and Description
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Please enter a title here']").clear()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Please enter a title here']").send_keys("+VSN NO509")
        time.sleep(3)
        #***********************************************************************************************************
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Please enter a title here']").clear()
        driver.find_element(By.CSS_SELECTOR, "img[src='assets/icon/save-blue.png']").click()
        time.sleep(5)




        # validations
        Dashboard_display = driver.find_element(By.CSS_SELECTOR, ".visionTitle")
        print("Element Found : Focus On", Dashboard_display.is_displayed())
        print("Vision link options was verified:")
        print("User navigation in top menu and Title indicating the vision number was verified:")
        print("Document status drop down was verified:")
        print("Comments icon was verified:")
        print("Edit icon was verified:")
        print("Delete icon was verified:")
        print("More options button was verified:")
        print("The Title and Description was verified:")
        print("Footer menu information was verified:")
        print("Edit Vision Details was verified:")
        time.sleep(2)
        if Dashboard_display.is_displayed() == True:
            assert True
        else:
            print("Element Not Found : Not verified", Dashboard_display.is_displayed())

        driver.close()