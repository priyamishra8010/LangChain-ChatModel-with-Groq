# LangChain ChatModel with Groq

## Overview

This project demonstrates how to integrate a Large Language Model (LLM) with LangChain using Groq. It sends a prompt to the Qwen model and prints the generated response.

## Technologies Used

- Python
- LangChain
- LangChain Groq
- Groq API
- python-dotenv

## Concepts Learned

- Initializing a chat model using `ChatGroq`
- Loading environment variables using `python-dotenv`
- Sending prompts to an LLM using `invoke()`
- Configuring model parameters such as temperature and maximum output tokens
- Accessing the generated response using `response.content`

## How It Works

1. Load environment variables from the `.env` file.
2. Initialize the Qwen chat model using `ChatGroq`.
3. Send a prompt using `llm.invoke()`.
4. Print the generated text response.

## Setup and Installation

1. Create and activate a virtual environment.

   **Windows:**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add your Groq API key:

   ```text
   GROQ_API_KEY=your_actual_api_key
   ```

4. Run the project:

   ```bash
   python chatmodel.py
   ```

## Model Configuration

- **Model:** `qwen/qwen3.8-27b`
- **Temperature:** `0`
- **Maximum output tokens:** `100`

## Purpose

This beginner-level Generative AI project demonstrates LLM integration with LangChain, prompt submission, model configuration, and API-based response generation.

## Security

- Never upload your `.env` file or expose your Groq API key.
- Keep API credentials private.
