from django.contrib import admin
from .models import *


class Subscriber_new(admin.ModelAdmin):
    #list_display = ['email','name']
    list_display = [field.name for field in Subscriber._meta.fields]
    #exclude = ["email"]
    fields =["name"]
    list_filter = ['email']
    search_fields = ['name']
    class Meta:
        model = Subscriber




admin.site.register(Subscriber, Subscriber_new)