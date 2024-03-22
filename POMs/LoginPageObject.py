from selenium.webdriver.common.by import By
from Configurations import Config

class LoginPage:

    #-----Locators-----
    Locator_SignIn_CSS = "a[class='sign-in ga-header-sign-in'] span"
    Locator_UserMail_ID = "identifierId"
    Locator_UserPassword_Name = "Passwd"
    Locator_User_Next_Button_ID = "identifierNext"
    Locator_Password_Next_Button_ID = "passwordNext"

    #-----Variable_Values----
    user_Mail = Config.user_mail
    user_Password = Config.user_password
    guest_Mail = Config.guest_mail
    guest_password = Config.guest_password
    login_page_title = "Blogger.com - Create a unique and beautiful blog easily."
    login_guest_page_title = "BloggerAutomation"
    #-----Methods-----

    def __init__(self,driver):
        self.driver=driver

    def loginPageCheck(self):
        current_title = self.driver.title
        if current_title == self.login_page_title:
            assert True
        else:
            self.driver.save_screenshot(
                "C:\\Users\\10132817\\PycharmProjects\\BloggerAutomation\\Error_ScreenShots\\LoginPageTitle_error_screenshot.png")
            assert False


    def loginGuestPageCheck(self):
        current_title = self.driver.title
        if current_title == self.login_guest_page_title:
            status = True
        else:
            self.driver.save_screenshot(
                "C:\\Users\\10132817\\PycharmProjects\\BloggerAutomation\\Error_ScreenShots\\LoginGuestPageTitle_error_screenshot.png")
            status = False
        return status

    def setUserMail(self,Mail):
        #sleep(3)
        userMailtxt=self.driver.find_element(By.ID,self.Locator_UserMail_ID)
        userMailtxt.clear()
        userMailtxt.send_keys(Mail)

    def setPassword(self,Password):
        #sleep(3)
        passwordtxt = self.driver.find_element(By.NAME,self.Locator_UserPassword_Name)
        passwordtxt.clear()
        passwordtxt.send_keys(Password)

    def clickSignIn(self):
        #sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,self.Locator_SignIn_CSS).click()

    def clickMailNext(self):
        #sleep(3)
        self.driver.find_element(By.ID,self.Locator_User_Next_Button_ID).click()

    def clickPassNext(self):
        #sleep(3)
        self.driver.find_element(By.ID, self.Locator_Password_Next_Button_ID).click()




