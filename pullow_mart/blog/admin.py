from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
#Register your models here.



class CategorieArticleAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add', 'date_update', 'status', 'image_view')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add" 
    list_display_links = ["nom"]
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [
                ("Info CategorieArticle", {"fields":['nom', 'image', 'description']}),
                ("Standard", {"fields":['status']})
                ]
    def image_view(self,obj):
        return mark_safe('<img src="{url}" width=100 height=50>'.format(url=obj.image.url))

def _register(model,admin_class):
    admin.site.register(model, admin_class) 




_register(models.CategorieArticle, CategorieArticleAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add', 'date_update', 'status', 'image_view')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add" 
    list_display_links = ["nom"]
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [
                ("Info Article", {"fields":['nom', 'image', 'description']}),
                ("Standard", {"fields":['status']})
                ]

