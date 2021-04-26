from django.contrib import admin
from .models import Orders,Merchant,District,Division,SubDistrict

class DistrictInline(admin.TabularInline):
    model = District
class SubDistrictInline(admin.TabularInline):
    model = SubDistrict
class DivisionAdmin(admin.ModelAdmin):
    inlines = [
        DistrictInline

    ]
class DistrictAdmin(admin.ModelAdmin):
    inlines = [
        SubDistrictInline

    ]


# Register your models here.
admin.site.register(Orders)
admin.site.register(Merchant)
admin.site.register(Division,DivisionAdmin)
admin.site.register(District,DistrictAdmin)
admin.site.register(SubDistrict)