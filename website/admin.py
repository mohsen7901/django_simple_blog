from django.contrib import admin
from website.models import Contact, Newsletter

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_date'
    list_display = ['id', 'name', 'email', 'subject', 'updated_date']
    list_filter = ['name', 'email']
    search_fields = ['subject']
    list_display_links = ['id', 'name']

class NewsletterAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['id', 'email', 'created_date']
    search_fields = ['email']
    list_display_links = ['id', 'email']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter, NewsletterAdmin)