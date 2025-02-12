from django.test import SimpleTestCase
from django.urls import reverse


def test_1(self):
    respond = self.client.get('/PM_A/')
    self.assertEqual(respond.status_code, 200)

def test_2(self):
    respond = self.client.get(reverse('PM_A'))
    self.assertEqual(respond.status_code, 200)

def test_3(self):
    respond = self.client.get(reverse('PM_A'))
    self.asserttemplate(respond, 'S_D.html')