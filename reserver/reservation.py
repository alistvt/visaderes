import os
from pathlib import Path
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import cv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FF_DIR = os.path.join(BASE_DIR, 'geckodriver')


class VisaType:
    schengen = 0
    legal = 1
    student = 2


class Reserver:
    def __init__(self, file_path, visa_type):
        options = Options()
        options.add_argument("user-data-dir=" + os.path.dirname(os.path.abspath(__file__)) + "/hamyarweb")
        self.driver = webdriver.Chrome(executable_path=os.path.dirname(os.path.abspath(__file__)) + "/chromedriver", options=options)
        self.driver.maximize_window()
        self.read_info_file(file_path)
        self.type = visa_type

    def read_info_file(self, file_path):
        yaml_file = open(file_path, 'r', encoding='utf8')
        data = yaml.safe_load(yaml_file)
        self.city = data['city']
        self.payment_cart = data['payment_cart']
        self.payment_date = data['payment_date']
        self.sheba = data['sheba']
        self.sheba_owner = data['sheba_owner']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.birth_year = data['birth_year']
        self.birth_month = data['birth_month']
        self.birth_date = data['birth_date']
        self.passport = data['passport']
        self.phone = data['phone']
        self.email = data['email']

    def reserve(self):

        self.driver.get('https://ir-appointment.visametric.com/ir')
        
        if self.type == VisaType.schengen:
            self.driver.find_element(By.XPATH,'//*[@id="schengenBtn"]').click()
            self.driver.find_element(By.XPATH,'//*[@id="schengenBtn"]').click()
            sleep(1)
            self.driver.find_element(By.XPATH,'//*[@id="result0"]').click()
            sleep(1)
            self.driver.find_element(By.XPATH,'//*[@id="result1"]').click()
        elif self.type == VisaType.legal:
            self.driver.find_element(By.XPATH,'//*[@id="legalizationBtn"]').click()
            sleep(3)
            self.driver.find_element(By.XPATH,'//*[@id="result0"]').click()
            sleep(3)
            self.driver.find_element(By.XPATH,'//*[@id="result1"]').click()
        elif self.type == VisaType.student:
            self.driver.find_element(By.XPATH,'//*[@id="nationalBtn"]').click()
            sleep(3)
            self.driver.find_element(By.XPATH,'//*[@id="result1"]').click()
            sleep(3)
            self.driver.find_element(By.XPATH,'//*[@id="result3"]').click()
        
        WebDriverWait(self.driver, 200).until(lambda d: d.find_element(By.CSS_SELECTOR,".antigate_solver.solved"))
        print('captcha solved')
        self.driver.find_element(By.XPATH,'//*[@id="btnSubmit"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH, f"//select[@name='city']/option[text()='{self.city}']").click()
        sleep(1)
        self.driver.find_element(By.XPATH, "//select[@name='office']/option[text()='تهران']").click()
        sleep(1)
        self.driver.find_element(By.XPATH, "//select[@name='officetype']/option[text()='عادی']").click()
        sleep(1)
        x=self.driver.find_element(By.XPATH, "//select[@name='totalPerson']")
        x.click()
        x.send_keys(Keys.ARROW_DOWN)
        x.send_keys(Keys.ENTER)
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="atm"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="paymentCardInput"]').send_keys(self.payment_cart)
        self.driver.execute_script('document.getElementsByName("cardDatepicker")[0].removeAttribute("readonly")')
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="popupDatepicker2"]').clear()
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="popupDatepicker2"]').send_keys(self.payment_date)
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="paymentCardInput"]').click()
        self.driver.find_element(By.XPATH,'//*[@id="checkCardListBtn"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="checkCardListDiv"]/table/tbody/tr/td[1]/input').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="btnAppCountNext"]').click()

        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="scheba_number"]').send_keys(self.sheba)
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="scheba_name"]').send_keys(self.sheba_owner)
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="name1"]').send_keys(self.first_name)
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="surname1"]').send_keys(self.last_name)
        sleep(1)
        self.driver.find_element(By.XPATH, f"//select[@name='birthyear1']/option[text()='{self.birth_year}']").click()
        sleep(1)

        self.driver.find_element(By.XPATH, f"//select[@name='birthmonth1']/option[text()='{self.birth_month}']").click()
        sleep(1)
        self.driver.find_element(By.XPATH, f"//select[@name='birthday1']/option[text()='{self.birth_date}']").click()
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="passport1"]').send_keys(self.passport)
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="phone1"]').send_keys(self.phone)
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="email1"]').send_keys(self.email)
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="btnAppPersonalNext"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="previewchk"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="btnAppPreviewNext"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="datepicker"]/input').click()
        sleep(1)
        m = self.driver.find_elements(By.CLASS_NAME, "day")
        for i in m:
            if i.get_attribute('class') == 'day':
                print('day ' + i.text + ' for reserve')
        with open("page_source.html", "w", encoding='utf-8') as f:
            f.write(self.driver.page_source)


class ReservationHandler:
    def handle(self, visa_type):
        # TODO: check if file exists
        # TODO: then delte the file and inform
        if visa_type == VisaType.schengen:
            file_path = Path('files') / ('schengen.yaml')
        elif visa_type == VisaType.legal:
            file_path = Path('files') / ('legal.yaml')
        if visa_type == VisaType.student:
            file_path = Path('files') / ('student.yaml')
        
        reserver = Reserver(file_path, visa_type)
        reserver.reserve()

    def validate_file_name(self, file_name):
        return file_name in ['student.yaml', 'schengen.yaml', 'legal.yaml']

    def validate_file(self, file_path):
        # TODO: حتما باید اعداد کمتر از ده قبلش صفر گذاشته شه که دو رقمی شه اگه نه خطا میده!!
        # 8 --> 08
        return True


if __name__ == '__main__':
    print(ReservationHandler().handle(VisaType.student))

else:
    reservation_handler = ReservationHandler()
