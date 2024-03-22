import pyperclip
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

from Configurations import Config
from selenium.webdriver.support import expected_conditions as EC
class PostPage:
    # -----Locators------
    Locator_AddImage_Xpath = "(//span[@class='DPvwYc sm8sCf GHpiyd'][contains(text(),'')])[1]"
    Locator_AddImage_URL_Xpath = "/html[1]/body[1]/div[7]/c-wiz[2]/div[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[1]/div[3]/span[1]/div[1]/div[1]/div[1]/div[1]/div[24]/div[1]/div[1]/span[4]/div[3]/div[1]"
    Locator_iframe_AddURL_Xpath = "/html/body/div[11]/div[2]/div/iframe"
    Locator_PasteImageURL_Input_Xpath = "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]"
    Locator_Select_URL_Button_ID = "picker:ap:0"
    Locator_PublishButton_CSS = "div[aria-label='Publish'] span[class='CwaK9']"
    Locator_ConfirmButton_Xpath = "(//span[@class='RveJvd snByac'][normalize-space()='Confirm'])[2]"
    Locator_iframe_TextArea_Xpath = "/html[1]/body[1]/div[7]/c-wiz[1]/div[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[1]/div[3]/span[1]/div[1]/div[1]/div[2]"
    Locator_iframe_TextArea_CSS = "iframe[class='ZW3ZFc editable']"
    Locator_TextArea_Xpath = "(//body)[1]"
    Locator_UpdateButton_CSS = "div[aria-label='Update'] div[class='A2yzVd']"

    # -----Variable_Values------
    ImageURL = Config.image_url
    Text = "NEW EDITTED POSTT!!!!!!"
    edit_post_page_title = "Post: Edit"

    # -----Methods-----
    def __init__(self, driver):
        self.driver = driver

    def edit_page_check(self):
        sleep(3)
        current_title = self.driver.title
        if current_title == self.edit_post_page_title:
            assert True
        else:
            self.driver.save_screenshot(
                "C:\\Users\\10132817\\PycharmProjects\\BloggerAutomation\\Error_ScreenShots\\NewEditPageTitle_error_screenshot.png")
            assert False


    def clickAddImage(self):
        sleep(3)
        self.driver.find_element(By.XPATH, self.Locator_AddImage_Xpath).click()

    def clickAdd_Image_W_URL(self):
        sleep(3)
        self.driver.find_element(By.XPATH, self.Locator_AddImage_URL_Xpath).click()

    def SwitchFrame_to_AddURL(self):
        sleep(3)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, self.Locator_iframe_AddURL_Xpath))

    def setImageURL_to_Input(self, URL):
        sleep(3)
        pyperclip.copy(URL)
        self.driver.find_element(By.XPATH, self.Locator_PasteImageURL_Input_Xpath).send_keys(Keys.CONTROL, 'v')

    def click_Select_URL_Button(self):
        sleep(5)
        self.driver.find_element(By.ID, self.Locator_Select_URL_Button_ID).click()

    def SwitchDefaulFrame(self):
        self.driver.switch_to.default_content()

    def clickPublishButton(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, self.Locator_PublishButton_CSS).click()

    def clickUpdateButton(self):

        try:
            button = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,self.Locator_UpdateButton_CSS)))
            if button.is_enabled() == True:
                print("try icinde", button.is_enabled())
                button.click()
        except Exception as e:
            print("exceptionaaaa")
            self.driver.save_screenshot(
                "C:\\Users\\10132817\\PycharmProjects\\BloggerAutomation\\Error_ScreenShots\\EditButtonNotClickable_error_screenshot.png")
            assert False




        #self.driver.find_element(By.CSS_SELECTOR, self.Locator_UpdateButton_CSS).click()

    def clickConfirmButton(self):
        sleep(3)
        pre_confirm_title = self.driver.title
        self.driver.find_element(By.XPATH, self.Locator_ConfirmButton_Xpath).click()
        sleep(2)
        expected_title = self.driver.title
        if pre_confirm_title == "Post: Edit" and expected_title == "Blogger: Posts":
            assert True
        else:
            self.driver.save_screenshot(
                "C:\\Users\\10132817\\PycharmProjects\\BloggerAutomation\\Error_ScreenShots\\PostNotAdded2_error_screenshot.png")
            assert False

    def SwitchFrame_to_TextArea(self):
        sleep(3)
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, self.Locator_iframe_TextArea_CSS))

    def setText_to_TextArea(self, Text):
        sleep(3)
        pyperclip.copy(Text)
        self.driver.find_element(By.XPATH, self.Locator_TextArea_Xpath).send_keys(Keys.CONTROL, 'v')
