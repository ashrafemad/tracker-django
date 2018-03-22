from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from tracker.forms import UserAllData
from tracker.models import Entry


class AuthorizedUserOrAdmin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        data = super().get_queryset()
        # filtering with user
        if not self.request.user.is_staff:
            data = data.filter(user=self.request.user)
        # filtering with date
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        if start_date and end_date:
            data = data.filter(date__gte=start_date, date__lte=end_date)
        # Weekly report
        if self.request.GET.get('week'):
            data = data.filter(date__range=(date.today()-timedelta(days=7), date.today()))
        return data


class AdminOnly(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return HttpResponseRedirect(reverse('index'))
        return super().dispatch(request, *args, **kwargs)


class Signup(CreateView):
    model = User
    form_class = UserAllData
    success_url = '/login/'


class Login(LoginView):
    model = User
    template_name = 'auth/login.html'


class MyEntries(AuthorizedUserOrAdmin, ListView):
    model = Entry


class CreateEntry(AuthorizedUserOrAdmin, CreateView):
    model = Entry
    fields = ('user', 'date', 'time', 'distance')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method in ('POST', 'PUT'):
            data = kwargs['data']
            data._mutable = True
            data['user'] = self.request.user.id
            kwargs['data'] = data
        return kwargs


class DeleteEntry(AuthorizedUserOrAdmin, DeleteView):
    model = Entry
    success_url = '/entries/'


class UpdateEntry(AuthorizedUserOrAdmin, UpdateView):
    model = Entry
    fields = ('date', 'distance', 'time')
    success_url = '/entries/'


class ListUsers(AdminOnly, ListView):
    model = User


class DeleteUser(AdminOnly, DeleteView):
    model = User
    success_url = '/users/'


class UpdateUser(AdminOnly, UpdateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'is_staff')
    success_url = '/users/'


def signout(request):
    logout(request)
    return render(request, 'main.html')


def index(request):
    return render(request, 'main.html')