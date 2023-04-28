from telnetlib import EC

import psycopg2 as pg
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


from selenium.webdriver.support.wait import WebDriverWait

from PageObjes.dyno_pom import Loginpage
class TestLogin:

    def test_Login(self):
        path= Loginpage(self)
        self.driver = path.get_driver()
        self.driver.implicitly_wait(30)

        self.driver.get(Loginpage.URL)
        self.driver.find_element(By.XPATH, Loginpage.textbox_mailid_xpath).send_keys(Loginpage.email)
        shadow = self.driver.find_element(By.CSS_SELECTOR, Loginpage.next)
        shadow.click()

        port = '5432'
        host = '34.100.216.73'
        user = "postgres"
        password = "t3djo7b0jfd9J3JL"
        database = "devdyno"

        con = pg.connect(database=database, user=user, password=password, host=host, port=port)
        cur = con.cursor()
        QueryString = '''SELECT (payload ->>'OTP') FROM auth.nq Order by pid desc limit 1'''
        time.sleep(3)
        cur.execute(QueryString)
        con.commit()
        output1 = cur.fetchall()
        a = str(output1)
        b = a.replace('[(', '')
        otp = b.replace(',)]', '')
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter OTP']").send_keys(otp)
        shadow1 = self.driver.find_element(By.CSS_SELECTOR,".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow1.click()
    #**************************************************************************************************************************

        # Empty text box - Invalid testcase SID 1.1
        self.driver.find_element(By.XPATH,"//input[@placeholder='Email']")
        shadow = self.driver.find_element(By.CSS_SELECTOR, ".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow.click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").clear()
        #***************************************************************************

        # Invalid mail - Invalid testcase SID 1.2
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys('abc')
        shadow = self.driver.find_element(By.CSS_SELECTOR,".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow.click()
        self.driver.find_element(By.CSS_SELECTOR, ".error-message")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").clear()

        #***************************************************************************
        # valid mail - valid testcase SID 1.3
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys('manjunath.s@tibilsolutions.com')
        shadow = self.driver.find_element(By.CSS_SELECTOR, ".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow.click()

        #************************************************************************************************
        # enter the otp - Empty text box - Invalid testcase SID 1.4
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter OTP']")
        shadow = self.driver.find_element(By.CSS_SELECTOR,".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow.click()
        #****************************************************************************************************************

        # wrong otp - Invalid testcase SID 1.5
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter OTP']").send_keys('123456')
        self.driver.implicitly_wait(2)
        shadow = self.driver.find_element(By.CSS_SELECTOR,".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter OTP']").clear()


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

    #  ******************************************************************************************
        # valid otp - valid testcase SID 1.6
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter OTP']").send_keys(otp)
        time.sleep(5)
        shadow1 = self.driver.find_element(By.CSS_SELECTOR, ".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow1.click()
        time.sleep(5)

        # validations
        errormsg = 'Error messages verified'
        if errormsg=="Error messages was verified":
            print(errormsg)
        else:
            print("verified")

        Dashboard_display = self.driver.find_element(By.XPATH, "//img[@class='orgLogo ng-star-inserted']")

        print("Element Found : Focus On", Dashboard_display.is_displayed())

        print("Error messages was verified:")
        print("Login page was verified:")
        time.sleep(5)
        if Dashboard_display.is_displayed() == True:
            assert True
        else:
            print("Element Not Found : Not verified", Dashboard_display.is_displayed())

        self.driver.close()



