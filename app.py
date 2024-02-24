# from fastapi import FastAPI, Form
# import subprocess
# import json

# app = FastAPI()

# # Route to receive the single input from the frontend
# @app.post("/input")
# async def receive_input(text: str = Form(...)):
#     # Trigger the run of main.py
#     subprocess.run(["python", "main.py", text])
    
#     return {"message": "Input received successfully"}

# # # Route to get the titles and playlist link from main.py
# # @app.get("/results")
# # async def get_results():
# #     # Read the generated JSON file
# #     with open("results.json", "r") as file:
# #         results = json.load(file)
    
# #     return results

# # # Run the FastAPI application
# # if __name__ == "__main__":
# #     import uvicorn
# #     uvicorn.run(app, host="0.0.0.0", port=8000)

import sys
import json
import requests
import os
import openai

def gpt_request(prompt, api_key):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=input_text,
        max_tokens=500,
        api_key=os.environ.get('OPENAI_API_KEY')
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py <text_to_process>")
        sys.exit(1)
    
    input_text = sys.argv[1]
    
    # Customize your prompt here. Add the user's text to this prompt as needed.
    custom_prompt = f"This is your customized input: {input_text}. Now, tell me more about it."
    
    # Ensure you have the OPENAI_API_KEY environment variable set.
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        sys.exit(1)
    
    gpt_response = gpt_request(custom_prompt, api_key)

    response_json = json.dumps(gpt_response, ensure_ascii=False)
    
    # Print or handle the JSON response as needed. 
    # In an actual application, you would likely send this back to the caller or another part of your system. 
    print(response_json)

print("Hello World")


