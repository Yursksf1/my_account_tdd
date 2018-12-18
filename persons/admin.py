from django.contrib import admin
from persons.models import owner


class OwnerAdmin(admin.ModelAdmin):
	list_display = ('id','user', 'name', 'notes', 'active_notifications')

admin.site.register(owner, OwnerAdmin)
