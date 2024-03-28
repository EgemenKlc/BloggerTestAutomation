import pytest

from Pages.GuestPage import GuestPage
from Configurations import Config, BaseFunctions

"""
1 - Open browser and visit https://onlinebloggertest.blogspot.com/
2 - Wait until page loading 
3 - Check post visibility
4 - Close browser
"""
class TestCheckPostByGuest:
    @pytest.mark.order(4)
    def test_check_post_by_guest(self):
        # Setup logger with class name
        self.logger = BaseFunctions.loggerInit(self, self.__class__.__name__)

        self.logger.info("1. Open Browser and visit https://onlinebloggertest.blogspot.com/")
        BaseFunctions.browser_setup(self, Config.guest_blog_Url)
        self.logger.info("Browser opened successfully!")

        self.gp = GuestPage(self.driver)

        self.logger.info("2 - Wait until page loading ")
        self.gp.guestPageCheck()
        self.logger.info("Guest page is True ")
        self.logger.info("3 - Check post visibility ")
        self.gp.PostCheck()
        self.logger.info("post is visible ")
        self.tearDown()
        self.logger.info("4. browser Closed")

    def tearDown(self):
        self.driver.close()