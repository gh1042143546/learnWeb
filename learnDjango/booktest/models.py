from django.db import models

# Create your models here.
class BookInfo(models.Model):#模型类去使用必须继续models.Model，才能用对象去操作数据库
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    def __str__(self):
        #return self.btitle.encode('utf-8')
        return self.btitle #pythn3写法s
class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo)#定义外键
    def __str__(self):
        #return self.hname.encode('utf-8')  #用admin进行后台进行表添加数据时展示的文字
        return self.hname


