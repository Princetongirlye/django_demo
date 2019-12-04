from django.shortcuts import render, redirect,HttpResponse
from book_management_system import models

# Create your views here.


# 展示出版社列表
def publisher_list(request):
    ret = models.Publisher.objects.all().order_by("id")
    return render(request, "book_management_system/publisher_list.html", {'publisher_list': ret})


# 增加出版社
def add_publisher(request):
    error_msg = ""

    # 用户第一次来
    if request.method == 'POST':

        name = request.POST.get('publisher_name')
        if name:
            models.Publisher.objects.create(name=name)
            return redirect("/book_management_system/")
        else:
            error_msg = "出版社名字不能为空"
    return render(request, "book_management_system/add_publisher.html",{"error":error_msg})


# 删除
def delete_publisher(request):
    del_id = request.GET.get("id", None)
    print(request.GET)
    if del_id:
        del_obj = models.Publisher.objects.get(id=del_id)
        del_obj.delete()
        return redirect("/book_management_system/publisher")
    else:
        return HttpResponse("要删除的数据不存在")


def edit_publisher(request):
    # 获取当前编辑的出版社对象

    print(request.GET)
    if request.method == "POST":
        new_name = request.POST.get("publisher_name")
        id = request.POST.get("id")
        edit_publisher = models.Publisher.objects.get(id=id)
        edit_publisher.name = new_name
        if new_name:
            edit_publisher.save()
            return redirect("/book_management_system/publisher")
        else:
            return HttpResponse("不可为空")
    id = request.GET.get("id")
    if id:
        publisher_cur_obj = models.Publisher.objects.get(id=id)
        return render(request, 'book_management_system/edit_publisher.html', {"publisher": publisher_cur_obj})

