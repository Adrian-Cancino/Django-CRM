from django.contrib import admin

from .models import User, Lead, Agent

# Register your models here to apear in the admin page

admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
