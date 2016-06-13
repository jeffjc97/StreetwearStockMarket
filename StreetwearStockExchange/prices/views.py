from django.shortcuts import render
from django.http import HttpResponse
import datetime
import json
# import ebaysdk
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection


def index(request):
    return render(request, 'prices.html')


def get_history(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        data = json.loads(data)
        if 'search' in data:
            keywords = data['search']
            try:
                api = Connection(appid='JeffreyC-Streetwe-PRD-f2f871c7c-922e659d', config_file=None)
                response = api.execute('findCompletedItems', {'keywords': keywords})
                items = response.reply.searchResult.item
                return HttpResponse(items)

            except ConnectionError as e:
                return HttpResponse("Connection error.")

        else:
            return HttpResponse("No search.")
    else:
        return HttpResponse("Must be a POST request.")
