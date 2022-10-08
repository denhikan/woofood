from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_show', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', )
    prepopulated_fields = {'slug': ('title',)}

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' style='width:100px'/>".format(obj.image.url))
        return "None"

    image_show.__name__ = "Картинка"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size)
admin.site.register(Weight)


