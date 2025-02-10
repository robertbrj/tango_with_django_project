from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'views', 'likes')  

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url') 
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

admin.site.register(UserProfile)
