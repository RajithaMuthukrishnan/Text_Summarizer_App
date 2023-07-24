from transformers import (
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
)
from huggingface_hub import login, logout

def login_huggingface():
    access_token_write = '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'
    login(token = access_token_write)   

def load_model():
    login_huggingface()
    model_name = "RajithaMuthukrishnan/text-summariser-english"
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    encoder_max_length = 256
    decoder_max_length = 64
    return model, tokenizer, encoder_max_length, decoder_max_length

