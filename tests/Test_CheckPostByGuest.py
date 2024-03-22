import pytest

from POMs.GuestPageObject import GuestPage
from Configurations import Config

class Test_GuestPostCheck:
    @pytest.mark.order(4)
    def test_PostCheck(self, setup):

        self.driver = setup
        self.driver.get(Config.guest_blog_Url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)


        self.gp = GuestPage(self.driver)

        self.gp.PostCheck()
        self.driver.close()
