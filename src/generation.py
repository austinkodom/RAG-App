from transformers import pipeline

def generate_response(input_text):
    generator = pipeline('text2text-generation', model='t5-base')
    response = generator(input_text,max_new_tokens=200, num_return_sequences=1)

    return response[0]['generated_text']
