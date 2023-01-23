from django.test import TestCase
from .models import Vacancy
from userapp.models import BlogUser


# Create your tests here.
class VacancyTestCase(TestCase):

    def setUp(self):

        user = BlogUser.objects.create_user(username='test_user', email='test@test.com', password='leo1234567')
        self.vacancy = Vacancy.objects.create(name='test_vacancy', user=user)

        self.vacancy_str = Vacancy.objects.create(name='test_vacancy_str', user=user)

    def test_has_image(self):
        self.assertFalse(self.vacancy.has_image())

    def test_some_method(self):
        vacancy = Vacancy.objects.get(name='test_vacancy')
        self.assertFalse(vacancy.some_method() == 'some method')

    def test_str(self):
        self.assertEqual(str(self.vacancy_str), 'test_vacancy_str, user: test_user')


