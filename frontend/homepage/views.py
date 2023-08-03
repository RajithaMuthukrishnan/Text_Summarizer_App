from django.shortcuts import render
from django.apps import apps
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests


global text_data, summary, button_text
API_URL = "https://api-inference.huggingface.co/models/RajithaMuthukrishnan/text-summariser-english"
headers = {"Authorization": "Bearer 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"}

# Create your views here.
def homepage(request):
    global button_text
    button_text = "Submit"
    context = {
        'button_text': button_text,
    }
    return render(request, 'homepage.html', context)

def get_data(request):
    global button_text
    if (button_text=='Submit' and request.method == 'POST'):
        text_data = request.POST['doc_text_area'] 
        summary = predict(text_data)
        button_text = "Clear"
        context = {
            'text_data': text_data,
            'summary': summary,
            'button_text': button_text,
        }
        return render(request, 'homepage.html', context)
    
    if (button_text=='Clear'):
        return HttpResponseRedirect(reverse('homepage'))


# Helper Functions
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def predict(text_data):
    print('Predicting...')
    output = query({"inputs": text_data,})
    print('Done!')
    output_dict = output[0]
    output_str = output_dict.get('generated_text')
    return output_str
