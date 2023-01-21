from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


@user_passes_test(lambda u: u.is_superuser)
def post(request, id):
    fulls = FullOffer.objects.get(id=id)
    return render(request, 'modapp/post.html', context={'fulls': fulls})


@login_required
def create_post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'modapp/create.html', context={'form': form})
    else:
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('mod:index'))
        else:
            return render(request, 'modapp/create.html', context={'form': form})


class RegionListView(ListView):
    model = Region
    template_name = 'region_list.html'
    context_object_name = 'regions'

    def get_context_data(self, *args, **kwargs):
        """
        Отвечает за передачу параметров в контекст
        :param args:
        :param kwargs:
        :return:
        """
        context = super().get_context_data(*args, **kwargs)
        context['name'] = 'Регионы'
        return context


class FullDetailView(DetailView):
    model = FullOffer
    template_name = 'modapp/full_detail.html'

    def get_context_data(self, *args, **kwargs):
        """
        Отвечает за передачу параметров в контекст
        :return:
        :param args:
        :param kwargs:
        :return:
        """
        context = super().get_context_data(*args, **kwargs)
        context['name'] = 'Регионы'
        return context


class RegionCreateView(LoginRequiredMixin, CreateView):
    model = Region
    fields = '__all__'
    success_url = reverse_lazy('mod:region_list')
    template_name = 'modapp/region_create.html'

    def form_valid(self, form):
        """
        Метод срабатывает после того как форма валидна
        :param form:
        :return:
        """
        # self.request.user - текущий пользователь
        form.instance.user = self.request.user
        return super().form_valid(form)


class RegionUpdateView(UpdateView):
    model = Region
    fields = '__all__'
    success_url = reverse_lazy('mod:region_list')
    template_name = 'modapp/region_create.html'


class RegionDeleteView(DeleteView):
    template_name = 'modapp/region_delete_confirm.html'
    model = Region
    success_url = reverse_lazy('mod:region_list')
