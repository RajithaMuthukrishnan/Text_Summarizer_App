from django.shortcuts import render
from django.apps import apps


# Create your views here.
def homepage(request):
    # print(apps.get_app_config('homepage').model)
    return render(request, 'homepage.html', {})

# def predict(request):
#     inputs = apps.get_app_config('homepage').tokenizer(
#         test_samples,
#         padding='max_length',
#         truncation=True,
#         max_length=apps.get_app_config('homepage').encoder_max_length,
#         return_tensors='pt',
#     )
#     input_ids = inputs.input_ids.to(apps.get_app_config('homepage').model.device)
#     attention_mask = inputs.attention_mask.to(apps.get_app_config('homepage').model.device)
#     outputs = apps.get_app_config('homepage').model.generate(input_ids, attention_mask=attention_mask)
#     output_str = apps.get_app_config('homepage').tokenizer.batch_decode(outputs, skip_special_tokens=True)
#     return output_str