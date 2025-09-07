# Interview_bot
☁️ Interview Preparation Bot

A simple interview preparation chatbot that generates domain-specific interview questions, evaluates candidate answers by providing a numeric score (1 to 10), and tracks session history (JSON, CSV, PDF report).

✅ Features

 Generate challenging interview questions for a given role, mode (technical, HR), and domain (AI, Cloud, etc.).
 
 Evaluate candidate answers locally using a pretrained language model.
 
 Track session history: stores all Q&A in JSON & CSV.
 
 Export a PDF report summarizing the session (optional).

Fully offline and modular — no external API required.

# Requirements
Python ≥ 3.8

# How to Run
Run the chatbot:
  chatbot.py

 # Notes

The evaluation score is generated locally using the google/flan-t5-small
 model.
 
To enable PDF report export, install fpdf:
