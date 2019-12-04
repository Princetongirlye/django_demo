from django.db import models

# Create your models here.

# 图书管理系统 书 作者 出版社


class Publisher(models.Model):
    # 自增的ID主键
    id = models.AutoField(primary_key=True)
    # 创建唯一不为空的字段 出版社名字
    name = models.CharField(max_length=64, null=False, unique=True)

