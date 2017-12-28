from django.http import HttpResponse

from TestModel.models import Test

# def testdb(request):
#     test1 = Test(name='runoob')
#     test1.save()
#     return HttpResponse("<p>数据添加成功！</p>")

# 数据库操作
def testdb(request):
    # 初始化
    response1 = ""
    response2 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list1 = Test.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    list2 = Test.objects.filter(id=1)

    # 获取单个对象
    list3 = Test.objects.get(id=1)
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]

    #数据排序
    Test.objects.order_by("id")

    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")
    test1 = Test.objects.get(id=1)
    test1.name = 'Google'
    test1.save()

    # 输出所有数据
    for var in list1:
        response1 += var.name + " "
    for var in list2:
        response2 += var.name + " "
    response3 = list3.name
    return HttpResponse("<p>" + response1 + "</p>" + '\n' +
                        "<p>" + response2 + "</p>" + '\n' +
                        "<p>" + response3 + "</p>" + '\n' +
                        "<p>" + str(list3.__class__) + '\n' +
                        "<p>" + str(type(list3)) + "</p>" + '\n' +
                        "<p>" + test1.name + "</p>" + '\n'
    )