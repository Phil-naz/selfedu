from django.contrib import admin

from .models import *                            # импорт для отображения в админке

class WomenAdmin(admin.ModelAdmin):               #дополнительные поля в админке
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', )
    search_fields = ('title', 'content')
    list_editable = ('is_published', 'title')             # изменяемые в админке поля
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}  # автоматическое формирование slug в админке

class CategoryAdmin(admin.ModelAdmin):              #дополнительные поля в админке
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',) # запятая обязательно тк кортеж!!!
    prepopulated_fields = {"slug": ("name",)}   # автоматическое формирование slug в админке

admin.site.register(Women, WomenAdmin)                       # импорт для отображения в админке
admin.site.register(Category, CategoryAdmin)
