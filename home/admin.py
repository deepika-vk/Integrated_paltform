# admin.py
from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'created_at')  # Make sure these fields exist in your model
    search_fields = ('name', 'email', 'mobile')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
