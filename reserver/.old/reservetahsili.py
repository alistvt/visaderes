from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys





BASE_DIR=os.path.dirname(os.path.abspath(__file__))
FF_DIR = os.path.join(BASE_DIR, 'geckodriver')
url='https://ir-appointment.visametric.com/ir'
class BOT:
    def __init__(self):
        options = Options()

        options.add_argument("user-data-dir=" + os.path.dirname(os.path.abspath(__file__)) + "/hamyarweb")

        self.driver = webdriver.Chrome(executable_path=os.path.dirname(os.path.abspath(__file__)) + "/chromedriver",
                                  options=options)
        self.driver.maximize_window()


    def login(self,city,payment_cart,payment_date,sheba,sheba_owner,first_name,last_name,birth_year,birth_month,birth_date,passport,phone,email):
        self.driver.get(url)
        self.driver.find_element(By.XPATH,'//*[@id="nationalBtn"]').click()
        sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="result1"]').click()
        sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="result3"]').click()
        #WebDriverWait(self.driver, 120).until(lambda x: x.find_element_by_css_selector('.antigate_solver.solved'))
        WebDriverWait(self.driver, 200).until(lambda d: d.find_element(By.CSS_SELECTOR,".antigate_solver.solved"))
        sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="btnSubmit"]').click()

        sleep(2)

        self.driver.find_element(By.XPATH, f"//select[@name='city']/option[text()='{city}']").click()
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
        sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="paymentCardInput"]').send_keys(payment_cart)
        self.driver.execute_script('document.getElementsByName("cardDatepicker")[0].removeAttribute("readonly")')
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="popupDatepicker2"]').clear()
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="popupDatepicker2"]').send_keys(payment_date)
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="paymentCardInput"]').click()
        self.driver.find_element(By.XPATH,'//*[@id="checkCardListBtn"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="checkCardListDiv"]/table/tbody/tr/td[1]/input').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="btnAppCountNext"]').click()



        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="scheba_number"]').send_keys(sheba)
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="scheba_name"]').send_keys(sheba_owner)
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="name1"]').send_keys(first_name)
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="surname1"]').send_keys(last_name)
        sleep(1)
        self.driver.find_element(By.XPATH, f"//select[@name='birthyear1']/option[text()='{birth_year}']").click()
        sleep(1)

        self.driver.find_element(By.XPATH, f"//select[@name='birthmonth1']/option[text()='{birth_month}']").click()
        sleep(1)
        self.driver.find_element(By.XPATH, f"//select[@name='birthday1']/option[text()='{birth_date}']").click()
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="passport1"]').send_keys(passport)
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="phone1"]').send_keys(phone)
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="email1"]').send_keys(email)
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="btnAppPersonalNext"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="previewchk"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="btnAppPreviewNext"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="datepicker"]/input').click()
        sleep(1)
        m = self.driver.find_elements(By.CLASS_NAME, "day")
        for i in m:
            if i.get_attribute('class')=='day':
                print('day ' + i.text +' for reserve')
        with open("page_source.html", "w", encoding='utf-8') as f:
            f.write(self.driver.page_source)



if __name__ == '__main__':
    bt=BOT()
    bt.login()




