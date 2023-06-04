
# Register your models here.
from django.contrib import admin
from . import models

from .models import StargEntertainment,Section

class AuthorAdminStarg(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title']}
    list_display = ['title','content','image','event']
    
admin.site.register(models.StargEntertainment, AuthorAdminStarg)
admin.site.register(Section)