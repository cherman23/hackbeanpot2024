from fastapi import FastAPI, Form

app = FastAPI()

import openai

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def generate_search_keywords(topic):
    prompts = [
        "How to " + topic + " for beginners",
        "Basic " + topic + " tutorial",
        topic + " 101",
        "Advanced " + topic + " techniques",
        "Intermediate " + topic + " guide",
        "Next level " + topic,
        "Mastering " + topic,
        "Expert " + topic + " strategies",
        "Deep dive into " + topic
    ]

    search_keywords = []
    for prompt in prompts:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        search_keywords.append(response["choices"][0]["text"].strip())

    return search_keywords

# @app.get("/search_keywords/")
# def get_search_keywords(topic: str):
#     search_keywords = generate_search_keywords(topic)
#     return {"search_keywords": search_keywords}

@app.post("/input")
async def receive_input(text: str = Form(...)):
    # Trigger the run of main.py
    search_keywords = generate_search_keywords(text)
    return {"search_keywords": search_keywords}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
