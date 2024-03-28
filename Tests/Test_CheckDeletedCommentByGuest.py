import pytest

from Pages.GuestPage import GuestPage
from Configurations import Config,BaseFunctions

"""

1 - Open browser and visit https://onlinebloggertest.blogspot.com/
2 - Check the post visibility
3 - Check comment is deleted
4 - Close browser

"""
class TestCheckDeletedCommentByGuest:
    @pytest.mark.order(7)
    def test_check_deleted_comment_by_guest(self):
        # Setup logger with class name
        self.logger = BaseFunctions.loggerInit(self, self.__class__.__name__)

        self.logger.info("1. Open Browser and visit https://onlinebloggertest.blogspot.com/")
        BaseFunctions.browser_setup(self, Config.guest_blog_Url)
        self.logger.info("Browser opened successfully!")
        self.gp = GuestPage(self.driver)
        self.logger.info("2 - Check the post visibility")
        self.gp.PostCheck()
        self.logger.info("Post is visible")
        self.logger.info("3 - Check comment is deleted")
        self.gp.CommentCheckAfterDeletion()
        self.logger.info("Comment is deleted successfully")

        self.tearDown()
        self.logger.info("4. browser Closed")

    def tearDown(self):
        self.driver.close()

