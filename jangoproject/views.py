from django.shortcuts import render
import requests
from django.http import JsonResponse
# from rest_framework import status

def html_page(request):
    return render(request,'index.html')
    
def shop_page(request):
    return render(request, 'shop.html')

def get_externel_data(request):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"error": "Failed to fetch data"}, status=500)
    
def post_externel_data(request):
    url = "https://jsonplaceholder.typicode.com/posts"
    data ={
        "userId": 11,
        "id":101,
        "title": "Sample Post",
        "body": "This is a sample post"
    }
    response = requests.post(url=url, json=data)
    if response.status_code == 201:
        return JsonResponse({"message": "Data posted successfully"}, status=201)
    else:
        return JsonResponse({"error": "Failed to post data"}, status=500)