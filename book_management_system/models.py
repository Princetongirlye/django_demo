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


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=255, null=False, unique=True)
    # 告诉ORM author 和 book 多对多的关联关系
    # orm 自动生成第三张表
    book = models.ManyToManyField(to=Book)

    class Meta:
        db_table = 't_author'

    def __str__(self):
        return "<Author Object:{}>".format(self.author_name)


# class Author_Book(models.Model):
#     id = models.AutoField(primary_key=True)
#     author_id = models.ForeignKey(to=Author, on_delete=None)
#     book_id = models.ForeignKey(to=Book, on_delete=None)
#
#     class Meta:
#         db_table = "t_author_book"
