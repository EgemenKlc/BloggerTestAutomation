from selenium.webdriver.common.by import By
from Configurations import Config, BaseFunctions
from enum import Enum
class LoginPage:
    class locator(Enum):
        #-----Locators-----
        Locator_SignIn_CSS = (Config.LocatorType.CSS_SELECTOR, "a[class='sign-in ga-header-sign-in'] span")
        #Locator_SignIn_CSS1 = (By.CSS_SELECTOR, "a[class='sign-in ga-header-sign-in'] span")
        Locator_UserMail_ID = (Config.LocatorType.ID, "identifierId")
        Locator_UserPassword_Name = (Config.LocatorType.NAME, "Passwd")
        Locator_User_Next_Button_ID = (Config.LocatorType.ID, "identifierNext")
        Locator_Password_Next_Button_ID = (Config.LocatorType.ID, "passwordNext")
        def get_locator_type(self):
            return self.value[0]
        def get_locator_string(self):
            return self.value[1]

    #-----Variable_Values----
    user_Mail = Config.user_mail
    user_Password = Config.user_password
    guest_Mail = Config.guest_mail
    guest_password = Config.guest_password
    login_page_title = "Blogger.com - Create a unique and beautiful blog easily."
    login_guest_page_title = "BloggerAutomation"
    #-----Methods-----

    def __init__(self, driver):
        self.driver = driver

    """Login with google by User information
    param str index: User credential indexes you want to Login with
    """
    def LoginInit(self, mail, password):
        self.setUserMail(mail)
        self.clickMailNext()
        self.setPassword(password)
        self.clickPassNext()

    """Login Page Validation
    Login page validation with Title 
    """
    def loginPageCheck(self):
        current_title = self.driver.title
        if current_title == self.login_page_title:
            assert True
        else:
            BaseFunctions.take_screenshot(self, 1)
            assert False

    """Login Guest Page Validation
    Login Guest page validation with Title 
    """
    def loginGuestPageCheck(self):
        current_title = self.driver.title
        if current_title == self.login_guest_page_title:
            status = True
        else:
            BaseFunctions.take_screenshot(self, 1)
            status = False
        return status

    """Set User Mail
    param str index: User mail index you want to login with 
    """
    def setUserMail(self,mail):
        mail_input = BaseFunctions.element_fail(self, self.locator.Locator_UserMail_ID.get_locator_type(), self.locator.Locator_UserMail_ID.get_locator_string())
        mail_input.clear()
        mail_input.send_keys(mail)

    """Set User Password
    param str index: User password index you want to login with 
    """
    def setPassword(self,Password):
        password_input = BaseFunctions.element_fail(self, self.locator.Locator_UserPassword_Name.get_locator_type(),self.locator.Locator_UserPassword_Name.get_locator_string())
        #password_input = self.driver.find_element(By.NAME,self.locator.Locator_UserPassword_Name.get_locator_string())
        password_input.clear()
        password_input.send_keys(Password)

    """Click Signin button for login on blogger.com      
    """
    def clickSignIn(self):

        Signin_button = BaseFunctions.element_fail(self,self.locator.Locator_SignIn_CSS.get_locator_type(), self.locator.Locator_SignIn_CSS.get_locator_string())
        Signin_button.click()
        #self.driver.find_element(By.CSS_SELECTOR,self.Locator_SignIn_CSS).click()

    """Click Next button after entering the e-mail     
    """
    def clickMailNext(self):
        mail_next_button = BaseFunctions.element_fail(self, self.locator.Locator_User_Next_Button_ID.get_locator_type(),
                                                      self.locator.Locator_User_Next_Button_ID.get_locator_string())
        mail_next_button.click()
        #self.driver.find_element(By.ID,self.locator.Locator_User_Next_Button_ID.get_locator_string()).click()

    """Click Next button after entering the password     
    """
    def clickPassNext(self):
        pass_next_button = BaseFunctions.element_fail(self, self.locator.Locator_Password_Next_Button_ID.get_locator_type(),
                                               self.locator.Locator_Password_Next_Button_ID.get_locator_string())
        pass_next_button.click()
        #self.driver.find_element(By.ID, self.locator.Locator_Password_Next_Button_ID.get_locator_string()).click()




