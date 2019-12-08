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
