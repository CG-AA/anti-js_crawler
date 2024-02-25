import json
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

def load_settings():
    try:
        with open('setting.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError("File not found: setting.json")

def init_driver():
    return webdriver.Chrome()

def login(driver, settings, serial):
    driver.get('https://apcs.camp/vip')
    driver.find_element(By.NAME, "email").send_keys(settings['login_settings']['acc'+str(serial)])
    driver.find_element(By.NAME, "password").send_keys(settings['login_settings']['pas'+str(serial)])
    driver.find_element(By.ID, ":r2:").click()
    sleep(1)
    driver.get('https://apcs.camp/vip/judge')
    sleep(1)

def write_problem(driver, problem_id):
    sess = requests.Session()
    for cookie in driver.get_cookies():
        sess.cookies.set(cookie['name'], cookie['value'])
    HTML = sess.get(f"https://judge.apcs.camp/problems/{problem_id}")
    with open(f"./problems/problem{problem_id}.html", "w", encoding='utf-8') as file:
        file.write(HTML.text)

def download_problems(driver, settings):
    os.makedirs("./problems", exist_ok=True)
    for i in settings['catch'][f'a{settings["temp"]}']:
        for j in range(int(settings['catch'][f'a{settings["temp"]}'][i][0]), int(settings['catch'][f'a{settings["temp"]}'][i][1])+1):
            write_problem(driver, j)

def main():
    settings = load_settings()
    driver = init_driver()
    login(driver, settings, settings['temp'])
    download_problems(driver, settings)

if __name__ == "__main__":
    main()