import pytest

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.CommentPage import CommentPage
from Configurations import Config,BaseFunctions
"""
    1. open browser and visit Blogger.com
    2. check the login page and press the Signin button
    3. enter your email address and password, then log in.
    4. check the home page after login
    5 - Click Comment Button
    6 - Check comment is visible and validate comment text
    7 - Click delete icon 
    8 - Click delete confirm button
    9 - Browser Closed
"""

class TestCheckCommentAndDeleteByAdmin:
    @pytest.mark.order(6)
    def test_check_comment_and_delete_by_admin(self):
        # Setup logger with class name
        self.logger = BaseFunctions.loggerInit(self, self.__class__.__name__)
        self.logger.info("1. Open Browser and visit blogger.com")

        BaseFunctions.browser_setup(self, Config.admin_blog_Url)

        self.logger.info("Browser opened successfully!")

        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.cp = CommentPage(self.driver)

        self.logger.info("2.Check the login page and press the login button")
        self.lp.loginPageCheck()
        self.lp.clickSignIn()

        self.logger.info("login page is true and Signin clicked")
        self.logger.info("3.Enter your email address and password, then log in.")
        self.lp.LoginInit(self.lp.user_Mail, self.lp.user_Password)
        self.logger.info("User logged in successfully!")
        self.logger.info("4. check the home page after login")

        self.hp.home_page_check()
        self.logger.info("home page is true")

        #-----home page go to Comment Section------
        self.logger.info("5 - Click Comment Button")
        self.hp.clickCommentSection()
        self.cp.commentPageCheck()
        self.logger.info("Comment Page is opened")
        self.logger.info("6 - Check comment if it is visible and validate comment text")
        self.cp.GetCommentTexts()
        self.logger.info("7 - Click delete icon ")
        self.cp.clickDeleteCommentIcon()
        self.logger.info("8 - Click delete confirm button")
        self.cp.clickDeleteButton()
        self.logger.info("Comment deleted successfully")
        self.tearDown()
        self.logger.info("9 - Browser Closed")

    def tearDown(self):
        self.driver.close()
