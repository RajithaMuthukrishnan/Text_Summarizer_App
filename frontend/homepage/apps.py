from django.apps import AppConfig
from homepage.bart_model import load_model

class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "homepage"
    model, tokenizer, encoder_max_length, decoder_max_length = load_model()
    print('Model loaded')
