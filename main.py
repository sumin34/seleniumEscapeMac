import time
from selenium import webdriver
import pyperclip as pyperclip
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# service = Service(executable_path=r"C:\Users\jki00\PycharmProjects\seleniumEscapeMac\chromedriver.exe")
service = Service(executable_path="./chromedriver.exe")
# WebDriver 객체 생성
driver = webdriver.Chrome(service=service)





try:
    # 웹 페이지 로드
    driver.get("https://keyescape.co.kr/web/home.php?go=rev.make")


    # 지점 선택
    select_point = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[text()='LOG_IN 1']")))
    select_point.click()
    time.sleep(0.5)
    # 날짜 선택
    select_date = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'15')]")))
    select_date.click()
    time.sleep(0.5)
    # 테마 선택
    select_thema = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'머니머니패키지')]")))
    select_thema.click()
    time.sleep(0.5)

    # 시간 선택
    select_time = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'09:30  ')]")))
    select_time.click()
    time.sleep(1)

    #예약 시작 버튼 클릭
    # reserve_start = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'예약하기')]")))
    # reserve_start.click()

    reserve_start = driver.find_element(By.CLASS_NAME,"b").send_keys(Keys.ENTER)
    time.sleep(0.5)

    # 이름 입력
    enter_name = driver.find_element(By.NAME,"name")
    enter_name.send_keys("방수민")

    # 전화번호 가운데 입력
    enter_middle_num = driver.find_element(By.NAME, "mobile2")
    enter_middle_num.send_keys(8497)
    #
    # 전화번호 끝자리 입력
    enter_end_num = driver.find_element(By.NAME, "mobile3")
    enter_end_num.send_keys(9425)

    # 인원 선택
    select_people = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'person')))
    select_people.send_keys(Keys.ENTER)
    time.sleep(1)

    select_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//option[contains(text(),'3')]")))
    select_option.click()

    # 동의 체크
    select_check = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'ck_agree')))
    select_check.click()

    # 여기서 60초간 대기하도록 변경
    time.sleep(500)

finally:
    # 브라우저 종료
    driver.quit()



