import time

from PageObject.LoginPage import Loginpage
from utilities.readconfig import Readconfig
from utilities.customlogger import Loggen
from PageObject.searchcustomer import Searchcustomer
from PageObject.addcustomerpage import AddCustomer

class Test_004_Searchcustomer:
    baseURL = Readconfig.getapplicationurl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    logger = Loggen.logs()

    def test_searchcustomerbyEmail(self,setup):
        self.logger.info("************* Test_004 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.ac = AddCustomer(self.driver)
        self.ac.clickOnCustomersMenu()
        self.ac.clickOnCustomersMenuItem()
        self.sc = Searchcustomer(self.driver)
        self.sc.setEmail("jacqueline.mueller@gmail.com")
        self.sc.clickSearch()
        time.sleep(5)
        status= self.sc.searchCustomerByEmail("jacqueline.mueller@gmail.com")
        if status == True:
            assert True
            self.logger.info("************* TC_4 is passed **********")
        else:
            assert False
            self.logger.info("************* TC_4 is Failed **********")

    def test_searchcustomerbyName(self,setup):
        self.logger.info("************* Test_005 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.ac = AddCustomer(self.driver)
        self.ac.clickOnCustomersMenu()
        self.ac.clickOnCustomersMenuItem()
        self.sc = Searchcustomer(self.driver)
        self.sc.setFirstName("Virat")
        self.sc.setLastName("Kohli")
        self.sc.clickSearch()
        time.sleep(5)
        status= self.sc.searchCustomerByName("Virat Kohli")
        if status == True:
            assert True
            self.logger.info("************* TC_5 is passed **********")
        else:
            assert False
            self.logger.info("************* TC_5 is Failed **********")

    def test_searchcustomerbyCompanyname(self, setup):
        self.logger.info("************* Test_006 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.ac = AddCustomer(self.driver)
        self.ac.clickOnCustomersMenu()
        self.ac.clickOnCustomersMenuItem()
        self.sc = Searchcustomer(self.driver)
        self.sc.setcompanyname("CucumberDemo")
        self.sc.clickSearch()
        time.sleep(5)
        status = self.sc.searchCustomerByCompany("CucumberDemo")
        if status == True:
            assert True
            self.logger.info("************* TC_6 is passed **********")
        else:
            assert False
            self.logger.info("************* TC_6 is Failed **********")

