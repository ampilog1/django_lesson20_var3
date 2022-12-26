from django.shortcuts import render
from .models import FullOffer


# Create your views here.
def main_view(request):
    fulls = FullOffer.objects.all()
    return render(request, 'modapp/index.html', context={'fulls': fulls})

def create_post(request):
    return render(request, 'modapp/create.html')

def post(request, id):
    fulls = FullOffer.objects.get(id=id)
    return render(request, 'modapp/create.html', context={'fulls': fulls})