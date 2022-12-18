from django.core.management.base import BaseCommand, CommandError
from modapp.models import Region, Vacancy, Skills, NumberOffer, FullOffer
import sqlite3

#Извлекаем данные из тестовой базы и перезаливаем их в базу данных Django через созданную модель
class Command(BaseCommand):
    def handle(self, *args, **options):

        conn = sqlite3.connect('TestDB.db')

        # Создаем курсор
        cursor = conn.cursor()

        cursor.execute('SELECT name from Region')

        region_sql = cursor.fetchall()

        cursor.execute('SELECT name from Skills')

        skills_sql = cursor.fetchall()

        cursor.execute('SELECT name from vacancy')

        vacancy_sql = cursor.fetchall()

        cursor.execute('SELECT number from Number_offer')

        number_offer_sql = cursor.fetchall()

        full_offer_list = []
        for row in cursor.execute('SELECT number_offer, vacancy, region, skill FROM full_offer ORDER BY number_offer'):
            full_offer_list.append(row)
#заполняем базу нашей модели
        for reg in region_sql:
            region1 = Region.objects.create(name=reg[0])

        for ski in skills_sql:
            skills1 = Skills.objects.create(name=ski[0])

        for vac in vacancy_sql:
            vacancy1 = Vacancy.objects.create(name=vac[0])

        for num in number_offer_sql:
            number_offer1 = NumberOffer.objects.create(name=num[0])

        for ful in full_offer_list:
        full_offer1 = FullOffer.objects.all()
        print(full_offer1)

        full_offer1.update(numberOffer=ful[0], VACANCY=ful[1], REGION=ful[2], SKILLS=ful[3])
        for ful in full_offer_list:
            number1 = NumberOffer.objects.get(id=ful[0])
            vacancy1 = Vacancy.objects.get(id=ful[1])
            region1 = Region.objects.get(id=ful[2])
            skills1 = Skills.objects.get(id=ful[3])

            full1 = FullOffer(numberOffer=number1, VACANCY=vacancy1, REGION=region1, SKILLS=skills1)

            full1.save()
