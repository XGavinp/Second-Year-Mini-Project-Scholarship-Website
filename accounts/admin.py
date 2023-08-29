from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Profile)
admin.site.register(Eligibility)
admin.site.register(Gender)
admin.site.register(Course)
admin.site.register(Education)
#admin.site.register(Scholarship)
admin.site.register(Location)
admin.site.register(Language)
admin.site.register(Major)
admin.site.register(Accomodation)
admin.site.register(Living_Expense)
admin.site.register(Month)
admin.site.register(Year)
admin.site.register(s_data)
admin.site.register(Level)


 
@admin.register(Scholarship)
class MemberAdmin(ImportExportModelAdmin):
    list_display = ("uni_name", "major", "tuition_covered")
    pass