from selenium import webdriver
driver=webdriver.Chrome()
driver.fullscreen_window()
driver.get("https://www.google.com")
driver.find_element_by_class_name('gsfi').send_keys('习近平\n')