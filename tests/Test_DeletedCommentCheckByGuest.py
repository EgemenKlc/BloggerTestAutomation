import pytest

from POMs.GuestPageObject import GuestPage
from Configurations import Config


class Test_GuestDeletedCommentValidation:
    @pytest.mark.order(7)
    def test_GuestCommentCheck(self,setup):

        self.driver = setup
        self.driver.get(Config.guest_blog_Url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

        # ----- guest page Check if post is visible------
        self.gp = GuestPage(self.driver)
        self.gp.PostCheck()
        self.gp.CommentCheckAfterDeletion()

        self.driver.close()

