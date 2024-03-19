import time

from selenium import webdriver
from PageObject.LoginPage import Loginpage
from selenium.webdriver.common.by import By
from utilities.readconfig import Readconfig
from utilities.customlogger import Loggen
from utilities import XLUtils

class Test_002_Login:
    baseURL = Readconfig.getapplicationurl()
    path = ".//testdata/LoginData.xlsx"
    logger = Loggen.logs()

    def test_login_ddt(self,setup):
        self.driver = setup
        self.logger.info("*****TC_2******")
        self.driver.get(self.baseURL)
        lp=Loginpage(self.driver)
        self.max_row=XLUtils.getRowCount(self.path,'Sheet1')
        lst_status = []
        for r in range(2,self.max_row+1):
            self.username=XLUtils.readData(self.path,'Sheet1',r,1)
            self.logger.info("*****Entered the username******")
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.logger.info("*****Entered the password******")
            self.exp= XLUtils.readData(self.path, 'Sheet1', r, 3)
            lp.setUserName(self.username)
            lp.setPassword(self.password)
            lp.clickLogin()
            time.sleep(5)
            act_title=self.driver.title

            if  act_title=="Dashboard / nopCommerce administration":
                if self.exp == 'Pass':
                    self.logger.info("**** passed ****")
                    lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("**** failed ****")
                    lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title!="Dashboard / nopCommerce administration":
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
            print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False
        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ");


