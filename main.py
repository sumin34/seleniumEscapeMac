import tkinter as tk
import tkinter.ttk
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


pointList = ["LOG_IN 2","LOG_IN 1","메모리컴퍼니","우주라이크","강남 더오름","강남점"
,"홍대점","전주점","부산점"]

#지점 변수. 원하는 지점을 복사 붙여넣기 해주세요
#"힐링 방탈출북" "LOG_IN 2" "LOG_IN 1" "메모리컴퍼니" "우주라이크" "강남 더오름" "강남점" "KEYESCAPE"
#"강남 더어썸" "명동점" "혜화점" "홍대점" "전주점" "부산점"

#예약할 "일" 을 적어주세요 ex:) 3월 17일 예약하고 싶다 -> date = "17"
themaList=["머니머니패키지", "FOR FREE", "BACK TO THE SCENE+", "A GENTLE MONDAY", "FILM BY EDDY",
 "FILM BY STEVE", "FILM BY BOB", "US", "WANNA GO HOME", "네드", "엔제리오", "월야애담-영문병행표기",
"살랑살랑연구소", "그카지말라캤자나"]

themes = {
    "LOG_IN 2": ["BACK TO THE SCENE+", "A GENTLE MONDAY"],
    "LOG_IN 1": ["머니머니패키지", "FOR FREE"],
    "메모리컴퍼니": ["FILM BY EDDY", "FILM BY STEVE", "FILM BY BOB"],
    "우주라이크": ["US", "WANNA GO HOME"],
    "강남 더오름": ["네드", "엔제리오"],
    "강남점": ["월야애담-영문병행표기", "살랑살랑연구소", "그카지말라캤자나"],
    "부산점": ["정신병동", "파파라치", "난쟁이의 장난-영문병행표기","셜록 죽음의 전화","신비의숲 고대마법의 비밀"],
    "전주점": ["난쟁이의 장난-영문병행표기", "혜화잡화점", "월야애담-영문병행표기","사라진 목격자","살랑살랑연구소"],
    "홍대점": ["삐릿-뽀", "홀리데이", "고백"]
}
#테마를 선택합니다.
#"머니머니패키지" "FOR FREE" "BACK TO THE SCENE+" "A GENTLE MONDAY" "FILM BY EDDY"
#"FILM BY STEVE" "FILM BY BOB" "US" "WANNA GO HOME" "네드" "엔제리오" "월야애담-영문병행표기"
#"살랑살랑연구소" "그카지말라캤자나" ...
#thema = "머니머니패키지"

#원하는 시간을 입력해주세요. 아래와 같은 양식을 지켜주세요. 테마마다 가능한 시간이 다르므로 사이트를 확인하고 입력해주세요
# wanted_time="09:"
# sub_time="17:"
# sub_sub_time="20:"
#
#
# #예약자 이름을 입력해주세요
# name = "방수민"
#
# #전화번호 가운데 자리와 끝자리를 입력해주세요
# middle_num = 8497
# end_num = 9425
#
# def set_point(selectedpoint):
#     point = selectedpoint
#     print("선택된 지점 : ",point)
#
# def set_thema(selectedThema):
#     global  thema
#     thema = selectedThema
#

def run_macro(point,date, thema,wanted_time,sub_time,sub_sub_time,name,middle_num,end_num):
    max_retries = 5
    retry_count = 0
    #인원추가는 현장 추가결제로 합니다. defaul는 2명이며 매크로 적용하고 싶다면 아래 주석을 해제해주세요
    while retry_count < max_retries:
        try:
            # 웹 페이지 로드
            driver.get("https://keyescape.co.kr/web/home.php?go=rev.make")

            # 지점 선택
            select_point = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[text()='"+point+"']")))
            select_point.click()
            time.sleep(0.5)

            # print("여기 시작")
            #
            # click_next = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='next']/a")))
            # click_next.click()
            # time.sleep(0.5)
            #
            # print("여기 도착") //*[@id="calendar_data"]/table/tbody/tr[3]/td[3]/font

            if driver.find_elements(By.XPATH,f'//font[contains(text(),"{date}")]'):
                click_next = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='next']/a")))
                click_next.click()
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
    root = tk.Tk()
    root.title("매크로 실행")
    root.geometry("500x250")

    def on_select(event):
        selected_item = point_combobox.get()
        theme_combobox['values'] = themes[selected_item]
    #지점 ///////////////////////////////////////////////////////////////
    point_combobox = tkinter.ttk.Combobox(root)
    point_combobox.config(values=pointList)
    point_combobox.config(state="readonly")
    point_combobox.set("지점을 선택해주세요")
    point_combobox.bind("<<ComboboxSelected>>", on_select)
    point_combobox.grid(column=3,row=0)
    #날짜 /////////////////////////////////////////////////////////////////
    date_input = tkinter.ttk.Entry(root)
    date_label = tkinter.Label(text="원하는 날짜를 입력하세요(ex:2,30,11...)")
    date_label.grid(column=0,row=4)
    date_input.grid(column=3,row=4)
    #테마 ////////////////////////////////////////////////////////////////////
    theme_combobox = tkinter.ttk.Combobox(root)
    theme_combobox.set("테마를 선택해주세요")
    theme_combobox.grid(column=3,row=8)
    #시간 입력 /////////////////////////////////////////////////////////////////
    time_input = tkinter.ttk.Entry(root)
    time_label = tkinter.Label(text="원하는 시간을 다음과 같이 입력하세요(ex 09:,21:...)")
    time_label.grid(column=0,row=12)
    time_input.grid(column=3,row=12)

    sub_time_input = tkinter.ttk.Entry(root)
    sub_time_label = tkinter.Label(text="두번째로 원하는 시간을 다음과 같이 입력하세요(ex 21:)")
    sub_time_label.grid(column=0,row=16)
    sub_time_input.grid(column=3,row=16)

    sub_sub_time_input = tkinter.ttk.Entry(root)
    sub_sub_time_label = tkinter.Label(text="세번째로 원하는 시간을 다음과 같이 입력하세요(ex 09: )")
    sub_sub_time_label.grid(column=0,row=20)
    sub_sub_time_input.grid(column=3,row=20)

    name_input = tkinter.ttk.Entry(root)
    name_label = tkinter.Label(text="예약자 성함을 입력해주세요")
    name_label.grid(column=0,row=24)
    name_input.grid(column=3,row=24)

    middle_input = tkinter.ttk.Entry(root)
    middle_label = tkinter.Label(text="전화번호 가운데 자리를 입력해주세요")
    middle_label.grid(column=0,row=28)
    middle_input.grid(column=3,row=28)

    end_input = tkinter.ttk.Entry(root)
    end_label = tkinter.Label(text="전화번호 끝자리를 입력해주세요")
    end_label.grid(column=0,row=32)
    end_input.grid(column=3,row=32)

    def on_select(event):
        selected_item = point_combobox.get()
        theme_combobox['values'] = themes[selected_item]

    def run_button():
        run_macro(point_combobox.get(), date_input.get(), theme_combobox.get()
                  , time_input.get(), sub_time_input.get(), sub_sub_time_input.get()
                  ,name_input.get(),middle_input.get(),end_input.get())
        root.destroy()


    btn = tk.Button(root)
    btn.config(text="실행")
    btn.config(width=10)
    btn.config(command=run_button)
    btn.grid(column=3,row=36)

    root.mainloop()
    #run_macro("LOG_IN 1","2","머니머니패키지","09:","17:","20:","테스트","1111","2222")

if __name__ == "__main__":
    main()