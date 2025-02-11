from django.test import SimpleTestCase
from django.urls import reverse

class MessagePageTest(SimpleTestCase):

    def test_urls_is_exist(self):
        response = self.client.get('/Amin_message/')
        self.assertEqual(response.status_code, 200)

    def test_urls_available(self):
        response = self.client.get(reverse('Amin_message'))
        self.assertEqual(response.status_code, 200)

    def test_templates_name(self):
        response = self.client.get(reverse('Amin_message'))
        self.assertTemplateUsed(response, 'home.html')

    def test_contains_correct_template(self):
        response = self.client.get(reverse('Amin_message'))
        self.assertContains(response, ' <h1><b><i>WELCOME '
                                      'TO OUR SITE</i></b></h1>')