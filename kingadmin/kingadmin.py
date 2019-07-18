from kingadmin import models
from kingadmin.site import BaseAdmin,site
# Register your models here.
class CustomerAdmin(BaseAdmin):
    list_display = ['name','id','role']
    search_key=['name',]
    list_filter=['role',]

site.register(models.Role)
site.register(models.Customer,CustomerAdmin)
