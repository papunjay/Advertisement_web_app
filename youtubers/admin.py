from django.contrib import admin
from .models import Youtuber
# Register your models here.
class ytAdmin(admin.ModelAdmin):
    list_display=('id','name','sub_count','is_featured')
    search_fields=('name','camera_type')
    list_filter=('city','camera_type')
    list_display_links=('id','name')
    list_editable=('is_featured',)

admin.site.register(Youtuber,ytAdmin)
