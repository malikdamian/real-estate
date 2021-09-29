from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from base_app.models import *
from base_app.forms import LoginForm, RegistrationForm, SearchForm, addApartametForm, addHomeForm, \
    addPlotForm, addOfficeForm, addGarageForm, addMagazineForm, addOtherForm


def index(request):
    return render(request, 'base.html')


class CategoryView(View):

    def get(self,request):
        categories = Category.objects.all()
        return render(request, 'categories.html', {'categories': categories})


class AdvView(View):

    def get(self, request,cat_id,type_id):
        cat = Category.objects.get(pk=cat_id)
        offer_type= TypeOfferts.objects.get(pk=type_id)
        obj_lists = RealEstate.objects.all()
        if cat.id == 1:
            obj_lists = Apartament.objects.filter(type_offerts=offer_type).order_by('-id')
        elif cat_id == 2:
            obj_lists = Home.objects.filter(type_offerts=offer_type).order_by('-id')
        elif cat_id == 3:
            obj_lists = Plot.objects.filter(type_offerts=offer_type).order_by('-id')
        elif cat_id == 4:
            obj_lists = Office.objects.filter(type_offerts=offer_type).order_by('-id')
        elif cat_id == 5:
            obj_lists = Garage.objects.filter(type_offerts=offer_type).order_by('-id')
        elif cat_id == 6:
            obj_lists = Magazine.objects.filter(type_offerts=offer_type).order_by('-id')
        elif cat_id == 7:
            obj_lists = Other.objects.filter(type_offerts=offer_type)
        return render(request, 'adv.html', {'obj_lists': obj_lists})


class TypeOffertsView(View):

    def get(self, request, id):
        category = Category.objects.get(pk=id)
        types = TypeOfferts.objects.all()
        return render(request, 'type_offerts.html', {'types': types, 'category':category})


class OfferView(View):

    def get(self, request, id):
        offer = RealEstate.objects.get(pk=id)
        return render(request, 'offer.html', {'offer':offer})


class AddAdvertisement(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self,request):
        categories = Category.objects.all()
        return render(request, 'add_advertisement.html', {'categories': categories})


class AddAdvView(View):

    @staticmethod
    def get_form(cat_id):
        if cat_id == 1:
            return addApartametForm
        elif cat_id == 2:
            return addHomeForm
        elif cat_id == 3:
            return addPlotForm
        elif cat_id == 4:
            return addOfficeForm
        elif cat_id == 5:
            return addGarageForm
        elif cat_id == 6:
            return addMagazineForm
        elif cat_id == 7:
            return addOtherForm

    def get(self, request, cat_id):
        form_class = AddAdvView.get_form(cat_id)
        form = form_class()
        return render(request, 'addForm.html', {'form':form})

    def post (self, request, cat_id):
        form_class = AddAdvView.get_form(cat_id)
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'addForm.html', {'form':form})


class SearchView(View):

    def get(self, request):
        form = SearchForm()
        obj_lists = RealEstate.objects.all().order_by('-id')
        return render(request, 'search.html', {'form':form, 'obj_lists': obj_lists})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            obj_lists = RealEstate.objects.filter(title__icontains=title)
            form = SearchForm(initial={'title':title})
        else:
            print('Coś nie gra')
        return render(request,'search.html',{'obj_lists': obj_lists, 'form': form})


class RemoveOffer(PermissionRequiredMixin,View):
    permission_required = 'base_app.delete_offer'

    def post(self, request, id):
        offer = RealEstate.objects.get(pk=id)
        offer.delete()
        return redirect('/')


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                print("Nie udalo sie zalogowac")
            return redirect('/')


class LogOutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')


class RegistrationView(View):

    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            return redirect('/')
        return render(request, 'registration.html', {'form': form})
