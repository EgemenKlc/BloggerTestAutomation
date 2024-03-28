import pytest

from Pages.GuestPage import GuestPage
from Pages.LoginPage import LoginPage
from Configurations import Config,BaseFunctions

"""Test Case Steps:
1- Open browser and visit https://onlinebloggertest.blogspot.com/
2 - Click "Post a Comment" button
3 - Click "Sign in With Google" button
4 - Enter email and Password then login
5 - Click Enter Comment textbox
6 - Enter a comment
7 - Click Publish button
8 - Check comment if it is added or not
9 - Close browser
"""


class TestCheckGuestAddComment:
    @pytest.mark.order(5)
    def test_check_guest_add_comment(self):
        # Setup logger with class name
        self.logger = BaseFunctions.loggerInit(self, self.__class__.__name__)

        self.logger.info("1. Open Browser and visit https://onlinebloggertest.blogspot.com/")
        BaseFunctions.browser_setup(self, Config.guest_blog_Url)
        self.logger.info("Browser opened successfully!")

        #----- guest page Check if post is visible------
        self.gp = GuestPage(self.driver)
        self.gp.guestPageCheck()
        self.logger.info("Guest page is True ")
        self.gp.PostCheck()
        self.logger.info("Post is visible ")
        #-------Click to comment button -------
        self.logger.info("2 - Click \"Post a Comment\" button ")
        self.gp.clickPostComment()
        self.gp.SwitchFrame_to_CommentSign()
        self.logger.info("3 - Click \"Sign in With Google\" button")
        self.gp.click_GoogleSignIn_ForComment()

        # ----Login Process-----
        self.lp = LoginPage(self.driver)
        self.logger.info("4 - Enter email and Password then login")
        self.lp.LoginInit(self.lp.guest_Mail, self.lp.guest_password)
        self.logger.info("Guest Login successfully")

        #------ set comment and publish after sign in ---------
        self.logger.info("5 - Click Enter Comment textbox")
        self.gp.SwitchFrame_to_CommentSign()
        self.logger.info("6 - Enter a comment")
        self.gp.setCommentText()
        self.logger.info("Comment entered successfully")
        self.logger.info("7 - Click Publish button")
        self.gp.clickPublishCommentButton()
        self.logger.info("8 - Check comment if it is added or not")
        self.gp.postCommentCheck()
        self.logger.info("Comment added Successfully")
        self.tearDown()
        self.logger.info("9 - Browser closed")
    def tearDown(self):
        self.driver.close()


