from django.contrib import admin

# Register your models here.
from .models import * #python3����
#from models import * #python2����
class HeroInfoInline(admin.TabularInline):#�Ա��ʽǶ�׹�ϵ
    model = HeroInfo #ҪǶ�׵���
    extra = 2 #һ��Ƕ�׼���

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date'] #Ҫ��ʾ�ı���ֶ�
    search_fields = ['btitle']
    list_per_page = 10
    inlines = [HeroInfoInline]#BookInfoAdmin��Ƕ��HeroInfoInline
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)
