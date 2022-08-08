from django.shortcuts import render
import requests

def home(request):
    url = "https://openapi.naver.com/v1/search/book.json?query=%EC%A3%BC%EC%8B%9D&amp;display=10&amp;start=1&quot;"
    header_data = {"X-Naver-Client-Id": 'pp2PYHr35Hb2KoEQJlTD',
               'X-Naver-Client-Secret': 'DlH1Et474N'}
    response = requests.get(url,  headers=header_data)
    response_status = response.status_code
    response_data = response.json()
    # print(response_data)
    # return render(request, 'login.html', {'response':response_data})
    if response_status == 200:
        response_data = response.json()
        return render(request, 'index.html', response_data)
    else:
        return render(request, 'login/errorPage.html', {'response':response_data})
    return render(request,"index.html")
