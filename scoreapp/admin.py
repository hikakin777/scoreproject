from django.contrib import admin

from .models import Category, ScorePost,Condition

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class ScorePostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class ConditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')




    

admin.site.register(Category, CategoryAdmin)
admin.site.register(ScorePost, ScorePostAdmin)
admin.site.register(Condition, ConditionAdmin)



