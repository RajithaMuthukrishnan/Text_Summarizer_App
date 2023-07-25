from django.shortcuts import render
from django.apps import apps
from django.http import HttpResponseRedirect
from django.urls import reverse


global text_data, summary, button_text

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
        summary = predict(text_data)[0]
        # summary = ['Yeayyyyyyy its working!!!'][0]
        button_text = "Clear"
        context = {
            'text_data': text_data,
            'summary': summary,
            'button_text': button_text,
        }
        return render(request, 'homepage.html', context)
    
    if (button_text=='Clear'):
        return HttpResponseRedirect(reverse('homepage'))

def predict(text_data):
    print('Predicting...')
    inputs = apps.get_app_config('homepage').tokenizer(
        text_data,
        padding='max_length',
        truncation=True,
        max_length=apps.get_app_config('homepage').encoder_max_length,
        return_tensors='pt',
    )
    input_ids = inputs.input_ids.to(apps.get_app_config('homepage').model.device)
    attention_mask = inputs.attention_mask.to(apps.get_app_config('homepage').model.device)
    outputs = apps.get_app_config('homepage').model.generate(input_ids, attention_mask=attention_mask)
    output_str = apps.get_app_config('homepage').tokenizer.batch_decode(outputs, skip_special_tokens=True)
    print('Done!')
    return output_str
