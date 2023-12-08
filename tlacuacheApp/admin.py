from django.contrib import admin
from .models import Post

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("title", "date", "description",)
  
admin.site.register(Post, MemberAdmin)