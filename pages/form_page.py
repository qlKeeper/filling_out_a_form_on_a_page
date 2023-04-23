import time
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators
from selenium.webdriver.common.keys import Keys

class FormPage(BasePage):
    
    def fill_fields_and_submit(self):
        first_name = 'Pasha'
        last_name = 'Rogov'
        email = "pasha_rogov@gmail.com"
        self.remove_footer()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE).send_keys('1234567890')
        subject = self.element_is_visible(Locators.SUBJECT)
        subject.send_keys('English')
        subject.send_keys(Keys.ENTER)
        self.element_is_visible(Locators.HOBBIES).click()
        self.element_is_visible(Locators.FILE_INPUT).\
            send_keys('/home/keeper/QA_automation/automation_project_demoqa/test.txt')
        self.element_is_visible(Locators.CURRENT_ADDRESS).\
            send_keys("City, 1231, USA")
        self.element_is_visible(Locators.SUBMIT).click()
        return first_name, last_name, email
    

    def form_result(self):
        result_list = self.elements_are_visible(Locators.RESULT_TABLE)
        
        result_text = [i.text for i in result_list]
        
        return result_text