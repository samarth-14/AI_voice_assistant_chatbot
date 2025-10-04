# AI_voice_assistant_chatbot
# 🎙️ AI Voice Assistant with ElevenLabs Conversational AI

This project is a simple **AI Voice Assistant** powered by [ElevenLabs Conversational AI](https://elevenlabs.io/).  
It allows you to create a conversational agent that can respond to users based on custom prompts and schedules.  
The assistant runs locally in Python and connects to ElevenLabs’ API for conversation and voice features.

---

## ✨ Features
- 🧠 **Conversational AI** – powered by ElevenLabs
- 🎤 **Voice interface** – listen & respond (via ElevenLabs audio interface)
- ⚡ **Custom prompts** – configure agent behavior and first message
- 🔑 **Secure API keys** using `.env`
- 👤 **User-specific sessions** with unique `user_id`

---

## 📂 Project Structure


---

## 🚀 Getting Started

### 1. Clone the repository
git clone https://github.com/your-username/ai-voice-assistant.git
cd ai-voice-assistant
### 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
###3. Install dependencies
pip install -r requirements.txt

###4. Set up environment variables

Create a .env file in the root of the project:

ELEVENLABS_API_KEY=your_api_key_here
ELEVENLABS_AGENT_ID=your_agent_id_here


You can find these in your ElevenLabs Dashboard
.

###5. Run the assistant
python voice_assistant.py

⚙️ Configuration

In voice_assistant.py, you can customize:

User name

user_name = "Samarth"


Schedule / context

schedule = "Do Leetcode at 12:00"


Agent prompt

prompt = f"You are a helpful assistant. Your interlocutor has the following schedule: {schedule}."


First message

first_message = f"Hello {user_name}, how can I help you today?"

🛠 Requirements

Python 3.9+

ElevenLabs API Key (with ConvAI enabled)

Dependencies listed in requirements.txt

Example requirements.txt:

python-dotenv
elevenlabs

📌 Notes

Make sure your ElevenLabs API key has ConvAI permissions (convai_write) enabled, otherwise you’ll get a 401 error.

Never commit your .env file to GitHub (add it to .gitignore).

🐛 Troubleshooting

401 Unauthorized → Check if your API key has Conversational AI permissions.

Missing user_id → Add user_id when creating ConversationConfig.

os.getenv returning None → Ensure .env file is set up correctly and load_dotenv() is called.

📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute it with attribution.

🙌 Acknowledgments

ElevenLabs
 for Conversational AI & TTS APIs.

python-dotenv
 for environment variable management.
