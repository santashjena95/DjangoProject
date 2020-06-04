from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def hi(request):
    return render(request, 'hi.html', {'name':'Santash'})
def checking(request):
    return render(request, 'checking.html', {'name':'Santash'})
def add(request):
    return render(request, 'add.html', {'name': 'Santash'})
def result(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1 + val2
    return render(request, 'result.html', {'result': res, 'name': 'Santash'})
def tweet(request):
    return render(request, 'twitter.html', {'name': 'Santash'})
def twt_res(request):
    val1 = request.POST["twt1"]
    val2 = request.POST["twt2"]
    val3 = request.POST["twt3"]
    val4 = request.POST["twt4"]
    val5 = request.POST["twt5"]
    val6 = request.POST["twt6"]
    val7 = request.POST["twt7"]
    val8 = request.POST["twt8"]
    val9 = request.POST["twt9"]
    val10 = request.POST["twt10"]
    val = val1+" "+val2+" "+val3+" "+val4+" "+val5+" "+val6+" "+val7+" "+val8+" "+val9+" "+val10

    def fun_call(strg):
        if (strg[0] == "#"):
            return 0
        else:
            return 1

    def find(new_string, g):
        m = len(new_string)
        for i in range(0, m, 2):
            if (new_string[i] == g):
                return 0
        return 1

    def count_number(b, g, new_string, z):
        if (find(new_string, g)):
            c = 0
            for i in range(0, z):
                if (g == b[i]):
                    c = c + 1
            return (c)
        else:
            return 0

    def i_want_half_sort(new_string):
        q = len(new_string)
        for i in range(0, q, 2):
            for j in range(i + 2, q, 2):
                if (new_string[i] > new_string[j]):
                    temp1 = new_string[i]
                    temp2 = new_string[i + 1]
                    new_string[i] = new_string[j]
                    new_string[i + 1] = new_string[j + 1]
                    new_string[j] = temp1
                    new_string[j + 1] = temp2
        return (new_string)

    # main string
    b = []
    for i in range(0, 1):
        strg = val.split()
        l = len(strg)
        for i in range(0, l):
            ret = fun_call(strg[i])
            if (ret == 0):
                b.append(strg[i])

    z = len(b)
    new_string = []
    for i in range(0, z):
        count = count_number(b, b[i], new_string, z)
        if (count != 0):
            new_string.append(b[i])
            new_string.append(count)
    half_sort = i_want_half_sort(new_string)
    temp = half_sort[1]
    final_output = []
    leng = len(half_sort)
    for i in range(1, leng, 2):
        if (temp < half_sort[i]):
            temp = half_sort[i]

    for i in range(1, leng, 2):
        if (temp != 0):
            for j in range(1, leng, 2):
                if (half_sort[j] == temp):
                    final_output.append(half_sort[j - 1])
            temp = temp - 1
        else:
            break

    return render(request, 'twt_result.html', {'name': 'Santash', 'output' : final_output})