from selenium import webdriver
from time import sleep
from login_details import *

class BumbleBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def open_bumble(self):
        self.driver.get('https://bumble.com/')

        sleep(2)
        #join button
        join = self.driver.find_element('xpath', '/html/body/div[2]/div/div/main/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/a')
        join.click()

        sleep(5)

        #start login
        self.facebook_login()

    def facebook_login(self):

        # find and click FB login button
        

        login_with_fb = self.driver.find_element('xpath','//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/button/span/span[2]/span')

        login_with_fb.click()

        
        # save references to main and FB windows
        sleep(5)
        base_window = self.driver.window_handles[0]
        fb_popup_window = self.driver.window_handles[1]
        # switch to FB window
        self.driver.switch_to.window(fb_popup_window)

        # login to FB

        email_field = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
        pw_field = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
        login_button = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
        
        # enter email, password and login
        email_field.send_keys(fbusername)
        pw_field.send_keys(fbpassword)
        login_button.click()

        sleep(10)
        continue_button = self.driver.find_element('xpath', '/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div')
        continue_button.click()

        #important
        self.driver.switch_to.window(base_window)
        
    def like(self):
        like_btn = self.driver.find_element('xpath', '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div')
        like_btn.click()
    def dislike(self):
        dislike_btn = self.driver.find_element('xpath', '/html/body/div/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(5)
            try:
                self.like()
            except:
                self.dislike()

    # def close_match(self):
    #     match_popup = self.driver.find_element('xpath', '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
    #     match_popup.click()

    # def get_matches(self):
    #     match_profiles = self.driver.find_elements('class name', 'matchListItem')
    #     message_links = []
    #     for profile in match_profiles:
    #         if profile.get_attribute('href') == 'https://tinder.com/app/my-likes' or profile.get_attribute('href') == 'https://tinder.com/app/likes-you':
    #             continue
    #         message_links.append(profile.get_attribute('href'))
    #     return message_links

    # def send_messages_to_matches(self):
    #     links = self.get_matches()
    #     for link in links:
    #         self.send_message(link)

    # def send_message(self, link):
    #     self.driver.get(link)
    #     sleep(2)
    #     text_area = self.driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/textarea')

    #     text_area.send_keys('hi')

    #     text_area.send_keys(Keys.ENTER)

bot = BumbleBot()
bot.open_bumble()
bot.auto_swipe()
# bot.send_messages_to_matches()