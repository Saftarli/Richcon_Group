from django.contrib import admin
from core.models import *


# Register your models here.
@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parameter', 'description', 'updated_date', 'created_date')
    search_fields = ('name', 'parameter', 'description',)

    class Meta:
        model = GeneralSetting
