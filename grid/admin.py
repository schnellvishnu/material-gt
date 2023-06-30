from django.contrib import admin
from.models import Data_tbl
# Register your models here.
class Data_tblAdmin(admin.ModelAdmin):
    list_display =('name','age','address')
admin.site.register(Data_tbl,Data_tblAdmin)