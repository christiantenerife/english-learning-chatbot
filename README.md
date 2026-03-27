# English Learning Chatbot

A chatbot built with Flask that helps learners find English practice activities such as grammar exercises, vocabulary tasks, and B2 First (FCE) exam practice.



## Features

- Search grammar, vocabulary, reading, and exam practice activities
- Topic detection (conditionals, reported speech, etc.)
- Clickable activity links
- Simple conversational help messages
- Designed for an English learning website

## Tech Stack

- Python
- Flask
- HTML
- JavaScript

## How it works

1. User sends a message in the chat interface
2. Flask receives the message
3. The chatbot detects:
   - level (B1, B2)
   - skill (grammar, vocabulary, etc.)
   - topic (conditionals, reported speech, etc.)
4. The bot returns recommended activities with clickable links

## Running the project

Install dependencies:


pip install -r requirements.txt


Run the server:


python app.py


Open the chatbot:


http://127.0.0.1:5000
<img width="926" height="924" alt="image" src="https://github.com/user-attachments/assets/fec43771-4613-4cba-8c5e-f2f5f595aea5" />


## Example queries

Try asking:

- B2 grammar
- conditional activities
- reported speech exercises
- exam practice

## Future Improvements

- Firebase integration
- smarter NLP topic detection
- lesson recommendations
- connecting videos with H5P activities
