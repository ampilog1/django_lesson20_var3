from django.shortcuts import render


# Create your views here.
def main_view(request):
    pass
    render(request, 'modapp/index.html', context={})