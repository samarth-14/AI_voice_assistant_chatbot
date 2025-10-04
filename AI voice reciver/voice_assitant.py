import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Fetch API key and Agent ID from environment variables
API_KEY = os.getenv("a0e8044e99c7da67a3b23182f61f9fdda8384eb36a92be77ec384871ec724449")
AGENT_ID = os.getenv("agent_0601k6nqwy2tfggv297sqqvcqf6p")
# --- Imports ---
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig

# --- Config setup ---
user_name = "Samarth"
schedule = "Do Leetcode at 12:00"
prompt = f"You are a helpful assistant. Your interlocutor has the following schedule: {schedule}."
first_message = f"Hello {user_name}, how can I help you today?"

conversation_override = {
    "agent": {
        "prompt": {
            "prompt": prompt,
        },
        "first_message": first_message,
    },
}

config = ConversationConfig(
    user_id="samarth123",  # required unique ID for the user
    conversation_config_override=conversation_override,
    extra_body={},
    dynamic_variables={},
)

# --- Client setup ---
client = ElevenLabs(api_key="a0e8044e99c7da67a3b23182f61f9fdda8384eb36a92be77ec384871ec724449")

# --- Callback functions ---
def print_agent_response(response):
    print(f"Agent: {response}")

def print_interrupted_response(original, corrected):
    print(f"Agent interrupted, truncated response: {corrected}")

def print_user_transcript(transcript):
    print(f"User: {transcript}")

# --- Conversation setup ---
conversation = Conversation(
    client=client,
    agent_id="agent_0601k6nqwy2tfggv297sqqvcqf6p",
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_agent_response_correction=print_interrupted_response,
    callback_user_transcript=print_user_transcript,
)

# --- Start session ---
conversation.start_session()

