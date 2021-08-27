from django.contrib import admin
from testapp.models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display=['title','content']
admin.site.register(Blog,BlogAdmin)
