

from selenium.webdriver.common.by import By
from time import sleep
from Configurations import Config

class GuestPage:


    #-----Locators-----
    Locator_NoPostMessage_CSS = "div[class='no-posts-message']"
    Locator_PostFeatured_ID = "FeaturedPost1"
    Locator_PostComment_CSS = "span[class='num_comments']"
    Locator_iframe_Comment_NAME = "comment-editor"
    Locator_GoogleSignIn_CSS ="div[aria-label='Sign in with Google'] span[class='RveJvd snByac']"
    Locator_CommentTextArea_CSS = "textarea[aria-label='Enter Comment']"
    Locator_PublishCommentButton_CSS = "div[aria-label='Publish'] span[class='RveJvd snByac']"
    Locator_CommentList_CSS = "ol[id='top-ra']"
    Locator_CommentList_Xpath = "//*[@id='top-ra']"


    #-----Variable_Value-----
    CommentText = "Hey You I am a Guest!! :)"
    guest_page_title = "BloggerAutomation"
    global_total_comment_number = 0


    #-----Methods-----

    def __init__(self,driver):
        self.driver = driver

    #----- Page Check-----
    def guestPageCheck(self):
        sleep(3)
        current_title = self.driver.title
        if current_title == self.guest_page_title:
            status = True
        else:
            self.driver.save_screenshot(
                "C:\\Users\\10132817\\PycharmProjects\\BloggerAutomation\\Error_ScreenShots\\GuestPageTitle_error_screenshot.png")
            status = False
        return status

    def PostCheck(self):

        sleep(3)
        elements = self.driver.find_elements(By.ID,self.Locator_PostFeatured_ID)
        # Eğer liste boşsa, element yoktur
        if not elements:
            self.driver.save_screenshot("C:\\Users\\10132817\\PycharmProjects\\BloggerAutomation\\Error_ScreenShots\\PostNotFound_error_screenshot.png")
            assert False
        else:
            assert True


    def CommentCheck(self):
        Comment_Text = self.driver.find_element(By.CSS_SELECTOR,self.Locator_PostComment_CSS).text
        if "Post" in Comment_Text:
            print("yorum yok")
            assert False
        else:
            text_parts = Comment_Text.split(" comment")
            Config.total_comment_number = text_parts[0]
            print(Config.total_comment_number)
            self.driver.save_screenshot("C:\\Users\\10132817\\PycharmProjects\\BloggerAutomation\\Error_ScreenShots\\CommentNotFound_error_screenshot.png")
            assert True
    def CommentCheckAfterDeletion(self):
        Comment_Text = self.driver.find_element(By.CSS_SELECTOR, self.Locator_PostComment_CSS).text
        if "Post" in Comment_Text:
            print("yorum yok")
            assert True
        else:
            text_parts = Comment_Text.split(" comment")
            Config.total_comment_number = text_parts[0]
            print(Config.total_comment_number)
            self.driver.save_screenshot(
                "C:\\Users\\10132817\\PycharmProjects\\BloggerAutomation\\Error_ScreenShots\\CommentDeletion_error_screenshot.png")
            assert False
        '''
        if int(Config.total_comment_number) - 1 == 1:
            print(Config.total_comment_number)
            assert True
        else:
            assert False
        '''

    def clickPostComment(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,self.Locator_PostComment_CSS).click()

    def SwitchDefaultFrame(self):
        self.driver.switch_to.default_content()

    def SwitchFrame_to_CommentSign(self):
        sleep(3)
        self.driver.switch_to.frame(self.driver.find_element(By.NAME, self.Locator_iframe_Comment_NAME ))


    def click_GoogleSignIn_ForComment(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, self.Locator_GoogleSignIn_CSS).click()

    def setCommentText(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, self.Locator_CommentTextArea_CSS).send_keys(self.CommentText)

    def clickPublishCommentButton(self):
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, self.Locator_PublishCommentButton_CSS).click()
        sleep(2)

    def postCommentCheck(self):
        command_list = self.driver.find_elements(By.XPATH, self.Locator_CommentList_Xpath)
        if not command_list:
            assert False
        else:
            assert True

            #id yi globale al


'''
    comments = self.driver.find_elements(By.XPATH, self.viewComments_xpath)

    for comment in comments:
        current_comment_id = comment.get_attribute("id")
        print(current_comment_id)
        if current_comment_id == self.comment_id:
            return False

    return True
    
    '''


