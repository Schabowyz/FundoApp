from django.contrib import admin

from .models import Connection, Notification

# Register your models here.
admin.site.register(Connection)
admin.site.register(Notification)