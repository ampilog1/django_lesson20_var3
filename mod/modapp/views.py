from django.shortcuts import render, HttpResponseRedirect
from .models import FullOffer, Region
from .forms import ContactForm, PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy


# Create your views here.
def main_view(request):
    fulls = FullOffer.objects.all()
    return render(request, 'modapp/index.html', context={'fulls': fulls})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Получить данные из форы
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            send_mail(
                'Contact message',
                f'Ваш сообщение {message} принято',
                'from@example.com',
                [email],
                fail_silently=True,
            )

            return HttpResponseRedirect(reverse('mod:index'))
        else:
            return render(request, 'modapp/contact.html', context={'form': form})
    else:
        form = ContactForm()
    return render(request, 'modapp/contact.html', context={'form': form})

def post(request, id):
    fulls = FullOffer.objects.get(id=id)
    return render(request, 'modapp/post.html', context={'fulls': fulls})

def create_post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'modapp/create.html', context={'form': form})
    else:
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mod:index'))
        else:
            return render(request, 'modapp/create.html', context={'form': form})

class RegionListView(ListView):
    model = Region
    template_name = 'region_list.html'
    context_object_name = 'regions'

class FullDetailView(DetailView):
    model = FullOffer
    template_name = 'modapp/full_detail.html'

class RegionCreateView(CreateView):
    model = Region
    fields = '__all__'
    success_url = reverse_lazy('mod:region_list')
    template_name = 'modapp/region_create.html'

class RegionUpdateView(UpdateView):
    model = Region
    fields = '__all__'
    success_url = reverse_lazy('mod:region_list')
    template_name = 'modapp/region_create.html'

class RegionDeleteView(DeleteView):
    template_name = 'modapp/region_delete_confirm.html'
    model = Region
    success_url = reverse_lazy('mod:region_list')