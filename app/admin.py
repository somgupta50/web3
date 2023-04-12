from django.contrib import admin
from .models import Feedback
from .models import Contact

# Register your models here.

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    '''Admin View for Feedback'''
    list_display = ('name', 'email', 'rating', 'message')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    '''Admin View for Contact'''
    list_display = ('name', 'email', 'mobile', 'subject')
