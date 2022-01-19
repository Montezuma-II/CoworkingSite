""" https://git.heroku.com/lit-cove-22798.git"""

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
class MainView(HttpResponse):

    @staticmethod
    def main_view(request):
        return render(request, 'index.html')
