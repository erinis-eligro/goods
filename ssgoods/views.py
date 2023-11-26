from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
import pandas as pd
import os



# Create your views here.
def index(request):
    return HttpResponse("Hello Adobe Day!")

def input_list(request):
    return render(request, 'input_list.html', {})

def search(request):
    fp = os.path.join("goods_adobeday_adobe/static/list.xlsx")
    df = pd.read_excel(fp)

    size = df['후드티 사이즈']
    name = df['이름']
    phone = df['연락처']

    context = {
        'Name' : name[300],
        'Phone' : phone[300],
        'Size' : size[300]
    }

    for i in df.index:
        print(size[i])

    # data = get_data(fp, file_type='xlsx')
    # print(json.dump(data))

    return render(request, 'result_search.html', context)