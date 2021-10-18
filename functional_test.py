from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    '''Тест нового посетителя'''

    def setUp(self):
        '''Установка'''
        self.browser = webdriver.Chrome()

    def tearDown(self):
        '''демонтаж'''
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''тест: можно начать список и получить его позже'''
        # Открыть домашнюю страницу
        self.browser.get('http://localhost:8000')

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

        # Добавить ещё один элемент
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)


        # Старница обновляется и показывает два элемента списка
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Купить павлиньи перья', [row.text for row in rows])
        self.assertIn('2: Сделать мушку из павлиньих перьев', [row.text for row in rows])
        self.assertTrue(
            any(row.text == '1: Купить павлиньи перья' for row in rows),
            f"Новый элемент списка не появился в таблице. Содержимым было: {table.text=}"
        )


        self.fail('Закончить тест')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
