from django.db import models

# Create your models here.

# 图书管理系统 书 作者 出版社


class Publisher(models.Model):
    # 自增的ID主键
    id = models.AutoField(primary_key=True)
    # 创建唯一不为空的字段 出版社名字
    name = models.CharField(max_length=64, null=False, unique=True)

    addr = models.CharField(max_length=128, default="无地址")

    class Meta:
        db_table = "t_publisher"


class Book(models.Model):
    # 自增的主键
    id = models.AutoField(primary_key=True)
    # 书名 不能为空 不能重复
    book_name = models.CharField(max_length=255, null=False, unique=True)
    # 和出版社关联的外键字段
    publisher_id = models.ForeignKey(to=Publisher, on_delete=None)

    class Meta:
        db_table = 't_book'


