import websockets
import asyncio
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException


class Instance:
    def __init__(self):
        self.driver = None
        self.email_address = None
        self.pwd = None

    def open_selenium(self):
        self.driver = webdriver.Chrome("C:\\Users\\lariv\\AppData\\Local\\Google\\Chrome\\User Data\\chromedriver.exe")
        self.driver.get("https://netflix.com/")

    def login(self):
        try:
            ActionChains(self.driver).click(self.driver.find_element_by_css_selector(".btn-accept.btn-red"))
            self.driver.find_element_by_id("id_email_hero_fuji").send_keys(self.email_address)
            ActionChains(self.driver).click(self.driver.find_element_by_css_selector(".btn.btn-red.nmhp-cta.nmhp-cta-extra-large.btn-none.btn-custom")).perform()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'id_password')))
            self.driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(self.pwd)
            ActionChains(self.driver).click(self.driver.find_element_by_css_selector(".btn.login-button.btn-submit.btn-small")).perform()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/div/a')))
            ActionChains(self.driver).click(self.driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/div/a')).perform()
        except TimeoutException:
            print("Failed!")

    async def ws_receive(self, websocket, path):
        json_data = json.load(await websocket.recv())
        self.email_address = json_data["email_address"]
        self.pwd = json_data["pwd"]
        self.login()

    def start(self):
        self.open_selenium()
        asyncio.run(self.start_ws())

    async def start_ws(self):
        async with websockets.serve(self.ws_receive, "localhost", 8765):
            await asyncio.Future()


if __name__ == '__main__':
    instance = Instance()
    instance.start()
