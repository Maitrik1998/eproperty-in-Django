#!/usr/bin/python -tt
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.

class Property(models.Model):


    iams = [
        ('Owner', 'Owner'),
        ('Dealer', 'Dealer'),
        ]

    propertytype = [
        ('Bunglow', 'Bunglow'),
        ('Flat', 'Flat'),
        ]

    propertysfor = [
        ('Sell','Sell'),
        ('Rent','Rent'),
        ]
        

    Areas = [
        ('Bopal', 'Bopal'),
        ('Thaltej', 'Thaltej'),
        ]

    BHK = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('Other', 'Other'),
        ]

    Meter = [
        ('Vaar', 'Vaar'),
        ('sq_ft', 'sq_ft'),
        ]

    Furnished=[
        ('Non-Furnished', 'Non-Furnished'),
        ('Semi-Furnished', 'Semi-Furnished'),
        ('Fully-Furnished','Fully-Furnished'),

        ]

    Age=[
        ('less than 1 year', 'less than 1 year'),
        ('Between 1-5 years', 'Between 1-5 years'),
        ('Between 6-10 years','Between 6-10 years'),
        ('More than 10 years', 'More than 10 years'),
        ]
 

        

    useremail=models.EmailField() 
    pid=models.AutoField(primary_key=True)

    Iam=models.CharField(
                max_length=10,
                choices=iams,
                default='Owner',
        )

    ptype=models.CharField(
                max_length=10,
                choices=propertytype,
                default='Flat',
        )
    pfor=models.CharField(
                max_length=5,
                choices=propertysfor,
                default='Sell',
        )

    Buildname=models.CharField(max_length=100)
    
    Adress=models.CharField(max_length=200)
    
    Area=models.CharField(
                max_length=9,
                choices=Areas,
                default='Bopal',
        )
    
    bhk=models.CharField(
                max_length=7,
                choices=BHK,
                default='Other',
        )

    Superbuildup=models.IntegerField()
    buildup=models.IntegerField()
    
    meter=models.CharField(
                max_length=5,
                choices=Meter,
                default='sq_ft',
        )
    
    addmore=models.TextField(max_length=1000)
    furnished=models.CharField(
                max_length=20,
                choices=Furnished,
                default='Non-Furnished',
        )

    pfloor=models.IntegerField()
    tfloor=models.IntegerField()
    cparkinng=models.BooleanField()
    oparkinng=models.BooleanField()
    age=models.CharField(
                max_length=19,
                choices=Age,
                default='Between 6-10 years',
        )
    price=models.CharField(max_length=100)
    nego=models.BooleanField()
    cname=models.CharField(max_length=100)  
    cemail=models.EmailField()  
    mobile=models.CharField(max_length=15)
    image=models.ImageField(upload_to ='uploads/')
    image2=models.ImageField(upload_to ='uploads/')
    image3=models.ImageField(upload_to ='uploads/')
    image4=models.ImageField(upload_to ='uploads/')


    class Meta:  
        db_table = "propertys"


