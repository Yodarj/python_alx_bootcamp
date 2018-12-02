from django.contrib import admin
from maf.models import Math
# Register your models here.


class MathAdmin(admin.ModelAdmin):
    list_display = ['func', 'l1', 'l2']
    search_fields = ['func']


admin.site.register(Math, MathAdmin)