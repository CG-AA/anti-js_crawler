from selenium import webdriver

# Start Chrome with the new options
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("http://google.com")

cookies = driver.get_cookies()

# Get the HTML of the webpage
html = driver.page_source

# Print the HTML
print(cookies)

# Close the browser
driver.quit()