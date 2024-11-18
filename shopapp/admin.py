from django.contrib import admin

from .models import Category, ShopPost,Condition

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class ShopPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class ConditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')




    

admin.site.register(Category, CategoryAdmin)
admin.site.register(ShopPost, ShopPostAdmin)
admin.site.register(Condition, ConditionAdmin)



