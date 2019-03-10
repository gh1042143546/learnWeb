from django.db import models

# Create your models here.

class BookInfoManager(models.Manager):#�Զ����������
    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)

class BookInfo(models.Model):#ģ����ȥʹ�ñ������models.Model�������ö���ȥ�������ݿ�
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    boots2 = BookInfoManager()#�����Զ����������
    #class Meta:����Ԫ��
        #db_table='bookinfo'#����������
class HeroInfo(models.Model):
    hhname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    hbook = models.ForeignKey(BookInfo)#�������