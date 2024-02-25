from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import json
import openai
import os
import subprocess
import asyncio

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# def gpt_request(prompt, api_key):
#     response = openai.Completion.create(
#         engine="gpt-3.5-turbo-instruct",
#         prompt=prompt,
#         max_tokens=1000,
#         api_key=api_key
#     )
#     return response.choices[0].text.strip()

# prompts = [
#     ("I am trying to learn {text} and I AM A BEGINEER. Now, tell me more about it and break it down into three levels for me: Beginner. Make sure your output is bulleted with three bullet points for each level and DO NOT display anything else aside of the bullet points. Keep them short and simple as well. Precede level with a # and the three bullets with a comma(,).", "System"),
#     ("I am trying to learn {text} and I AM AT INTERMEDIATE EXPERTISE. Now, tell me more about it and break it down into three levels for me: Intermediate. Make sure your output is bulleted with three bullet points for each level and DO NOT display anything else aside of the bullet points. Keep them short and simple as well. Precede level with a # and the three bullets with a comma(,).", "System"),
#     ("I am trying to learn {text} and I AM AT ADVANCED EXPERTISE. Now, tell me more about it and break it down into three levels for me: Advanced. Make sure your output is bulleted with three bullet points for each level and DO NOT display anything else aside of the bullet points. Keep them short and simple as well. Precede level with a # and the three bullets with a comma(,).", "System")
# ]

# Route to receive the single input from the frontend

@app.post("/input")
async def receive_input(text: str = Form(...)):
    return {"message": "Received input: " + text}
# # Initialize an empty array to store the outputs
#     outputs = []
#     # Set the OpenAI API key as an environment variable
#     os.environ['OPENAI_API_KEY'] = 'YOUR_API_KEY'

#     # Define the topic


#     # Split the prompts equally
#     # num_prompts = 9
#     # prompts = [
#     #     f"{topic} {i+1}" for i in range(num_prompts)
#     # ]

#     # Initialize an empty array to store the outputs
#     outputs = []

#     # Run the prompts/instances and store the outputs
#     for prompt, user in replaced_prompts:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a super helpful assistant and you need to help a student with three bullet points for each prompt. Do not give me extra fluff and text just give me topics in particular"},
#                 {"role": "system", "content": user},
#                 {"role": "assistant", "content": prompt}
#             ]
#         )
#         output = response.choices[0].message.content
#         outputs.append(output)

#     # Print the outputs
#     # return(outputs)

#     def formatOutputs(outputs):
#         formatted = []
#         for element in outputs:
#             formatted.append(list(element.split("\n")))
#         return formatted

#     def removeFluff(outputs):
#         for element in outputs:
#             element.pop(0)
#             for item in range(len(element)):
#                 element[item] = element[item][2::]
#         return outputs

#     outputs = removeFluff(formatOutputs(outputs))

#     return(outputs)


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

    # return {title1, task1, title2, task2, title3, task3}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)