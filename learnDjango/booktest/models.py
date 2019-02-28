from django.db import models

# Create your models here.
class BookInfo(models.Model):#模型类去使用必须继续models.Model，才能用对象去操作数据库
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo)#定义外键
    #cehsi



