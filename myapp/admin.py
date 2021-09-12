from django.contrib import admin
from myapp import models
# Register your models here.

admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.Fach)
admin.site.register(models.Library)
admin.site.register(models.Father)
admin.site.register(models.Author)
admin.site.register(models.Book)