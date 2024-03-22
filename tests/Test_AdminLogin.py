import pytest
from selenium import webdriver
from POMs.LoginPageObject import LoginPage
from POMs.HomePageObject import HomePage
from Configurations import Config




class Test_Login:
    @pytest.mark.order(1)
    def test_login(self, setup):

        self.driver = setup

        self.driver.get(Config.admin_blog_Url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)

        # ----Login Process-----
        self.lp.loginPageCheck()
        self.lp.clickSignIn()
        self.lp.setUserMail(self.lp.user_Mail)
        self.lp.clickMailNext()
        self.lp.setPassword(self.lp.user_Password)
        self.lp.clickPassNext()
        self.hp.home_page_check()

        self.driver.close()


































