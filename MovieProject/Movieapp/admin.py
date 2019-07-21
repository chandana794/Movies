from django.contrib import admin
from Movieapp.models import Movies

class MoviesAdmin(admin.ModelAdmin):
    list_display =['Release','MovieNmae','Hero','Heroine','Rating']
admin.site.register(Movies,MoviesAdmin)






# Register your models here.
