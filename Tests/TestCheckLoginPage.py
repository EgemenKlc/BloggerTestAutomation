import pytest
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Configurations import Config, BaseFunctions


""" Test Case Steps:
    1. open browser and visit Blogger.com
    2. check the login page and press the login button
    3. To log in, enter your email address and password, then log in.
    4. check the home page after login
    5. close browser 
"""


class TestCheckLoginPage:
    @pytest.mark.order(1)
    def test_check_login_page(self):
        # Setup logger with class name
        self.logger = BaseFunctions.loggerInit(self, self.__class__.__name__)
        self.logger.info("1. Open Browser and visit blogger.com")

        self.driver = BaseFunctions.browser_setup(self, Config.admin_blog_Url)

        self.logger.info("Browser opened successfully!")

        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)

        self.logger.info("2.Check the login page and press the login button")
        self.lp.loginPageCheck()
        self.lp.clickSignIn()

        self.logger.info("login page is ture and Signin clicked")
        self.logger.info("3.Enter your email address and password, then log in.")
        self.lp.LoginInit(self.lp.user_Mail, self.lp.user_Password)
        self.logger.info("User logged in successfully!")
        self.logger.info("4. check the home page after login")

        self.hp.home_page_check()
        self.logger.info("home page is true")

        self.tearDown()
        self.logger.info("5. browser Closed")

    def tearDown(self):
        self.driver.close()


































