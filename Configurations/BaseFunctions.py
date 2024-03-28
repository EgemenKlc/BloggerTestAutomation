from selenium.webdriver.chrome import webdriver
import logging
from selenium import webdriver
import inspect
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def browser_setup(self, url):
    options = webdriver.ChromeOptions()
    # Disable automatic close

    options.add_experimental_option("detach", True)
    options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"

    # Adding argument to disable the AutomationControlled flag
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Exclude the collection of enable-automation switches
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # Turn-off userAutomationExtension
    options.add_experimental_option("useAutomationExtension", False)

    self.driver = webdriver.Chrome(options=options)
    self.driver.get(url)
    self.driver.maximize_window()
    self.driver.implicitly_wait(10)

def take_screenshot(self, method=None):
    # Hata mesajının olduğu yerin ekran görüntüsünü alın
    if method is None:
        method = inspect.stack()[2].function  # Çağrıldığı methodun üstündeki methodun adını alın [x] x kadar üstteki parent method
        file_name = f"C:\\Users\\10132817\\PycharmProjects\\BloggerAutomation\\Error_ScreenShots\\Screenshoot_{method}.png"
        self.driver.save_screenshot(file_name)
    else:
        method = inspect.stack()[1].function  # Çağrıldığı methodun üstündeki methodun adını alın [x] x kadar üstteki parent method
        file_name = f"C:\\Users\\10132817\\PycharmProjects\\BloggerAutomation\\Error_ScreenShots\\Screenshoot_{method}.png"
        self.driver.save_screenshot(file_name)
    print(f"Ekran görüntüsü '{file_name}' olarak kaydedildi.")

def element_fail(self, locatorType, locator):
    try:
        # Belirli bir süre boyunca elementi ara
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((getattr(By, locatorType), locator)))
        return element

    except TimeoutException:
        take_screenshot(self)
    except NoSuchElementException:
        take_screenshot(self)

def loggerInit(self, test_class_name):
    logger = logging.getLogger(test_class_name)
    logger.setLevel(logging.INFO)
    # Dosyaya logları yazma
    file_name = f"C:\\Users\\10132817\\PycharmProjects\\BloggerAutomation\\Test_Logs\\{test_class_name}.log"
    file_handler = logging.FileHandler(file_name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
