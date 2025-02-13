from django.contrib import admin
from rango.models import UserProfile
from rango.models import Category, Page 


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')  # Correct placement

admin.site.register(Page, PageAdmin)  # Register with ModelAdmin

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)

admin.site.register(UserProfile)
