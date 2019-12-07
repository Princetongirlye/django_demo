from django.shortcuts import HttpResponse, render,redirect
from . import models


def books_list(request):
    # 去数据库中查询所有的书籍
    all_books_list  = models.Book.objects.all()
    # 在HTML页面完成字符串替换
    return render(request,"book_management_system/books_list.html",{"books":all_books_list})


def add_book(request):
    publishers = models.Publisher.objects.all()

    if request.method == "POST":
        new_book_name = request.POST.get("book_name")
        new_publisher_id = request.POST.get("publisher")
        print(request.POST)
        models.Book.objects.create(book_name=new_book_name, publisher_id_id=new_publisher_id)
        # 用出版社对象创建
        # publisher_obj = models.Publisher.objects.get(id=new_publisher_id)
        # models.Book.objects.create(publisher_id=publisher_obj)
        return redirect("/book_management_system/books_list")

    return render(request, "book_management_system/add_book.html", {"publishers": publishers})


def edit_book(request):
    print(request.POST)
    if request.method == "POST":
        edit_id = request.POST.get("id", None)
        edit_book_name = request.POST.get("book_name")
        edit_publisher_id = request.POST.get("publisher")
        edit_book = models.Book.objects.get(id=edit_id)
        edit_book.book_name = edit_book_name
        edit_book.publisher_id = edit_publisher_id
        if edit_book_name:
            edit_book.save()
            return redirect("/book_management_system/books_list")
        else:
            return HttpResponse("不可为空")

    elif request.method == "GET":
        id = request.GET.get("id", None)
        if id:
            curr_book = models.Book.objects.get(id=id)
            publishers = models.Publisher.objects.all()
            return render(
                request,
                "book_management_system/edit_book.html",
                {"book": curr_book, "publishers": publishers})


def delete_book(request):
    del_id = request.GET.get("id", None)

    if del_id:
        del_obj = models.Book.objects.get(id=del_id)
        del_obj.delete()
        return redirect("/book_management_system/books_list")
    return HttpResponse("删除的数据不存在")
