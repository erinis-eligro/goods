from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
import pandas as pd
import os
from goods_adobeday_adobe import settings
from .models import CheckedUser

# Create your views here.
def index(request):
    return HttpResponse("Hello Adobe Day!")

def input_list(request):

    #Text Code
    # testUsers = CheckedUser.objects.all()
    # for user in testUsers:
    #     print("Email "+ user.email)

    return render(request, 'input_list.html', {})

def duplication(request):
    return render(request, 'duplication.html')

def none_user(request):
    return render(request, 'none_user.html')

def search(request):
    if request.method == 'GET':
        print('here!!! '+request.method)
        return render(request, 'result_search.html')
    
    elif request.method == 'POST':
        
        checkeds = CheckedUser.objects.filter(email=request.POST['company_email'])
        if checkeds.exists():
            return render(request, 'duplication.html')

        email = request.POST['company_email']

        print("Email "+email)

        fp = os.path.join("static/list.xlsx")
        df = pd.read_excel(fp)

        col_size = df['후드티 사이즈']
        col_name = df['이름']
        col_phone = df['연락처']
        col_division = df['부서']
        col_mail = df['이메일']

        return_context = {}
        for i in col_name.index:
            # print(col_mail[i]+"   "+email)
            if col_mail[i] == email:
                return_context = {
                    'Name' : col_name[i],
                    'Phone' : col_phone[i],
                    'Division' : col_division[i],
                    'Email' : col_mail[i],
                    'Size' : col_size[i]
                }

        if return_context == {} :
            return render(request, 'none_user.html')
        else:
            settings.GLOBAL_CONTEXT = return_context
            return render(request, 'result_search.html', return_context)

    # for i in df.index:
    #     print(size[i])

    # data = get_data(fp, file_type='xlsx')
    # print(json.dump(data))

    # return render(request, 'result_search.html', context)
    # return render(request, 'result_search.html', {'form':form})

def confirm(request):
    print(settings.GLOBAL_CONTEXT)
    context = settings.GLOBAL_CONTEXT
    # print(return_context['Name'])
    # print(return_context['Phone'])
    # print(return_context['Division'])
    # print(return_context['Email'])
    # print(return_context['Size'])

    checked = CheckedUser(
        username = context['Name'],
        email = context['Email']
    )
    checked.save()

    return render(request, 'confirm.html', {})