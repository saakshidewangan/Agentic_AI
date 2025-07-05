import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from phi.agent import Agent
from phi.model.groq import Groq

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize AI Agent
youtube_agent = Agent(
    name="YouTube Summary Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Summarize the given YouTube transcript."],
    markdown=True,
    debug_mode=True
)

def get_video_id(url):
    """Extracts video ID from YouTube URL."""
    if "youtube.com" in url:
        return url.split("v=")[-1].split("&")[0]
    elif "youtu.be" in url:
        return url.split("/")[-1]
    return None

def get_transcript(video_url):
    """Fetches transcript of a YouTube video."""
    video_id = get_video_id(video_url)
    if not video_id:
        return None

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([entry['text'] for entry in transcript])
        return transcript_text
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

# User Input: YouTube Video URL
video_url = input("Enter YouTube video URL: ")
transcript = get_transcript(video_url)

if transcript:
    print("\n📜 Transcript fetched successfully!\n")
    youtube_agent.print_response(f"Summarize this transcript: {transcript}", stream=True)
else:
    print("❌ Could not fetch transcript. Try another video.")
