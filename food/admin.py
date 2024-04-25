from django.contrib import admin
from .models import *

# Register your models here.
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name','description','price',)
admin.site.register(FoodItem,FoodItemAdmin)

admin.site.register(Profile)