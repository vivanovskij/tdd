from selenium import webdriver
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
        self.fail('Закончить тест')

        # Ввести элемент списка


if __name__ == '__main__':
    unittest.main(warnings='ignore')
