from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from Configurations import Config
class HomePage:

    #-----Locators------
    Locator_NewPost_Xpath = "//div[@class='SpTCHb']//span[@class='MIJMVe'][normalize-space()='New Post']"
    Locator_PostPublished_Xpath = "//c-wiz[@class='zQTmif SSPGKf eejsDc qWnhY O3LMFb haXJ6e']//a[@class='azat BJi0D']"
    Locator_CommentSection_CSS = "div[class='SpTCHb'] span[aria-label='Comments'] div[class='kurlme DQGx6d']"
    Locator_PostMoverArea_Xpath = "(//a[@class='azat BJi0D'])[1]"
    Locator_PostDeleteIcon_Xpath = "(//span[@class='DPvwYc'][contains(text(),'')])[2]"
    Locator_PostDeleteButton_Xpath = "//*[@id='yDmH0d']/div[4]/div/div[2]/div[3]/div[2]/span/span"
    Locator_PostList_Xpath = "(//div[@class='gNK4lf'])"
    Locator_Img_no_Post_CSS = "img[aria-label='Empty post list image']"
    Locator_List_NumberElement = "div[class='MocG8c iRqe nj0FMe F8KQq LMgvRb KKjvXb'] span[class='vRMGwf oJeWuf']"
    #-----Variable_Values-----
    home_page_title = "Blogger: Posts"
    current_pos_num = 0
    post_list = []

    #-----Methods------

    def __init__(self, driver):
        self.driver = driver

    """Home Page Validation
    Login page validation with Title 
    """
    def home_page_check(self):
        sleep(3)
        current_title = self.driver.title
        if current_title == self.home_page_title:
            assert True
        else:
            Config.take_screenshot(self)
            assert False

    """Click "New Post" button for creating new post     
    """
    def clickNewPost(self):
        sleep(3)
        self.driver.find_element(By.XPATH,self.Locator_NewPost_Xpath).click()

    """Click on Published post to open edit page
    """
    def clickPostPublished(self):
        sleep(3)
        self.driver.find_element(By.XPATH,self.Locator_PostPublished_Xpath).click()

    """Click "Comment" button to open Comment Page    
    """
    def clickCommentSection(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,self.Locator_CommentSection_CSS).click()

    """Click "delete icon" on the post    
    """
    def clickPostDeleteIcon(self):
        sleep(3)
        action = ActionChains(self.driver)
        delete_item_list = self.driver.find_element(By.XPATH, self.Locator_PostMoverArea_Xpath)
        action.move_to_element(delete_item_list).perform()
        sleep(3)
        self.driver.find_element(By.XPATH,self.Locator_PostDeleteIcon_Xpath).click()

    """Click "Delete" button to confirm deletion after clicking "delete icon"    
       """
    def clickPostDeleteButton(self):
        sleep(3)
        self.driver.find_element(By.XPATH, self.Locator_PostDeleteButton_Xpath).click()
    """Count post number
    """
    def post_count(self):
        sleep(2)

        self.post_list = self.driver.find_elements(By.XPATH, self.Locator_PostList_Xpath)
        if not self.post_list:
            self.current_pos_num = 0
        else:
            self.current_pos_num = len(self.post_list)
        return self.current_pos_num
    """Count number of post with different elements
    """
    def PostNumber(self): #Kullanılacak!!!!
        postnum = self.driver.find_element(By.CSS_SELECTOR, self.Locator_List_NumberElement).text
        print(postnum)
        return postnum






