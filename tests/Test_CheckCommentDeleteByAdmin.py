import pytest

from POMs.HomePageObject import HomePage
from POMs.LoginPageObject import LoginPage
from POMs.CommentPageObject import CommentPage
from Configurations import Config


class Test_CheckCommentByAdmin:
    @pytest.mark.order(6)
    def test_CheckComment(self,setup):

        self.driver = setup
        self.driver.get(Config.admin_blog_Url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.cp = CommentPage(self.driver)
        # ----Login Process-----

        self.lp.clickSignIn()
        self.lp.setUserMail(self.lp.user_Mail)
        self.lp.clickMailNext()
        self.lp.setPassword(self.lp.user_Password)
        self.lp.clickPassNext()

        #-----home page go to Comment Section------

        self.hp.clickCommentSection()

        self.cp.commentPageCheck()

        self.cp.GetCommentTexts()
        self.cp.clickDeleteCommentIcon()
        self.cp.clickDeleteButton()

        self.driver.close()
