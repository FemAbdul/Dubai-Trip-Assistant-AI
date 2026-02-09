# Dubai-Trip-Assistant-AI --Streamlit + OpenAI API
🏙️ Dubai Trip Planning Assistant App

An interactive AI-powered travel planning assistant built with Streamlit and OpenAI, designed to create personalized Dubai itineraries through a chat-based interface.

✨ Features

🤖 AI-powered Dubai travel expert

🗺️ Personalized itineraries based on user preferences

🏖️ Covers attractions, culture, dining, shopping, adventure, and relaxation

💬 Real-time conversational chat UI

🔐 Secure API key handling using environment variables

🛠️ Tech Stack

Python

Streamlit – Web application framework

OpenAI API – Large Language Model (GPT-4o-mini)

python-dotenv – Environment variable management

📂 Project Structure
├── app.py
├── .env
└── README.md

Set up environment variables

    Create a .env file in the project root:

    OPENAI_API_KEY=your_openai_api_key_here

▶️ Running the App
   
    streamlit run app.py

How It Works

The app initializes a system prompt defining the AI as a Dubai travel expert.

User messages are stored in Streamlit’s session state.

Each message is sent to OpenAI along with the full conversation history.

The AI responds with concise, tailored travel recommendations.

Chat history is preserved across interactions.
