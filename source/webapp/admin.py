from django.contrib import admin
from .models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'created_at')
    list_display_links = ('pk', 'text')
    search_fields = ('text',)


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
