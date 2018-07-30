from selenium import webdriver
import download
import time

driver=webdriver.Firefox()
driver.get('https://www.taobao.com/')
driver.find_element_by_id('q').send_keys('PS4游戏')
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[1]/div[2]/form/div[1]/button').click()

i=0
while i<5:
    print('第',(i+1),'页')
    j=0
    while j<20:
        driver.execute_script("window.scrollBy(0,400)")
        j+=1
    time.sleep(2)
    imgItem=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[21]/div/div/div[1]')
    for img in imgItem.find_elements_by_xpath(".//img"):
        url=img.get_attribute('src')
        print(url)
        download.download(url)
        #img=0
    driver.find_element_by_css_selector('.next').click()
    i+=1
    time.sleep(2)

driver.quit()

