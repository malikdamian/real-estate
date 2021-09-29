"""RealEstate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from base_app import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('category/', views.CategoryView.as_view()),
    path('category/<int:cat_id>/type/<int:type_id>', views.AdvView.as_view()),
    path('category/<int:id>', views.TypeOffertsView.as_view()),
    path('add_advertisement/', views.AddAdvertisement.as_view()),
    path('add/<int:cat_id>', views.AddAdvView.as_view()),
    path('offer/<int:id>', views.OfferView.as_view()),
    path('search/', views.SearchView.as_view()),
    path('search/', views.SearchView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogOutView.as_view()),
    path('registration/', views.RegistrationView.as_view()),
    path('deloffer/<int:id>/', views.RemoveOffer.as_view()),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)