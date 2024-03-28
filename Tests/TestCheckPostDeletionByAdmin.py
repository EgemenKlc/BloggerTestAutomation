import pytest

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Configurations import Config,BaseFunctions
"""Test Case Steps:
    1. open browser and visit Blogger.com
    2. check the login page and press the login button
    3. To log in, enter your email address and password, then log in.
    4. check the home page after login
    5 - Click post delete icon
    6 - Click delete confirm button
    7 - Wait until home page refresh 
    8 - Close browser
"""

class TestCheckPostDeletionByAdmin:
    @pytest.mark.order(8)
    def test_check_post_deletion_by_admin(self):
        # Setup logger with class name
        self.logger = BaseFunctions.loggerInit(self, self.__class__.__name__)
        self.logger.info("1. Open Browser and visit blogger.com")

        BaseFunctions.browser_setup(self, Config.admin_blog_Url)

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
        self.logger.info("5 - Click post delete icon")
        self.hp.clickPostDeleteIcon()
        self.logger.info(" 6 - Click delete confirm button")
        self.hp.clickPostDeleteButton()
        self.logger.info(" 7 - Wait until home page refresh ")
        self.driver.refresh()
        self.logger.info("Post deleted Successfully ")
        self.tearDown()
        self.logger.info("8 - Browser closed ")

    def tearDown(self):
        self.driver.close()

        #----- Check the Post is deleted or not By GuestPostCheck ------


