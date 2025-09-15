import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Website Content Writer", page_icon="🌐", layout="wide")

st.title("🌐 AI Website Content Writer with SEO")
st.write("Generate website page content along with SEO meta title, meta description, and keywords.")

# User inputs
page_topic = st.text_input("Enter the page topic (e.g., About Us, Services, Digital Marketing, etc.)", "Digital Marketing Services")
tone = st.selectbox("Select content tone", ["Professional", "Friendly", "Persuasive", "Technical", "Storytelling"])
length = st.selectbox("Content length", ["Short (~200 words)", "Medium (~400 words)", "Long (~800+ words)"])

if st.button("Generate Content"):
    with st.spinner("AI is generating your website content..."):
        prompt = f"""
        You are an expert website content writer.
        Write {length} content for a web page about "{page_topic}" in a {tone} tone.
        Also generate:
        - Meta Title (under 60 characters)
        - Meta Description (under 160 characters)
        - 5 SEO Keywords
        Format the response clearly.
        """

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1200
        )

        content = response.choices[0].message.content

        st.subheader("📄 Website Content with SEO")
        st.write(content)

        # Download button
        st.download_button("Download as TXT", content, file_name=f"{page_topic.replace(' ','_')}_content.txt")
