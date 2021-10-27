from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):
    '''Тест нового посетителя'''

    def setUp(self):
        '''Установка'''
        self.browser = webdriver.Chrome()

    def tearDown(self):
        '''демонтаж'''
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        '''подтверждение строки в таблице списка'''
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''тест: можно начать список и получить его позже'''
        # Открыть домашнюю страницу
        self.browser.get(self.live_server_url)

        # Заголовок и шапка
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Ввести элемент списка
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Набрать в текстовом поле "Купить павлиньи перья"
        inputbox.send_keys('Купить павлиньи перья')

        # Нажать Enter, страница обновляется
        # теперь страница содержит "1: Купить павлиньи перья"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Купить павлиньи перья')

        # Добавить ещё один элемент
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Старница обновляется и показывает два элемента списка
        self.check_for_row_in_list_table('1: Купить павлиньи перья')
        self.check_for_row_in_list_table(
            '2: Сделать мушку из павлиньих перьев')

        self.fail('Закончить тест')
