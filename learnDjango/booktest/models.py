from django.db import models

# Create your models here.
class BookInfo(models.Model):#ģ����ȥʹ�ñ������models.Model�������ö���ȥ�������ݿ�
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo)#�������
    #cehsi



