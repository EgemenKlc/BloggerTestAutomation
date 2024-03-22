import pytest

from POMs.GuestPageObject import GuestPage
from POMs.LoginPageObject import LoginPage
from Configurations import Config



class Test_GuestPostComment:
    @pytest.mark.order(5)
    def test_postComment(self, setup):
        self.driver = setup
        self.driver.get(Config.guest_blog_Url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

        #----- guest page Check if post is visible------
        self.gp = GuestPage(self.driver)
        self.gp.PostCheck()
        #-------Click to comment button -------
        self.gp.clickPostComment()
        self.gp.SwitchFrame_to_CommentSign()
        self.gp.click_GoogleSignIn_ForComment()

        # ----Login Process-----
        self.lp = LoginPage(self.driver)

        self.lp.setUserMail(self.lp.guest_Mail)
        self.lp.clickMailNext()
        self.lp.setPassword(self.lp.guest_password)
        self.lp.clickPassNext()
        #------ set comment and publish after sign in ---------
        self.gp.SwitchFrame_to_CommentSign()
        self.gp.setCommentText()
        self.gp.clickPublishCommentButton()
        self.gp.postCommentCheck()
        self.driver.close()


