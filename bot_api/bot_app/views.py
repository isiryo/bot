from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import requests

import json
import bot_app.apps as apps

class api(TemplateView):
   # try:
        def post(self, request, *args, **kwargs):
            massage=json.load(request)["events"]["message"]["text"]
            person=json.load(request)["events"]["source"]["userId"]
            date=json.load(request)["events"]["timestamp"]
            sentence=apps.genelate_content(massage,person,date)
            headers = {
    "Content-Type":"application/json",
    "Authorization":"Bearer {jJJVeswm9MS0yEXwSVEDsGdHqglsRYFwetFdhsiJk7kLqXhKNM+ncOECqgcOJizUgAHHg7B+6mK+ogntQcnvOW goZWwuZo1c/sLiToW/+CYggTfQKZQxVN0RU1tRqGO/1ZSi0nHhtJrAPRN+7FUh3wdB04t89/1O/w1cDnyilFU=}"
                    }
            data={
                  "to":f"{person}",
                  "massages":{
                        "type":"text",
                        "text":f"{sentence}"
                  }
                }
            responce=requests.post(url="https://api.line.me/v2/bot/message/push",headers=headers,json=data)
    #except:
       # pass


# Create your views here.
