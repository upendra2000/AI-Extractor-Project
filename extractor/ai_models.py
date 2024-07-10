import json
import xml.etree.ElementTree as ET
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

class AIModelFactory:
    @staticmethod
    def get_model(model_name, credentials):
        if model_name == "gpt2":
            return GPT2Model(credentials)
        elif model_name == "tinyllama":
            return TinyLlamaModel(credentials)
        else:
            raise ValueError(f"Unsupported model: {model_name}")

class GPT2Model:
    def __init__(self, credentials):
        self.tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")
        self.model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2")
        self.pipe = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)

    def generate_text(self, prompt):
        result = self.pipe(prompt, max_length=150, max_new_tokens=50, num_return_sequences=1)
        return result[0]["generated_text"]

class TinyLlamaModel:
    def __init__(self, credentials):
        self.tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
        self.model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
        self.pipe = pipeline("summarization", model=self.model, tokenizer=self.tokenizer)

    def generate_text(self, prompt):
        result = self.pipe(prompt, max_length=150, max_new_tokens=50, num_return_sequences=1)
        return result[0]["summary_text"]

class DataExtractor:
    def __init__(self, model_name, credentials):
        self.model_name = model_name
        self.credentials = credentials
    
    def extract_data(self, content, extract_type, response_format):
        if extract_type == "extract_text":
            # Process text data
            return self.process_text(content)
        elif extract_type == "extract_binary":
            # Process binary data
            return self.process_binary(content)
    
    def process_text(self, text):
        # Implement text processing logic here
        return {"text_data": text}
    
    def process_binary(self, binary_data):
        # Implement binary processing logic here
        return {"binary_data": binary_data}
