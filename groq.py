# -*- coding: utf-8 -*-
"""GROQ.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10ZrijQq04CWg7b0lNf0VC6HOxj8xOJ5_
"""

import gradio as gr
import requests
import json
import os

GROQ_TOKEN = os.getenv("GROQ_TOKEN")

# Set the Groq API URL and token
API_URL = "https://api.groq.com/openai/v1/chat/completions"
headers = {"Authorization": f"Bearer {GROQ_TOKEN}"}

def generate_text_groq(prompt):
    messages = [{"role": "user", "content": prompt}]

    # Create the payload
    payload = {
        "model": "mixtral-8x7b-32768",  # Replace with the correct model name if available
        "messages": messages,
        "max_tokens": 1000,  # Adjust as needed
    }

    # Make the request to the API
    response = requests.post(API_URL, headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response
        result = response.json()
        generated_text = result["choices"][0]["message"]["content"]
        return generated_text
    else:
        return f"Error {response.status_code}: {response.text}"

# Define custom CSS for a modern, attractive theme
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
body {
    font-family: 'Roboto', sans-serif;
    background-color: #f4f7f8; /* Light background */
    color: #333;
    margin: 0;
    padding: 20px;
}
.container {
    max-width: 800px; /* Limit the width for better readability */
    margin: auto;
    padding: 20px;
    border-radius: 10px;
    background-color: #ffffff; /* White background for the container */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}
h1 {
    font-size: 32px; /* Large heading */
    font-weight: 700; /* Bold */
    color: #007BFF; /* Primary color */
    text-align: center;
}
.description {
    font-size: 18px; /* Medium size for description */
    font-weight: 500; /* Semi-bold */
    color: #666; /* Neutral color for description text */
    text-align: center;
    margin-bottom: 20px;
}
#input-textbox {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 12px;
    font-size: 16px;
    width: 100%;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    transition: border-color 0.3s, box-shadow 0.3s;
}
#input-textbox:focus {
    border-color: #007BFF; /* Highlight color on focus */
    box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
    outline: none; /* Remove default outline */
}
#output-text {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 12px;
    font-size: 16px;
    background-color: #e8f4f8;  /* Light background for output */
    color: #333;  /* Dark text for output */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    transition: box-shadow 0.3s;
}
.card {
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s;
}
.card:hover {
    transform: scale(1.02); /* Scale effect on hover */
}
.button {
    background-color: #007BFF; /* Primary button color */
    color: white;
    border: none;
    border-radius: 5px;
    padding: 12px 20px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s, transform 0.2s;
}
.button:hover {
    background-color: #0056b3; /* Darker shade on hover */
    transform: scale(1.05); /* Slight scale on hover */
}
.footer {
    text-align: center;
    margin-top: 20px;
    color: #666;
    font-size: 14px;
}
.examples {
    font-size: 14px; /* Smaller size for example text */
    color: #555;  /* Neutral Color */
    margin-top: 10px;
}
@media (max-width: 600px) {
    h1 {
        font-size: 24px; /* Responsive heading size */
    }

    .button {
        width: 100%; /* Full width buttons on small screens */
    }
}
"""

iface = gr.Interface(
    fn=generate_text_groq,
    inputs=[
        gr.Textbox(
            lines=5,
            placeholder="Enter your prompt here...",
            label="Prompt",
            elem_id="input-textbox"
        )
    ],
    outputs=[
        gr.Textbox(label="Generated Text", elem_id="output-text")
    ],
    title="Groq Text Generation",
    description="Generate text using the Groq API.",
    theme="default",  # You can change the theme to "compact" or any other as needed
    css=custom_css,  # Apply custom CSS
    examples=[
        ["Tell me a story about a brave knight."],
        ["What are the benefits of meditation?"],
        ["Describe a beautiful sunset in the mountains."]
    ],
    allow_flagging="never"  # Remove the flag button
)

iface.launch()