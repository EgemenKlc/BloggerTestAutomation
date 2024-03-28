from enum import Enum

import pyperclip
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from Configurations import Config, BaseFunctions
from selenium.webdriver.support import expected_conditions as EC


class PostEditPage:
    # -----Locators------
    class locator(Enum):

        Locator_AddImage_Xpath = (Config.LocatorType.XPATH, "(//span[@class='DPvwYc sm8sCf GHpiyd'][contains(text(),'')])[1]")
        Locator_AddImage_URL_Xpath = (Config.LocatorType.XPATH,"/html[1]/body[1]/div[7]/c-wiz[2]/div[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[1]/div[3]/span[1]/div[1]/div[1]/div[1]/div[1]/div[24]/div[1]/div[1]/span[4]/div[3]/div[1]")
        Locator_AddImage_URL_Xpath1 = (Config.LocatorType.XPATH , "//div[@class='JPdR6b e5Emjc qjTEB']//span[@aria-label='By URL']")
        Locator_iframe_AddURL_Xpath = (Config.LocatorType.XPATH, "/html/body/div[11]/div[2]/div/iframe")
        Locator_PasteImageURL_Input_Xpath = (Config.LocatorType.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")
        Locator_Select_URL_Button_ID = (Config.LocatorType.ID, "picker:ap:0")
        Locator_PublishButton_CSS = (Config.LocatorType.CSS_SELECTOR, "div[aria-label='Publish'] span[class='CwaK9']")
        Locator_ConfirmButton_Xpath = (Config.LocatorType.XPATH,"(//span[@class='RveJvd snByac'][normalize-space()='Confirm'])[2]")
        Locator_iframe_TextArea_Xpath = (Config.LocatorType.XPATH,"/html[1]/body[1]/div[7]/c-wiz[1]/div[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[1]/div[3]/span[1]/div[1]/div[1]/div[2]")
        Locator_iframe_TextArea_CSS = (Config.LocatorType.CSS_SELECTOR, "iframe[class='ZW3ZFc editable']")
        Locator_TextArea_Xpath = (Config.LocatorType.XPATH, "(//body)[1]")
        Locator_UpdateButton_CSS = (Config.LocatorType.CSS_SELECTOR, "div[aria-label='Update'] div[class='A2yzVd']")
        def get_locator_type(self):
            return self.value[0]
        def get_locator_string(self):
            return self.value[1]

    # -----Variable_Values------
    ImageURL = Config.image_url
    Text = "NEW EDITTED POSTT!!!!!!"
    edit_post_page_title = "Post: Edit"

    # -----Methods-----
    def __init__(self, driver):
        self.driver = driver

    """Edit Page Validation
    Edit page validation with Title 
    """
    def edit_page_check(self):
        sleep(3)
        current_title = self.driver.title
        if current_title == self.edit_post_page_title:
            assert True
        else:
            BaseFunctions.take_screenshot(self,1)
            assert False

    """Click on add image icon on the edit page 
    """
    def clickAddImage(self):
        element = BaseFunctions.element_fail(self, self.locator.Locator_AddImage_Xpath.get_locator_type(),
                                             self.locator.Locator_AddImage_Xpath.get_locator_string())
        element.click()
        sleep(2)

    """Click the add image With url Button in the menu that opens after clicking the add image icon"""
    def clickAdd_Image_W_URL(self):

        element = BaseFunctions.element_fail(self, self.locator.Locator_AddImage_URL_Xpath1.get_locator_type(),
                                             self.locator.Locator_AddImage_URL_Xpath1.get_locator_string())

        element.click()
        #sleep(3)
        #self.driver.find_element(By.XPATH, self.locator.Locator_AddImage_URL_Xpath1.get_locator_string()).click()


    """Switch to frame to write Url in the url field """
    def SwitchFrame_to_AddURL(self):
        sleep(3)
        element = BaseFunctions.element_fail(self, self.locator.Locator_iframe_AddURL_Xpath.get_locator_type(),
                                             self.locator.Locator_iframe_AddURL_Xpath.get_locator_string())
        self.driver.switch_to.frame(element)
        #self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "/html/body/div[11]/div[2]/div/iframe"))

    """Set image url in the url field
    param str index: image url index you want to add in the post
    """
    def setImageURL_to_Input(self,URL):
        #sleep(3)
        pyperclip.copy(URL)
        #self.driver.find_element(By.XPATH,self.locator.Locator_PasteImageURL_Input_Xpath.get_locator_string()).send_keys(Keys.CONTROL, 'v')
        element = BaseFunctions.element_fail(self, self.locator.Locator_PasteImageURL_Input_Xpath.get_locator_type(),
                                             self.locator.Locator_PasteImageURL_Input_Xpath.get_locator_string())
        element.send_keys(Keys.CONTROL, 'v')

    """click select button after entering the image url"""
    def click_Select_URL_Button(self):
        sleep(3)
        #self.driver.find_element(By.ID,self.locator.Locator_Select_URL_Button_ID.get_locator_string()).click()
        element = BaseFunctions.element_fail(self, self.locator.Locator_Select_URL_Button_ID.get_locator_type(), self.locator.Locator_Select_URL_Button_ID.get_locator_string())
        element.click()


    """Switch to default frame"""
    def SwitchDefaulFrame(self):
        self.driver.switch_to.default_content()

    """Click publish button to publish post"""
    def clickPublishButton(self):
        element = BaseFunctions.element_fail(self, self.locator.Locator_PublishButton_CSS.get_locator_type(),
                                             self.locator.Locator_PublishButton_CSS.get_locator_string())

        element.click()


    """Click on Confirm button that appears after clicking the publish button """
    def clickConfirmButton(self):
        element = BaseFunctions.element_fail(self, self.locator.Locator_ConfirmButton_Xpath.get_locator_type(),
                                             self.locator.Locator_ConfirmButton_Xpath.get_locator_string())
        pre_confirm_title = self.driver.title
        element.click()
        sleep(2)
        expected_title = self.driver.title
        if pre_confirm_title == "Post: Edit" and expected_title == "Blogger: Posts":
            assert True
        else:
            BaseFunctions.take_screenshot(self, 1)
            assert False

    """Click Update button to publish the changes after editing the existing post"""
    def clickUpdateButton(self):
        element = BaseFunctions.element_fail(self, self.locator.Locator_UpdateButton_CSS.get_locator_type(),
                                             self.locator.Locator_UpdateButton_CSS.get_locator_string())
        element.click()

    """Switch to frame to write text in the text field"""
    def SwitchFrame_to_TextArea(self):
        sleep(2)
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR,
                                                             self.locator.Locator_iframe_TextArea_CSS.get_locator_string()))

    """Set text to the text area
    param str index: text index to write on the text area
    """
    def setText_to_TextArea(self, Text):
        element = BaseFunctions.element_fail(self, self.locator.Locator_TextArea_Xpath.get_locator_type(),
                                             self.locator.Locator_TextArea_Xpath.get_locator_string())
        pyperclip.copy(Text)
        element.send_keys(Keys.CONTROL, 'v')
