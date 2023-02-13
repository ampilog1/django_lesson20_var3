from django.core.management.base import BaseCommand, CommandError
from mixer.backend.django import mixer

from modapp.models import Region, Vacancy, Skills, NumberOffer, FullOffer
from userapp.models import BlogUser


class Command(BaseCommand):
    mixer.blend()
    def handle(self, *args, **options):
        Region.objects.all().delete()
        Vacancy.objects.all().delete()
        Skills.objects.all().delete()
        NumberOffer.objects.all().delete()
        FullOffer.objects.all().delete()
        BlogUser.objects.filter(is_superuser=False).delete()

        count = 10
        for i in range(count):
            p = (i / count) * 100
            print(f'{i}) {p} %')
            mixer.blend(Region)

        print('end')
