import google.generativeai as palm
import os
from dotenv import load_dotenv
load_dotenv(".env")

palm.configure(api_key=os.environ['API_KEY'])


models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name 




def create_message (prompt:str):
    completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=1.0,# This parameter define how much changes the answer to the same prompt 
    # The maximum length of the response
    max_output_tokens=100,
)   
    mensaje=completion.result
    return  mensaje


