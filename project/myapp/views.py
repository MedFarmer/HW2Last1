from django.shortcuts import render
import requests
from django.http import HttpResponse
import json

def fetch_data(request):    
    url = 'https://jsonplaceholder.typicode.com/todos/'
    response = requests.get(url)
    data = response.json()   
    with open('data.json', 'w') as file:
        json.dump(data, file)
    
    return render(request, 'data.html', {'data':data}) 






