def add1(a, b):
    ''' add1 '''
    return a+b


def add2(a, b):
    ''' add2 '''
    result = a+b
    return result


a = add1(3, 4)
b = add2(3, 4)

print(add1(4, 5))
print(b)

# dwntjr


def add_many(*args):
    ''' add_many '''
    result = 0
    for i in args:
        result += i
    return result


ab = add_many()


def add_mul(choice, *args):
    ''' add_mul '''
    result = 0
    if choice == "add":
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result


print(add_mul(4, 5))


def ServiceStatusChart(request):
    days_a = now.weekday()
    # 담당자 정보 제공
    instance_info = instance_list.objects.all().order_by('esm_code')
    if request.GET.get('vip'):
        get_instance_vip = request.GET['vip']
    elif request.POST.get('vip'):
        get_instance_vip = request.POST['vip']
    else:
        template='owfs/owfs_chart.html'
        context={'instance_info': instance_info}
        return render(request, template, context)