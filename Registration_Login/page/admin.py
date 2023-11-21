from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','username','email')

   

admin.site.register(Page,PageAdmin)