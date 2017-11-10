from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

#removed private info

#Login
driver = webdriver.Firefox()
driver.get("https://studentemployment.neu.edu/Tsx_StuHireDetail.aspx?HiId=204047")
username = driver.find_element_by_css_selector("#Skin_ctl00_LoginNameText")
username.send_keys("username")
password = driver.find_element_by_css_selector("#Skin_ctl00_LoginPasswordText")
password.send_keys("password")
submit = driver.find_element_by_xpath("""//*[@id="Skin_ctl00_LoginTable"]/tbody/tr[4]/td[2]/input""")
submit.click()


#Selecting the timesheet
timesheet = driver.find_element_by_css_selector("#Skin_body_TimesheetList > tbody > tr.tsrowalt > td.tslink > a")
timesheet.click()

#Day 1 Automation
entry = driver.find_element_by_css_selector(""".addentry > td:nth-child(1) > a:nth-child(1)""")
entry.click()
date_select = Select(driver.find_element_by_css_selector('.addentry > td:nth-child(1) > span:nth-child(1) > select:nth-child(1)'))
date_select.select_by_visible_text("Day")
time_start = Select(driver.find_element_by_css_selector('#Skin_body_ctl01_StartDateTime1'))
time_start.select_by_visible_text("Time 1")
time_end = Select(driver.find_element_by_css_selector('#Skin_body_ctl01_EndDateTime1'))
time_end.select_by_visible_text("Time 2")
add = driver.find_element_by_css_selector("""#Skin_body_ctl01_TsEntriesTable > tbody > tr.addentry > td:nth-child(6) > input[type="submit"]:nth-child(1)""")
add.click()

#Day 2
entry = driver.find_element_by_css_selector("""#Skin_body_ctl01_TsEntriesTable > tbody > tr.addentry > td > a""")
entry.click()
date_select = Select(driver.find_element_by_css_selector('#Skin_body_ctl01_TsEntriesTable > tbody > tr.addentry > td:nth-child(1) > span > select'))
date_select.select_by_visible_text("Day")
time_start = Select(driver.find_element_by_css_selector('#Skin_body_ctl01_StartDateTime1'))
time_start.select_by_visible_text("Time 1")
time_end = Select(driver.find_element_by_css_selector('#Skin_body_ctl01_EndDateTime1'))
time_end.select_by_visible_text("Time 2")
add = driver.find_element_by_css_selector("""#Skin_body_ctl01_TsEntriesTable > tbody > tr.addentry > td:nth-child(6) > input[type="submit"]:nth-child(1)""")
add.click()


#Day 3 
entry = driver.find_element_by_css_selector("""#Skin_body_ctl01_TsEntriesTable > tbody > tr.addentry > td > a""")
entry.click()
date_select = Select(driver.find_element_by_css_selector('#Skin_body_ctl01_TsEntriesTable > tbody > tr.addentry > td:nth-child(1) > span > select'))
date_select.select_by_visible_text("Day")
time_start = Select(driver.find_element_by_css_selector('#Skin_body_ctl01_StartDateTime1'))
time_start.select_by_visible_text("Time 1")
time_end = Select(driver.find_element_by_css_selector('#Skin_body_ctl01_EndDateTime1'))
time_end.select_by_visible_text("Time 2")
add = driver.find_element_by_css_selector("""#Skin_body_ctl01_TsEntriesTable > tbody > tr.addentry > td:nth-child(6) > input[type="submit"]:nth-child(1)""")
add.click()

#Day 4 
entry = driver.find_element_by_css_selector("""#Skin_body_ctl01_TsEntriesTable > tbody > tr.addentry > td > a""")
entry.click()
date_select = Select(driver.find_element_by_css_selector('#Skin_body_ctl01_TsEntriesTable > tbody > tr.addentry > td:nth-child(1) > span > select'))
date_select.select_by_visible_text("Day")
time_start = Select(driver.find_element_by_css_selector('#Skin_body_ctl01_StartDateTime1'))
time_start.select_by_visible_text("Time 1")
time_end = Select(driver.find_element_by_css_selector('#Skin_body_ctl01_EndDateTime1'))
time_end.select_by_visible_text("Time 2")
add = driver.find_element_by_css_selector("""#Skin_body_ctl01_TsEntriesTable > tbody > tr.addentry > td:nth-child(6) > input[type="submit"]:nth-child(1)""")
add.click()

