from fastapi import FastAPI, Form
import subprocess
import json
import openai
import os

app = FastAPI()

def gpt_request(prompt, api_key):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=500,
        api_key=api_key
    )
    return response.choices[0].text.strip()

# Route to receive the single input from the frontend
@app.post("/input")
async def receive_input(text: str = Form(...)):
    # Trigger the run of main.py
    custom_prompt1 = f"I am trying to learn {text}. Now, tell me more about it and break it down into three levels for me: Beginner. Make sure your output is bulleted with three bullet points for each level and DO NOT display anything else aside of the bullet points. Keep them short and simple as well. Precede level with a # and the three bullets with a *."
    # custom_prompt2 = f"I am trying to learn {text}. Now, tell me more about it and break it down into three levels for me: Intermediate. Make sure your output is bulleted with three bullet points for each level and DO NOT display anything else aside of the bullet points. Keep them short and simple as well. Precede level with a # and the three bullets with a *."
    # custom_prompt3 = f"I am trying to learn {text}. Now, tell me more about it and break it down into three levels for me: Advanced. Make sure your output is bulleted with three bullet points for each level and DO NOT display anything else aside of the bullet points. Keep them short and simple as well. Precede level with a # and the three bullets with a *."
    
    # Ensure you have the OPENAI_API_KEY environment variable set.
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return {"error": "OpenAI API key not found. Please set the OPENAI_API_KEY environment variable."}

    # Make the GPT-3.5 request
    gpt_response = gpt_request(custom_prompt1, api_key)
    level = []
    bullets = []

    schedule_text = gpt_response
    
    lines = schedule_text.split('\n')

    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            level.append(line)
        elif line.startswith('*'):
            bullets.append(line)

    for i in range(len(level)):
        title1 = level[i].lstrip('#').strip()
        task1 = bullets[i].lstrip('*').strip()

    # Return the GPT-3.5 response
    

    # gpt_response2 = gpt_request(custom_prompt2, api_key)
    # level = []
    # bullets = []

    # schedule_text2 = gpt_response
    
    # lines = schedule_text2.split('\n')

    # for line in lines:
    #     line = line.strip()
    #     if line.startswith('#'):
    #         level.append(line)
    #     elif line.startswith('*'):
    #         bullets.append(line)

    # for i in range(len(level)):
    #     title2 = level[i].lstrip('#').strip()
    #     task2 = bullets[i].lstrip('*').strip()

    # # Return the GPT-3.5 response
    # gpt_response3 = gpt_request(custom_prompt3, api_key)
    # level = []
    # bullets = []

    # schedule_text3 = gpt_response3
    
    # lines = schedule_text3.split('\n')

    # for line in lines:
    #     line = line.strip()
    #     if line.startswith('#'):
    #         level.append(line)
    #     elif line.startswith('*'):
    #         bullets.append(line)

    # for i in range(len(level)):
    #     title3 = level[i].lstrip('#').strip()
    #     task3 = bullets[i].lstrip('*').strip()

    return {title1, task1, title2, task2, title3, task3}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)