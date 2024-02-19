from selenium import webdriver
import json
from selenium.webdriver.common.by import By
import os
from time import sleep

def init():
    sett = initsetting()
    driver = initdriver(sett)
    return sett, driver

def initsetting():
    try:
        with open('setting.json', 'r') as file:
            settings = json.load(file)
        return settings
    except FileNotFoundError:
        raise FileNotFoundError("File not found: setting.json")

def initdriver(sett):
    driver = webdriver.Chrome()
    return driver

def login(sett, driver, serial):
    driver.get('https://apcs.camp/vip')
    driver.find_element(By.NAME, "email").send_keys(sett['login_settings']['acc'+str(serial)])
    driver.find_element(By.NAME, "password").send_keys(sett['login_settings']['pas'+str(serial)])
    driver.find_element(By.ID, ":r2:").click()
    sleep(1)
    driver.get('https://apcs.camp/vip/judge')
    sleep(1)

def getNwrite(driver, i):
    driver.get("https://judge.apcs.camp/problems/" + str(i))
    with open("./problems/problem" + str(i) + ".html", "w") as file:
        file.write(driver.page_source)

def getproblemsHTML(driver, sett):
    os.makedirs("./problems", exist_ok=True)
    for i in sett['catch']['a2']:
        for j in range(int(sett['catch']['a2'][i][0]), int(sett['catch']['a2'][i][1])+1):
            getNwrite(driver, j)


def main():
    sett, driver = init()
    login(sett, driver, 2)
    getproblemsHTML(driver, sett)

main()