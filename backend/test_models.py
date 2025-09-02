import google.generativeai as genai

genai.configure(api_key="AIzaSyA_cgvKvshXbDpH8uE12DO5F88beE80wBE")

models = genai.list_models()

for model in models:
    print(model.name)
