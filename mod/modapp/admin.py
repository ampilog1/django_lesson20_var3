from django.contrib import admin
from .models import Region, Vacancy, Skills, NumberOffer, FullOffer
# Register your models here.

admin.site.register(Region)
admin.site.register(Vacancy)
admin.site.register(Skills)
admin.site.register(NumberOffer)
admin.site.register(FullOffer)