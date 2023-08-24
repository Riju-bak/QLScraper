import os

from selenium import webdriver
from selenium.webdriver.common.by import By


class Scraper:
    def __init__(self, primary_url):
        self.primary_url = primary_url
        self.driver = webdriver.Chrome()
        self.driver.get(primary_url)
        self.num_videos = 1
        self.out = "./QLEmbeddedVideos"  # the folder where videos will be downloaded

    def Fetch(self):
        # If ./QLEmbeddedVideos doesn't exist, create it
        self.CreateFolder(self.out)

        self.ShowEntries(100)

        self.ScrapeAndDownload()

    def CreateFolder(self, path):
        if not os.path.exists(path):
            os.mkdir(path)

    def ShowEntries(self, num_entries):
        entries_select = self.driver.find_element(By.NAME, 'tablepress-2_length')
        entries_select.send_keys('100')

    def ScrapeAndDownload(self):
        table = self.driver.find_element(By.ID, 'tablepress-2')
        rows = table.find_elements(By.TAG_NAME, 'tr')

        # Loop through each row and extract the href value
        for row in rows[1:]:
            column = row.find_element(By.CLASS_NAME, 'column-7')
            if column:
                anchor_element = column.find_element(By.TAG_NAME, 'a')
                link = '/'.join(anchor_element.get_attribute('href').split('/')[:-1])
                print(link)
                filename = link.split('/')[-1]  # Extract the filename from the link
                filepath = self.out
                # Download the file using curl
                os.system(f'wget -P "{filepath}" "{link}"')
                print(f"Downloaded: {filename}")
