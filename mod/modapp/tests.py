from django.test import TestCase
from .models import Vacancy
from userapp.models import BlogUser
from faker import Faker
from mixer.backend.django import mixer


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
        self.assertEqual(str(self.vacancy_str), 'test_vacancy_str')


class VacancyTestCaseFaker(TestCase):

    def setUp(self):
        faker = Faker()

        user = BlogUser.objects.create_user(username=faker.name(), email='test@test.com', password='leo1234567')
        self.vacancy = Vacancy.objects.create(name=faker.name(), user=user)

        self.vacancy_str = Vacancy.objects.create(name='test_vacancy_str', user=user)

    def test_has_image(self):
        self.assertFalse(self.vacancy.has_image())

    def test_some_method(self):
        self.assertFalse(self.vacancy.some_method() == 'some method')

    def test_str(self):
        self.assertEqual(str(self.vacancy_str), 'test_vacancy_str')


class VacancyTestCaseMixer(TestCase):
    def setUp(self):
        self.vacancy = mixer.blend(Vacancy)

        self.vacancy_str = mixer.blend(Vacancy, name='test_vacancy_str')

    def test_has_image(self):
        self.assertFalse(self.vacancy.has_image())

    def test_some_method(self):
        self.assertFalse(self.vacancy.some_method() == 'some method')

    def test_str(self):
        self.assertEqual(str(self.vacancy_str), 'test_vacancy_str')
