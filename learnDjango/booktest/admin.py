from django.contrib import admin

# Register your models here.
from .models import * #python3引入
#from models import * #python2引入
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date'] #要显示的表的字段
    search_fields = ['btitle']
    list_per_page = 10
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)
