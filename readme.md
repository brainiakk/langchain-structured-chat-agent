## LangChain Structured Chat Agent with Vision and Screenshot Tools

This repository contains code for a YouTube tutorial demonstrating how to set up a LangChain structured chat agent with custom tools for image analysis. The agent leverages Google Vertex AI's Gemini Pro model for its reasoning abilities and utilizes tools to interact with the user's webcam and screen.

**Features:**

* **Structured Chat Agent:** Utilizes LangChain's structured chat agent framework for efficient and human-like conversation.
* **Vision Tool:** Enables the agent to analyze images captured from the user's webcam.
* **Screenshot Tool:** Allows the agent to take screenshots of the user's screen for analysis.
* **Gemini Pro Integration:** Leverages the power of Google Vertex AI's Gemini Pro model for advanced reasoning and image understanding.
* **Voice Service Integration:** (Optional) Uses a voice service to play back responses.

**Getting Started:**

1. **Prerequisites:**
 - Python 3.9+
 - Google Cloud Platform Account with an active Vertex AI API key
 - `langchain` and other required libraries (see `requirements.txt`)

2. **Setup:**
 - Install dependencies: `pip install -r requirements.txt`
 - Create a Google Cloud Project and enable the Vertex AI API.
 - Obtain a Vertex AI API key and set it as the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.
 - Add your API key to the code.
 - (Optional) Install and set up a voice service (e.g., gTTS).
3. **Run the code:** `python main.py` or  `python -m main`

**Usage:**

- Run the script and interact with the agent via the console.
- Ask the agent to "look at the camera" or "take a look" to use the Vision Tool and analyze the webcam feed.
- Ask the agent to "look at the screen" or "take a screenshot" to use the Screenshot Tool and analyze the current screen.

**Note:**

- This project utilizes Google Vertex AI's Gemini Pro model, which is currently in preview.
- Ensure your system has a working webcam and the ability to take screenshots, enable the necessary permissions for your terminal.
- Customize the prompt, tools, and voice service to suit your specific needs.

**Further Development:**

- Integrate more tools to expand the agent's capabilities.
- Implement a web interface for a more interactive user experience.
- Explore using different large language models for image understanding.

This project provides a solid foundation for building a structured chat agent capable of interacting with the real world through image analysis.