import sys
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import datetime
from selenium.webdriver.common.by import By
import moodle_locators as locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# This method solves the "DeprecateWarning" error that occurs in Selenium 4 and above.
# 1. Comment out, or remove the previous method which was: driver = webdriver.Chrome('chromedriver.exe path')
# 2. Add following code
# s = Service(executable_path='..//chromedriver.exe')
# driver = webdriver.Chrome(service=s)
options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)



def setUp():
    print(f'launch {locators.app} App')
    print('---------------~*~---------------------')

    # Make browser full screen
    driver.maximize_window()

    # Give the browser up to 30 seconds to respond
    driver.implicitly_wait(30)

    # Navigate the Moodle app website
    driver.get(locators.app_homepage_url)

    if driver.current_url == locators.app_homepage_url and driver.title == locators.app_homepage_title:
        print('browser launched!')
        print(f'{locators.app} Url is {driver.current_url}\n{locators.app} website title is: {driver.title}')
        sleep(0.25)
    else:
        print('please check!')
        tearDown()


def tearDown():
    if driver is not None:
        print('---------------~*~---------------------')
        print(f'The test complete at {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


# login to Moodle
def log_in(username, password):
    if driver.current_url == locators.app_homepage_url:
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == locators.app_login_url:
            print(f'{locators.app} App Login page is displayed!')
            sleep(0.25)
            driver.find_element(By.ID, 'username').send_keys(username)
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys(password)
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click()
            # validate we are in Dashboard page
            if driver.current_url == locators.app_dashboard_url and driver.title == locators.app_dashboard_title:
                assert driver.current_url == locators.app_dashboard_url
                assert driver.title == locators.app_dashboard_title
                print(
                    f'Login successfully. {locators.app} {locators.app_dashboard_title} is displayed- Page title is {driver.title}')
            else:
                print(
                    f'{locators.app} {locators.app_dashboard_title} is not displayed,Please check your code and try again.')


def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
    sleep(0.25)
    # validate logout successful
    if driver.current_url == locators.app_homepage_url:
        print(f'--- {locators.full_name} Logout Successful! at {datetime.datetime.now()}')


def add_user():
    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    assert driver.title == locators.app_addnewuser_title
    print(f'Add a new user page is launched. ------Page title is  {driver.title}')
    driver.find_element(By.ID, 'id_username').send_keys(locators.user_name)
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.password)
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastname').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text(
        'Allow everyone to see my email address')
    sleep(0.25)
    driver.find_element(By.ID, 'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
    sleep(0.25)
    driver.find_element(By.ID, 'id_city').send_keys(locators.city)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text('Canada')
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_timezone')).select_by_visible_text('America/Vancouver')
    sleep(0.25)
    driver.find_element(By.ID, 'id_description_editoreditable').clear()
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.description)
    sleep(0.25)
    driver.find_element(By.CLASS_NAME, 'dndupload-arrow').click()
    sleep(0.25)
    # driver.find_element(By.LINK_TEXT,'Server files').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT,'sl_Frozen').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT,'sl_How to build a snowman').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT,'Course image').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT,'gieEd4R5T.png').click()
    pic_path = ['Server files', 'sl_Frozen', 'sl_How to build a snowman', 'Course image', 'gieEd4R5T.png']
    for p in pic_path:
        driver.find_element(By.LINK_TEXT, p).click()
    sleep(0.25)
    # select the radio button
    driver.find_element(By.XPATH, '//label[contains(.,"Create an alias/shortcut to the file")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[contains(.,"Select this file")]').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_imagealt').send_keys(locators.pic_desc)
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, "Additional names").click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_middlename').send_keys(locators.middle_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Interests').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@placeholder,"Enter tags...")]').click()
    for tags in locators.list_of_interests:
        driver.find_element(By.XPATH, '//input[contains(@placeholder,"Enter tags...")]').send_keys(tags, Keys.ENTER)
        #driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplete_input")]').send_keys(tags, Keys.ENTER)
        sleep(0.25)

    driver.find_element(By.LINK_TEXT, 'Optional').click()
    for i in range(len(locators.list_opt)):
        opt, ids, val = locators.list_opt[i], locators.list_ids[i], locators.list_val[i]
        # print(f'populate{opt}field')
        driver.find_element(By.ID, ids).send_keys(val)
        sleep(0.25)

    #################################################
    driver.find_element(By.ID, 'id_submitbutton').click()
    sleep(0.25)
    print(f'-----new user {locators.user_name} {locators.email} is added-----')
    logger('create')
    ##################################################


def search_user():
    if driver.current_url == locators.app_user_mainpage_url and driver.title == locators.app_user_mainpage_title:
        assert driver.find_element(By.LINK_TEXT, 'Browse list of users').is_displayed()
        print('----browse list of users is displayed')
        sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
        sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()
        sleep(0.25)
        if driver.find_element(By.XPATH, f'//td[contains(.,"{locators.email}")]'):
            print(f'-----User {locators.email} is found!')


def check_new_user_can_login():
    if driver.current_url == locators.app_dashboard_url and driver.title == locators.app_dashboard_title:
        if driver.find_element(By.XPATH, f'//span[contains(.,"{locators.full_name}")]').is_displayed():
            print(f' ---- User with full name: {locators.full_name} is displayed. ----')


def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.email}\t'
          f'{locators.user_name}\t'
          f'{locators.password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()


def delete_user():
    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Browse list of users').click()
    sleep(0.25)
    search_user()
    sleep(0.25)
    #assert driver.find_element(By.XPATH,f'//td[contains(.,"{locators.full_name}"]').is_displayed()
    #sleep(0.5)
    #driver.find_element(By.XPATH,'//input/id[contains(.,"id_filter_email")]').click()
    #print('fliter is removed')
    sleep(0.5)
    driver.find_element(By.XPATH,'//i[@title="Delete"]').click()
    sleep(0.5)
    #assert driver.find_element(By.XPATH,'//span[contains(.,"Delete user"])').is_displayed()
    sleep(0.5)
    driver.find_element(By.XPATH,'//button[contains(.,"Delete")]').click()
    sleep(0.25)
    print(f'-----User {locators.full_name} is deleted')
    sleep(0.25)
    logger('Deleted')


# # create new use
# setUp()
# log_in(locators.admin_username, locators.admin_password)
# add_user()
# search_user()
# log_out()
#
# # login new_user
# log_in(locators.user_name, locators.password)
# check_new_user_can_login()
# sleep(0.25)
# log_out()
# logger('create')
#
# #delete new_user
# log_in(locators.admin_username,locators.admin_password)
# delete_user()
# log_out()
#
# tearDown()
