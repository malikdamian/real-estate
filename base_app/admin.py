from django.contrib import admin
from base_app.models import *


@admin.register(Apartament)
class AdminApartament(admin.ModelAdmin):
    pass


@admin.register(Home)
class AdminHome(admin.ModelAdmin):
    pass


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass


@admin.register(Level)
class AdminLevel(admin.ModelAdmin):
    pass


@admin.register(FloorsHome)
class AdminFloorsHome(admin.ModelAdmin):
    pass


@admin.register(Furniture)
class AdminFurniture(admin.ModelAdmin):
    pass


@admin.register(NumberRooms)
class AdminNumberRooms(admin.ModelAdmin):
    pass


@admin.register(Type)
class AdminType(admin.ModelAdmin):
    pass
