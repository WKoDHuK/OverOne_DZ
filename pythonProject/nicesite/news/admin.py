from django.contrib import admin

from.models import News, Category



class NewsAdmin(admin.ModelAdmin):   #колонки добалвяем на сайте
    list_display = ('id', 'title', 'category', 'created_at', 'update_at', 'photo', 'is_published')
    list_display_links = ('id', 'title') #кликабельность сделали
    search_fields = ('title', 'content') #создает поисковую строку
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')



class CategoryAdmin(admin.ModelAdmin):   #колонки добалвяем на сайте
    list_display = ('id', 'title')
    list_display_links = ('id', 'title') #кликабельность сделали
    search_fields = ('title',) #создает поисковую строку


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

# Register your models here.
