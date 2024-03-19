from selenium import webdriver
from PageObject.LoginPage import Loginpage
from selenium.webdriver.common.by import By
from utilities.readconfig import Readconfig
from utilities.customlogger import Loggen

class Test_001_Login:
    baseURL = Readconfig.getapplicationurl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    logger = Loggen.logs()


    def test_homepagetitle(self,setup):
        self.driver = setup
        self.logger.info("*****TC_1 Verifying the Homepage title******")
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print(act_title)
        self.driver.close()
        if act_title == "Your store. Login":
            self.logger.info("*****Title is Verified and is correct******")
            assert True
        else:
            self.logger.info("*****Title is Verified and is Incorrect******")
            assert False



    def test_login(self,setup):
        self.driver = setup
        self.logger.info("*****TC_2 Verifying the Login Functionality******")
        self.driver.get(self.baseURL)
        lp=Loginpage(self.driver)

        lp.setUserName(self.username)
        self.logger.info("*****Entered the username******")
        lp.setPassword(self.password)
        self.logger.info("*****Entered the password******")
        lp.clickLogin()

        act_title=self.driver.title
        self.logger.info("*****Login is successful******")
        if act_title=="Dashboard / nopCommerce administration":
            self.logger.info("*****Title is Verified and is correct******")
            assert True
        else:
            self.logger.info("*****Title is Verified and is Incorrect******")
            assert False
        lp.clickLogout()
        self.driver.close()







