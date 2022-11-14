from django.contrib import admin

# Register your models here.
from .models import RegisteredClient,ElectoralDataTable

admin.site.register(RegisteredClient)
admin.site.register(ElectoralDataTable)