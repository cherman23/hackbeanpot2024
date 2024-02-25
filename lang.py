
import openai
import os
# Set the OpenAI API key as an environment variable

os.environ['OPENAI_API_KEY'] = 'YOUR_API_KEY'




# Define the three prompts/instances
prompts = [
    ("I am trying to learn {text} and I AM A BEGINEER. Now, tell me more about it and break it down into three levels for me: Beginner. Make sure your output is bulleted with three bullet points for each level and DO NOT display anything else aside of the bullet points. Keep them short and simple as well. Precede level with a # and the three bullets with a *.", "System"),
    ("I am trying to learn {text} and I AM AT INTERMEDIATE EXPERTISE. Now, tell me more about it and break it down into three levels for me: Intermediate. Make sure your output is bulleted with three bullet points for each level and DO NOT display anything else aside of the bullet points. Keep them short and simple as well. Precede level with a # and the three bullets with a *.", "System"),
    ("I am trying to learn {text} and I AM AT ADVANCED EXPERTISE. Now, tell me more about it and break it down into three levels for me: Advanced. Make sure your output is bulleted with three bullet points for each level and DO NOT display anything else aside of the bullet points. Keep them short and simple as well. Precede level with a # and the three bullets with a *.", "System")
]

# Initialize an empty array to store the outputs
outputs = []
# Set the OpenAI API key as an environment variable
os.environ['OPENAI_API_KEY'] = 'YOUR_API_KEY'

# Define the topic


# Split the prompts equally
# num_prompts = 9
# prompts = [
#     f"{topic} {i+1}" for i in range(num_prompts)
# ]

# Initialize an empty array to store the outputs
outputs = []

# Run the prompts/instances and store the outputs
for prompt, user in prompts:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a super helpful assistant and you need to help a student with three bullet points for each prompt. Do not give me extra fluff and text just give me topics in particular"},
            {"role": "system", "content": user},
            {"role": "assistant", "content": prompt}
        ]
    )
    output = response.choices[0].message.content
    outputs.append(output)

# Print the outputs
print(outputs)