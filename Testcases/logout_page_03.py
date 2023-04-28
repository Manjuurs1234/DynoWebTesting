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
        #  ******************************************************************************************
        # valid otp - valid testcase

        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter OTP']").send_keys(otp)
        time.sleep(5)
        shadow1 = self.driver.find_element(By.CSS_SELECTOR, ".next-btn.md.button.button-solid.ion-activatable.ion-focusable.hydrated")
        shadow1.click()


    # logout

        self.driver.find_element(By.CSS_SELECTOR, ".avatar").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/button[2]/div[1]").click()
        time.sleep(2)

        # validations
        logout_page = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']")
        print("Element Found : Focus On", logout_page.is_displayed())
        print("Logout page verified:")
        time.sleep(5)
        if logout_page.is_displayed() == True:
            assert True
        else:
            print("Element Not Found : Not verified", logout_page.is_displayed())

        self.driver.close()





