from django.test import TestCase

class HomePageTest(TestCase):
    '''тест домашней страницы'''

    def test_home_page_returns_correct_html(self):
        '''тест: домашняя страница возвращает правильный html'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


    def test_can_save_a_POST_request(self):
        '''тест: можно сохранить post-request'''
        response = self.client.post(
                '/',
                data={'item_text': 'A new list item'}
                )
        self.assertIn(
                'A new list item',
                response.content.decode()
                )

