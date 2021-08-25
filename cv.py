import cv2
import imutils
import json
import numpy as np
import os
import requests
from base64 import b64encode


def makeImageData(imgpath):
    img_req = None
    with open(imgpath, 'rb') as f:
        ctxt = b64encode(f.read()).decode()
        img_req = {
            'image': {
                'content': ctxt
            },
            'features': [{
                'type': 'DOCUMENT_TEXT_DETECTION',
                'maxResults': 1
            }]
        }
    return json.dumps({"requests": img_req}).encode()


def requestOCR(url, api_key, imgpath):
  imgdata = makeImageData(imgpath)
  response = requests.post(ENDPOINT_URL, 
                           data = imgdata, 
                           params = {'key': api_key}, 
                           headers = {'Content-Type': 'application/json'})
  return response

def pipeline():
    key_file = open("api_key.txt","r")

    api_key = key_file.readline()

    #using api
    global ENDPOINT_URL
    ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
    
    img_loc = "Captcha.png"


    result = requestOCR(ENDPOINT_URL, api_key, img_loc)

    if result.status_code != 200 or result.json().get('error'):
        print ("Error")
    else:
        result = result.json()['responses'][0]['textAnnotations']


    print(result[0]["description"])
    final_result = result[0]["description"]

    final_result = ''.join(e for e in final_result if e.isalnum())
    return(final_result)