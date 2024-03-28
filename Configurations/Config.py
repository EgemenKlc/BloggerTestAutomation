import logging

from selenium import webdriver
import inspect
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from enum import Enum

# -----User Credentials------
user_mail = "automationblogger5@gmail.com"
user_password = "adminTest123"
guest_mail = "guestautomated1@gmail.com"
guest_password = "Guest123"

# ---------- Url's---------------
admin_blog_Url = "https://www.blogger.com/"
guest_blog_Url = "https://bloggerautomation5.blogspot.com/"  # "https://berfintng.blogspot.com/"
image_url = "https://wallpapers.com/images/high/coolest-chilling-astronaut-505qm07utz7ea6ld.webp"


class LocatorType(str, Enum):
    CSS_SELECTOR = "CSS_SELECTOR"
    ID = "ID"
    NAME = "NAME"
    XPATH = "XPATH"
    TAG_NAME = "TAG_NAME"
    CLASS_NAME = "CLASS_NAME"
    LINK_TEXT = "LINK_TEXT"
    PARTIAL_LINK_TEXT = "PARTIAL_LINK_TEXT"
