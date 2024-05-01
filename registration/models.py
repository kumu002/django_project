from django.db import models


class User_roles(models.Model):
    roles = models.CharField(max_length=100)


class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.IntegerField(max_length=11, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='static/images', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    role = models.ForeignKey(User_roles, on_delete=models.CASCADE)


class Location(models.Model):
    loc_name = models.CharField(max_length=200)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)


class Parking_places(models.Model):
    car_slot = models.IntegerField()
    bike_slot = models.IntegerField()
    satuts = models.BooleanField(default=True)
    role = models.ForeignKey(User_roles, on_delete=models.CASCADE)


class Payment(models.Model):
    pay_amount = models.IntegerField()


class Rent(models.Model):
    amount = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    role = models.ForeignKey(User_roles, on_delete=models.CASCADE)
    parking = models.ForeignKey(Parking_places, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
