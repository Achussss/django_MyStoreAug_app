from django.db import models
from django.contrib.auth.models import User
from django.core.validators import  MaxValueValidator,MinValueValidator

class Products(models.Model):

    name=models.CharField(unique=True,max_length=200)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    image=models.ImageField(null=True,upload_to="images")
    @property
    def avg_rating(self):
        ratings=self.reviews_set.all().values_list("rating",flat=True)
        if ratings:
            return sum(ratings)/len(ratings)
        else:
            return 0

    def __str__(self):
        return self.name


class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    options=(
        ("order-placed","order-placed"),
        ("in-cart","in-cart"),
        ("cancelled","cancelled")
    ) 
    status=models.CharField(max_length=200,choices=options,default="in-cart")

class Reviews(models.Model):

    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=208)


    def __str__(self):
        return self.comment



class Orders(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("order-placed","order-placed"),
        ("despathed","despatched"),
        ("in-transit","in-transit"),
        ("cancelled","cancelled")
    ) 
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    date=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=250)
    phone=models.CharField(max_length=20)     

#python manage.py makemigrations
#python manage.py migrate



 #ORM
#orm for creating a resourcse
#modelname.objects.create(field=value,field2=value2,,,,,)
#Products.objects.create(name='samsung72',price=32000,description="mobile",category="electronics")


#ORM query for fetching all records
#qs=modelname.objects.all()

#ORM filter queries
#qs=modelname.objects.filter(category="electronics")

#qs=products.objects.all().exclude(category="electronics")
#qs=modelname.objects.get(id=1)

#price>25000
#qs=Products.objects.filter(price__lt=25000) less than
#__lt <
#__lte <=
#__gt >
#__gte >=

#products in range of 20000 to 30000
#qs=products.objects.filter(price__gt=20000,price__gt=30000)


#return all categories
#Products.objects.values_list('category')








# Create your models here.
