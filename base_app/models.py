from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=12, null=True)

    def __str__(self):
        return self.name


class Level(models.Model):
    level = models.CharField(max_length=20)

    def __str__(self):
        return self.level


class FloorsHome(models.Model):
    floor = models.CharField(max_length=20)

    def __str__(self):
        return self.floor


class Furniture(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class NumberRooms(models.Model):
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number


class Type(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type


class TypePlot(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type


class TypeOffice(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type


class TypeOfferts(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RealEstate(models.Model):
    title = models.CharField(max_length=70, verbose_name='Tytuł')
    type_offerts = models.ForeignKey(TypeOfferts, on_delete=models.CASCADE, verbose_name='Rodzaj oferty')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoria')
    price = models.FloatField(verbose_name='Cena')
    area = models.FloatField(verbose_name='Powierzchnia')
    description = models.TextField(verbose_name='Opis')
    photos = models.ImageField(blank=True, null=True, verbose_name='Dodaj zdjęcia')
    location = models.CharField(max_length=50, verbose_name='Lokalizacja')
    create_date = models.DateTimeField(auto_now_add=True, null=True)


class Apartament(RealEstate):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Rodzaj zabudowy')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name='Poziom')
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE, verbose_name='Umeblowanie')
    number_room = models.ForeignKey(NumberRooms, on_delete=models.CASCADE, verbose_name='Liczba pokoi')


class Home(RealEstate):
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE, verbose_name='Umeblowanie')
    parcel_area = models.FloatField(verbose_name='Powierzchnia działki')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Rodzaj zabudowy')
    floor = models.ForeignKey(FloorsHome, on_delete=models.CASCADE, verbose_name='Liczna pięter')


class Plot(RealEstate):
    type = models.ForeignKey(TypePlot, on_delete=models.CASCADE, verbose_name='Rodzaj')


class Office(RealEstate):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name='Poziom')
    type = models.ForeignKey(TypeOffice, on_delete=models.CASCADE, verbose_name='Przeznaczenie lokalu')


class Garage(RealEstate):
    pass


class Magazine(RealEstate):
    pass


class Other(RealEstate):
    pass
