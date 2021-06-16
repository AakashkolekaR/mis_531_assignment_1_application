from django.contrib import admin
from .models import Job
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ['job_id','job_title','min_salary','max_salary']
    list_filter = ['job_title','min_salary','max_salary']
    search_fields = ['job_title','min_salary','max_salary']

admin.site.register(Job, JobAdmin)
admin.site.site_header = "MIS531"
admin.site.site_title = "MIS531"
admin.site.index_title = "MIS531"