from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','username','is_active','last_login','date_joined')
    list_display_links=('email','first_name','last_name')
    readonly_fields=('last_login','date_joined')
    ordering=('-date_joined',)
    filter_horizontal=()
    list_filter=()
    fieldsets=()

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display=('category_name','slug')


class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','price','date_created','stock','is_available')
    prepopulated_fields={'slug':('product_name',)}
admin.site.register(Category,CategoryAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(Product,ProductAdmin)
