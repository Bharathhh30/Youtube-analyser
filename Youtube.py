import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi as yta
import google.generativeai as genai

# Configure Google Generative AI
genai.configure(api_key='AIzaSyDURpJOTQXExKr1qdZ1SD7aDS4lnyBkveg')

# Function to convert YouTube URL to text
def youtube_url_to_text(youtube_url):
    vid_id = youtube_url.split('watch?v=')[1]
    data = yta.get_transcript(vid_id)

    transcript = ''
    for value in data:
        for key, val in value.items():
            if key == 'text':
                transcript += val

    l = transcript.splitlines()
    final = "".join(l)
    return final

# Streamlit app
def main():
    st.title("YouTube Transcript to Notes Generator")

    # Get YouTube URL from user input
    youtube_url = st.text_input("Enter YouTube URL:")
    
    if st.button("Generate Notes"):
        if youtube_url:
            # Convert YouTube URL to text
            text = youtube_url_to_text(youtube_url)

            # Use Google Generative AI to generate notes
            model = genai.GenerativeModel('gemini-pro')
            prompt = f"You are an AI assistant that will generate neat notes, based on the corpus of text given. Generate with neat subheadings, multiple newlines, and neat list points, in markdown format. The text is : {text}"
            response = model.generate_content(prompt)

            # Display generated notes
            st.subheader("Generated Notes:")
            st.markdown(response.text)

if __name__ == "__main__":
    main()
