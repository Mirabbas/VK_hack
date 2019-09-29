# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 08:55:52 2019

@author: pitonhik
"""

import urllib.request
# If you are using Python 3+, import urllib instead of urllib2

import json 
import requests as re
def get_reit(value):
 try:
  data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["name", "fam", "sex", "age", "university", "career", "relation", "citi__id", "citi__title", "country__id", "country__title", "personal__political", "personal__religion", "personal__people_main", "personal__life_main", "personal__smoking", "personal__alcohol", "kr"],
                    "Values": [value]
                },        },
            "GlobalParameters": {
  }
     }

  body = str.encode(json.dumps(data))

  url = 'https://ussouthcentral.services.azureml.net/workspaces/5a025a8840b54b2e9d12f218006de513/services/3d232e6cd4da4d6e9b1aaf0bc1e1fea2/execute?api-version=2.0&details=true'
  api_key = '8jZKCuHu7867Oi0+sgGP3pKtui+vqF8BHP9ziWveL+zBwOA/r79355gVTEa5JCVG8ReTfuuWoyqDdzAhgoJq3w==' # Replace this with the API key for the web service
  headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

  #req = urllib.request(url, body, headers) 

  if True:
    #response = urllib.request.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    req = urllib.request.Request(url, body, headers) 
    response = urllib.request.urlopen(req)
    #print(response)
    r = eval(response.read())
  
    return float(r['Results']['output1']['value']['Values'][0][-1:][0])
    #print(result) 
 except:
     return 0
  
            