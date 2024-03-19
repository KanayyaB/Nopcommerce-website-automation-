import time
from selenium.webdriver.common.by import By

class Searchcustomer:
    txtFirstName_id="SearchFirstName"
    txtLastName_id="SearchLastName"
    txtEmail_id="SearchEmail"
    txtcompany_id="SearchCompany"
    table_xpath="(//table[@id='customers-grid'])[1]"
    tableRows_xpath="(//table[@id='customers-grid'])[1]//tbody/tr"
    tableColumns_xpath="(//table[@id='customers-grid'])[1]//tbody/tr/td"
    btnSearch_id="search-customers"


    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lname)

    def setcompanyname(self, companyname):
        self.driver.find_element(By.ID, self.txtcompany_id).clear()
        self.driver.find_element(By.ID, self.txtcompany_id).send_keys(companyname)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            Emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if Emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag

    def searchCustomerByCompany(self, Company):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            Companyname = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[5]").text
            if Companyname == Company:
                flag = True
                break
        return flag