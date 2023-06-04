from django.contrib import admin
from .models import *
# Register your models here.

class TagTublerInline(admin.TabularInline):
    model = Tag
    
class PostAdmin(admin.ModelAdmin):
    inlines = [TagTublerInline]

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)