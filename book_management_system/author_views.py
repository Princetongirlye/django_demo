from django.shortcuts import HttpResponse, redirect, render
from . import models


def add_author(request):
    if request.method == "POST":
        author = request.POST.get("author")
        # 多选
        books = request.POST.getlist("books")

        if author and books:
            new_author_obj = models.Author.objects.create(author_name=author)
            # 把新作者和书籍建立对应关系
            new_author_obj.book.set(books)
            return redirect("/book_management_system/authors_list")
        else:
            return HttpResponse("不能为空！")
    books = models.Book.objects.all()
    return render(request,
                  "book_management_system/add_author.html",
                  {"books_list": books})


def authors_list(request):
    authors = models.Author.objects.all()
    return render(request,
                  "book_management_system/authors_list.html",
                  {"authors": authors})


def delete_author(request):
    del_id = request.GET.get("id")
    if del_id:
        del_obj = models.Author.objects.get(id=del_id)
        del_obj.delete()
        return redirect("/book_management_system/authors_list")
    return HttpResponse("删除的数据不存在")


def edit_author(request):

    if request.method == "POST":
        edit_id = request.POST.get("id")
        new_author = request.POST.get("author")
        # 关联的书籍信息
        new_books = request.POST.getlist("books")

        if new_author and new_books:
            new_author_book = models.Author.objects.get(id=edit_id)
            new_author_book.author_name = new_author
            # 更新作者关联的书的对应关系
            new_author_book.book.set(new_books)
            # 提交到数据库
            new_author_book.save()
        return redirect("/book_management_system/authors_list")

    # 从URL里面取要编辑作者的id
    edit_id = request.GET.get("id")
    print("edit_id = ", edit_id)
    edit_author_obj = models.Author.objects.get(id=edit_id)
    books = models.Book.objects.all()
    return render(request
                  ,"book_management_system/edit_author.html"
                  ,{"books_list": books,"author": edit_author_obj})

















