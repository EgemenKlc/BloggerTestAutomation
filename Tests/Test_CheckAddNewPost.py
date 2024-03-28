import pytest

from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.PostEditPage import PostEditPage
from Configurations import Config, BaseFunctions
""" Test Case Steps:

    1. open browser and visit Blogger.com
    2. check the login page and click Signin button
    3. enter your email address and password, then log in.
    4. check the home page after login
    5. Click New Post Button
    6. Click Insert Image icon
    7. Click By Url button
    8. Enter image url 
    9. Click select button
    10. Click publish button
    11. Click confirm button
    12. close browser 
"""
class TestCheckAddNewPost:

    @pytest.mark.order(2)
    def test_check_add_new_post(self):
        self.logger = BaseFunctions.loggerInit(self, self.__class__.__name__)


        self.logger.info("1. Open Browser and visit blogger.com")
        BaseFunctions.browser_setup(self, Config.admin_blog_Url)
        self.logger.info("Browser opened successfully!")

        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.npp = PostEditPage(self.driver)

        #----Login Process-----
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

        #post sayısını tut
        pre_post_addition = self.hp.post_count()
        all_post = self.hp.PostNumber()
        self.logger.info(f"Number of post {pre_post_addition} , {all_post}")
        self.logger.info("5. Click New Post Button")
        self.hp.clickNewPost()



        #----- New post creation and image upload and Publishing--------
        self.npp.edit_page_check()
        self.logger.info("New Post page opened Successfully")
        self.logger.info("6. Click Insert Image icon")
        self.npp.clickAddImage()
        self.logger.info("7. Click By Url button")
        self.npp.clickAdd_Image_W_URL()
        self.npp.SwitchFrame_to_AddURL()
        self.logger.info("8. Enter image url ")
        self.npp.setImageURL_to_Input(self.npp.ImageURL)
        self.logger.info("Image url entered Successfully")
        self.logger.info("9. Click select button")
        self.npp.click_Select_URL_Button()
        self.logger.info("Image added to the post Successfully")

        self.logger.info("10. Click publish button")
        self.npp.clickPublishButton()
        self.logger.info("11. Click Confirm button")
        self.npp.clickConfirmButton()
        self.driver.refresh()
        after_post_addition = self.hp.post_count()
        if after_post_addition - pre_post_addition == 1:
            self.logger.info(f"Number of post after deletion {pre_post_addition} - Before Deletion {after_post_addition}  ")
            
            assert True
        else:
            BaseFunctions.take_screenshot(self, 1)
            assert False
        self.logger.info("New Post Added Successfully")
        self.tearDown()
        self.logger.info("12. browser Closed")

    def tearDown(self):
        self.driver.close()




