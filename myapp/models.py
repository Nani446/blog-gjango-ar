from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Father(models.Model):
     name = models.CharField( unique=True , max_length=20 , null=True, db_column='namex')       
     age  = models.BigIntegerField( null=True , default=12)

     class Meta:
         #verbose_name = 'Father_Rena'
         db_table = 'Father_T'
         ordering = ['age']

     def __str__(self):
         return self.name
     


class Author(models.Model):
     name = models.CharField( unique=True , max_length=20 , null=True)       
     #age  = models.BigIntegerField( null=True , default=12)

     def __str__(self):
        return self.name

class Book(models.Model):
     name = models.CharField( unique=True , max_length=20 , null=True)       
     author = models.ForeignKey(Author , on_delete=models.CASCADE , null=1)
     created = models.DateTimeField(null=1 , default=timezone.now)

     def __str__(self):
        return self.name       
    
    


class Teacher(models.Model):
     name = models.CharField( unique=True , max_length=20 , null=True)       
     #age  = models.BigIntegerField( null=True , default=12)

     def __str__(self):
        return self.name

class Fach(models.Model):
     name = models.CharField( unique=True , max_length=20 , null=True)   
     price = models.IntegerField(null=1)
     #age  = models.BigIntegerField( null=True , default=12)

     def __str__(self):
        return self.name

class Library(models.Model):
     name = models.CharField( unique=True , max_length=20 , null=True)       
     

     def __str__(self):
        return self.name

class Student(models.Model):
    chosse = [
        ('male' , 'male'),
        ('fmale', 'fmale'),
        ('other', 'other')
          ]
    name = models.CharField(max_length=40 , null=True , blank=True , unique=True , help_text='Enter Your Name hier',
    db_column='Name_student',
    verbose_name= 'Name Student',
    editable=True,
    error_messages={'unique':'ياباشا بطل عبط'}
    
    )
    age = models.BigIntegerField( null=True , default=12)
    gender = models.CharField(null=True , max_length=10 , choices=chosse)
    agree = models.BooleanField(null=True)
    #Joind = models.DateField(null=True)
    #hour  = models.TimeField(null=True)
    created = models.DateTimeField(default=datetime.now , null=True)
    #dem     = models.DecimalField(null=True , decimal_places=2 , max_digits=4)
    emil    = models.EmailField(null=True , max_length=100)
    #files   = models.FileField(upload_to='myapp/upload', null=True)
    #img     = models.ImageField(upload_to='myapp/upload', null=True)
    #text    = models.TextField(null=True)
    Teacher_name = models.OneToOneField(Teacher , on_delete=models.CASCADE , null=True)
    Fach_name = models.ForeignKey(Fach , on_delete=models.CASCADE, null=True )
    Book     = models.ManyToManyField(Library )
    

    
    def __str__(self):
        return self.name

