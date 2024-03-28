import pytest

from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.PostEditPage import PostEditPage
from Configurations import Config,BaseFunctions


""" Test Case Steps:

    1. open browser and visit Blogger.com
    2. check the login page and click Signin button
    3. enter your email address and password, then log in.
    4. check the home page after login
    5. Click the post that has been published
    6. Click the page 
    7. Edit the text with "NEW EDITTED POSTT!!!!!!"
    8. Click Update button
    9. Close browser
      
"""
class TestCheckEditPostPage:

    @pytest.mark.order(3)
    def test_check_edit_post_page(self):
        self.logger = BaseFunctions.loggerInit(self, self.__class__.__name__)

        self.logger.info("1. Open Browser and visit blogger.com")
        BaseFunctions.browser_setup(self, Config.admin_blog_Url)
        self.logger.info("Browser opened successfully!")

        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.npp = PostEditPage(self.driver)

        # ----Login Process-----
        self.logger.info("2.Check the login page and press the login button")
        self.lp.loginPageCheck()
        self.lp.clickSignIn()

        self.logger.info("login page is ture and Signin clicked")
        self.logger.info("3.Enter your email address and password, then log in.")
        self.lp.LoginInit(self.lp.user_Mail, self.lp.user_Password)
        self.logger.info("User logged in successfully!")
        self.logger.info("4. check the home page after login")

        # -----Home page new post Click----
        self.hp.home_page_check()
        self.logger.info("home page is true")

        #-----Home page Published post Click----
        self.logger.info("5. Click the post that has been published")
        self.hp.clickPostPublished()

        self.npp.edit_page_check()
        self.logger.info("Edit page is true")

        #---- Post Page Post Edit------
        self.logger.info(" 6. Click the page")
        self.npp.SwitchFrame_to_TextArea()
        self.logger.info("7. Edit the text with \"NEW EDITTED POSTT!!!!!!\"")
        self.npp.setText_to_TextArea(self.npp.Text)
        self.npp.SwitchDefaulFrame()
        self.logger.info(" 8. Click Update button")
        self.npp.clickUpdateButton()
        self.logger.info(" Post edited with Text Successfully")
        self.tearDown()
        self.logger.info("9. Browser Closed")

    def tearDown(self):
        self.driver.close()