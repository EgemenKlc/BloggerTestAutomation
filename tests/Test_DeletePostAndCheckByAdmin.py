import pytest

from POMs.HomePageObject import HomePage
from POMs.LoginPageObject import LoginPage
from Configurations import Config


class Test_PostDeleteAndCheck:
    @pytest.mark.order(8)
    def test_postDeleteAndCheck(self,setup):

        self.driver = setup
        self.driver.get(Config.admin_blog_Url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)

        # ----Login Process-----
        self.lp.clickSignIn()
        self.lp.setUserMail(self.lp.user_Mail)
        self.lp.clickMailNext()
        self.lp.setPassword(self.lp.user_Password)
        self.lp.clickPassNext()
        #-----Home Page Post Deletion------
        #
        self.hp.clickPostDeleteIcon()
        self.hp.clickPostDeleteButton()


        self.driver.close()
        #----- Check the Post is deleted or not By GuestPostCheck ------


