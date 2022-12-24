from django.shortcuts import render
from .models import FullOffer


# Create your views here.
def main_view(request):
    fulls = FullOffer.objects.all()
    return render(request, 'modapp/index.html', context={'fulls': fulls})
