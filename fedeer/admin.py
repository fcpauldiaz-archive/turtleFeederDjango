from django.contrib import admin
from fedeer.models import EventoFeed
# Register your models here.

class EventoFeedAdmin(admin.ModelAdmin):
	list_display=('fecha')
	search_fields=['fecha']
	class Meta:
		model = EventoFeed

admin.site.register(EventoFeed)
