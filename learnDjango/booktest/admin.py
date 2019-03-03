from django.contrib import admin

# Register your models here.
from .models import * #python3引入
#from models import * #python2引入
class HeroInfoInline(admin.TabularInline):#以表格方式嵌套关系
    model = HeroInfo #要嵌套的类
    extra = 2 #一次嵌套几个

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date'] #要显示的表的字段
    search_fields = ['btitle']
    list_per_page = 10
    inlines = [HeroInfoInline]#BookInfoAdmin里嵌套HeroInfoInline
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)
