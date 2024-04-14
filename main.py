import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# WebDriver 객체 생성
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


pointList = ["힐링 방탈출북","LOG_IN 2","LOG_IN 1","메모리컴퍼니","우주라이크","강남 더오름","강남점","KEYESCAPE"
,"강남 더어썸","명동점","혜화점","홍대점","전주점","부산점"]

#지점 변수. 원하는 지점을 복사 붙여넣기 해주세요
#"힐링 방탈출북" "LOG_IN 2" "LOG_IN 1" "메모리컴퍼니" "우주라이크" "강남 더오름" "강남점" "KEYESCAPE"
#"강남 더어썸" "명동점" "혜화점" "홍대점" "전주점" "부산점"
#point = "LOG_IN 1"

#예약할 "일" 을 적어주세요 ex:) 3월 17일 예약하고 싶다 -> date = "17"
date = "28"

themaList=["머니머니패키지", "FOR FREE", "BACK TO THE SCENE+", "A GENTLE MONDAY", "FILM BY EDDY",
 "FILM BY STEVE", "FILM BY BOB", "US", "WANNA GO HOME", "네드", "엔제리오", "월야애담-영문병행표기",
"살랑살랑연구소", "그카지말라캤자나"]

#테마를 선택합니다.
#"머니머니패키지" "FOR FREE" "BACK TO THE SCENE+" "A GENTLE MONDAY" "FILM BY EDDY"
#"FILM BY STEVE" "FILM BY BOB" "US" "WANNA GO HOME" "네드" "엔제리오" "월야애담-영문병행표기"
#"살랑살랑연구소" "그카지말라캤자나" ...
#thema = "머니머니패키지"

#원하는 시간을 입력해주세요. 아래와 같은 양식을 지켜주세요. 테마마다 가능한 시간이 다르므로 사이트를 확인하고 입력해주세요
wanted_time="09:"
sub_time="17:"
sub_sub_time="20:"


#예약자 이름을 입력해주세요
name = "방수민"

#전화번호 가운데 자리와 끝자리를 입력해주세요
middle_num = 8497
end_num = 9425

def set_point(selectedpoint):
    point = selectedpoint
    print("선택된 지점 : ",point)

def set_thema(selectedThema):
    global  thema
    thema = selectedThema


def run_macro():
    max_retries = 5
    retry_count = 0
    #인원추가는 현장 추가결제로 합니다. defaul는 2명이며 매크로 적용하고 싶다면 아래 주석을 해제해주세요
    while retry_count < max_retries:
        try:
            # 웹 페이지 로드
            driver.get("https://keyescape.co.kr/web/home.php?go=rev.make")

            # 지점 선택
            select_point = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[text()='"+point+"']")))
            select_point.click()
            time.sleep(1)

            # 날짜 선택
            select_date = WebDriverWait(driver,40).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'"+date+"')]")))
            select_date.click()
            time.sleep(0.4)


            # 테마 선택
            select_thema = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'"+thema+"')]")))
            select_thema.click()
            time.sleep(0.3)


            try:
                # 시간 선택
                select_time = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'"+wanted_time+"')]")))
                if 'impossible' in select_time.get_attribute('class'):
                    raise Exception("Select time is impossible")
                select_time.click()
                time.sleep(0.2)
            except:
                try:
                    sub_time = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'" + sub_time + "')]")))
                    if 'impossible' in sub_time.get_attribute('class'):
                        raise Exception("Select time is impossible")
                    sub_time.click()
                    time.sleep(0.2)

                except:
                    sub_sub_time = WebDriverWait(driver, 40).until(
                        EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'" + sub_sub_time + "')]")))
                    if 'impossible' in sub_sub_time.get_attribute('class'):
                        raise Exception("Select time is impossible")
                    sub_sub_time.click()
                    time.sleep(0.2)


            reserve_start = driver.find_element(By.CLASS_NAME,"b").send_keys(Keys.ENTER)
            time.sleep(0.2)

            # 이름 입력
            enter_name = driver.find_element(By.NAME,"name")
            enter_name.send_keys(name)

            # 전화번호 가운데 입력
            enter_middle_num = driver.find_element(By.NAME, "mobile2")
            enter_middle_num.send_keys(middle_num)
            #
            # 전화번호 끝자리 입력
            enter_end_num = driver.find_element(By.NAME, "mobile3")
            enter_end_num.send_keys(end_num)


            # # 인원 선택
            # select_people = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'person')))
            # select_people.send_keys(Keys.ENTER)
            # time.sleep(1)
            # select_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//option[contains(text(),'3')]")))
            # select_option.click()


            # 동의 체크
            select_check = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'ck_agree')))
            select_check.click()

            #매크로 입력창
            macro_input = driver.find_element(By.NAME,"input_captcha")
            macro_input.send_keys(Keys.ENTER)

            # 창이 꺼지지 않는 시간
            time.sleep(5000)

        except Exception as e:
            print("접속에 실패했습니다. 재시도 중...")
            retry_count += 1
            time.sleep(5)


def main():
    global point
    root = tk.Tk()
    root.title("매크로 실행")
    root.geometry("500x500")
    row=0
    col=0
    tk.Label(root,text="지점을 선택해주세요").grid(row=row,column=col)
    row += 1
    for i in range(len(pointList)):
        if col == 5:
            row = row+1
            col = 0

        tk.Button(root,text=pointList[i],
                  command=lambda p=pointList[i]: set_point(p)).grid(row=row,column=col,padx=5, pady=5)
        col += 1
    row += 1

    tk.Label(root, text=point).grid(row=row,column=0)
    # 변수 입력을 위한 라벨 및 입력 필드 생성
    # tk.Label(root, text="지점:").grid(row=4, column=1)
    # global point_entry
    # point_entry = tk.Entry(root)
    # point_entry.grid(row=4, column=1)
    #
    # tk.Label(root, text="예약할 일:").grid(row=5, column=0)
    # global date_entry
    # date_entry = tk.Entry(root)
    # date_entry.grid(row=5, column=1)

    # 필요한 변수들 계속 추가

    # 실행 버튼 생성
    run_button = tk.Button(root, text="실행", command=run_macro)
    run_button.grid(row=8, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    point =""
    main()