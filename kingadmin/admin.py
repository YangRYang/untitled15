from django.contrib import admin
from kingadmin import models
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','id','role']

admin.site.register(models.Role)
admin.site.register(models.Customer,CustomerAdmin)