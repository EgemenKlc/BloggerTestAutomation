from selenium.webdriver.common.by import By
from time import sleep
from Pages.GuestPage import GuestPage
from selenium.webdriver.common.action_chains import ActionChains
from Configurations import Config


class CommentPage:
    gp = GuestPage
    #-----Locators------
    Locator_CommentTexts_CSS = "div[class='Opvl3b']"
    Locator_CommentTexts_XPath = "//div[normalize-space()='Hey You I am a Guest!! :)']"
    Locator_CommentDeleteIcon_Xpath = "//c-wiz[@class='zQTmif SSPGKf eejsDc qWnhY O3LMFb haXJ6e']//div[@role='list']//div[1]//span[1]//div[1]//div[1]//div[4]//div[3]//span[1]//span[1]//span[1]"
    Locator_CommentDeleteButton_Xpath = "//*[@id='yDmH0d']/div[4]/div/div[2]/div[2]/div[2]"
    Locator_CommentListItems_Xpath = "(//div[@class='opmHNc'])[1]"
    Locator_CommentListItems_CSS = "div[role='list'] div:nth-child(1) span:nth-child(1) div:nth-child(1) div:nth-child(1) div:nth-child(4)"
    Locator_CommentListItems_CSS2 = "div[class='LgQiCc vOSR6b']"
    #-------Variables------
    comment_page_title = "Blogger: Comments"

    #-----Methods------
    def __init__(self, driver):
        self.driver = driver

    """Comment Page Validation
    Comment page validation with Title 
    """
    def commentPageCheck(self):
        sleep(3)
        current_title = self.driver.title
        if current_title == self.comment_page_title:
            status = True
        else:
            self.driver.save_screenshot(
                "C:\\Users\\10132817\\PycharmProjects\\BloggerAutomation\\Error_ScreenShots\\CommentPageTitle_error_screenshot.png")
            status = False
        return status

    """Get the text in the comment and check if it is the same as the text written for the comment"""
    def GetCommentTexts(self):
        sleep(3)
        element = self.driver.find_element(By.XPATH,self.Locator_CommentTexts_XPath)
        print(element.text)
        print(self.gp.CommentText)
        if element.text == self.gp.CommentText:
            assert True
        else:
            assert False

    """Click on the delete icon of the comment on the comment page  """
    def clickDeleteCommentIcon(self):
        sleep(2)
        action = ActionChains(self.driver)
        delete_item_list = self.driver.find_element(By.XPATH,self.Locator_CommentListItems_Xpath)
        action.move_to_element(delete_item_list).perform()
        sleep(3)
        self.driver.find_element(By.XPATH,self.Locator_CommentDeleteIcon_Xpath).click()

    """Click "Delete" button to confirm deletion after clicking "delete icon" of the comment    
    """
    def clickDeleteButton(self):
        sleep(3)
        self.driver.find_element(By.XPATH,self.Locator_CommentDeleteButton_Xpath).click()
        sleep(2)

    """Get the number of comments in  the comment page"""
    def commentNumber(self): #Kullanılacak!!!!
        
        comment_list = self.driver.find_elements(By.CSS_SELECTOR, self.Locator_CommentListItems_CSS2)
        if not comment_list:
            comment_num = 0
        else:
            comment_num = len(comment_list)
            #Config.total_comment_number = len(comment_list)

        return comment_num

    """Get the number of comments and assign them to a global variable"""
    '''
    def commentNumberGlobal(self):
        comment_list = self.driver.find_elements(By.CSS_SELECTOR, self.Locator_CommentListItems_CSS2)
        if not comment_list:
            Config.total_comment_number = 0
        else:
            Config.total_comment_number = len(comment_list)
            print(Config.total_comment_number)
            '''








