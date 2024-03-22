import pytest

from POMs.LoginPageObject import LoginPage
from POMs.HomePageObject import HomePage
from POMs.PostPageObject import PostPage
from Configurations import Config

class Test_NewPost:
    @pytest.mark.order(2)
    def test_NewPost(self,setup):

        self.driver = setup
        self.driver.get(Config.admin_blog_Url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.npp = PostPage(self.driver)

        #----Login Process-----

        self.lp.clickSignIn()
        self.lp.setUserMail(self.lp.user_Mail)
        self.lp.clickMailNext()
        self.lp.setPassword(self.lp.user_Password)
        self.lp.clickPassNext()

        #-----Home page new post Click----
        self.hp.home_page_check()
        pre_post_addition = self.hp.post_count()
        self.hp.PostNumber()

        self.hp.clickNewPost()

        #----- New post creation and image upload and Publishing--------
        self.npp.edit_page_check()
        self.npp.clickAddImage()
        self.npp.clickAdd_Image_W_URL()
        self.npp.SwitchFrame_to_AddURL()
        self.npp.setImageURL_to_Input(self.npp.ImageURL)
        self.npp.click_Select_URL_Button()
        self.npp.clickPublishButton()
        self.npp.clickConfirmButton()
        self.driver.refresh()
        after_post_addition = self.hp.post_count()
        if after_post_addition - pre_post_addition == 1:

            assert True
        else:
            self.driver.save_screenshot(
                "C:\\Users\\10132817\\PycharmProjects\\BloggerAutomation\\Error_ScreenShots\\PostNotAdded_error_screenshot.png")
            assert False
        self.driver.close()




