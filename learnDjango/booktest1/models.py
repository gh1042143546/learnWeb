from django.db import models

# Create your models here.

class BookInfoManager(models.Manager):#自定义管理器类
    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)

class BookInfo(models.Model):#模型类去使用必须继续models.Model，才能用对象去操作数据库
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    boots2 = BookInfoManager()#调用自定义管理器类
    #class Meta:定义元类
        #db_table='bookinfo'#定义表的名称
class HeroInfo(models.Model):
    hhname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    hbook = models.ForeignKey(BookInfo)#定义外键