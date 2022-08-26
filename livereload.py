from selenium import webdriver
from filehash import FileHash as fh
import time
import json

with open("config.json") as cfg:
    config = json.load(cfg)

filepath = config["filepath"]
browserpath = config["browserpath"]
updatedelay = config["updatedelay"]

md5hasher = fh('md5')
filehash = md5hasher.hash_file(filepath)

driver = webdriver.Chrome()

driver.get(browserpath)

while True:
    if filehash != md5hasher.hash_file(filepath):
        filehash = md5hasher.hash_file(filepath)
        driver.refresh()
        pass

    time.sleep(updatedelay)
