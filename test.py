import streamlit as st
import google.generativeai as genai
import os

# Set your API key securely
GOOGLE_API_KEY = "AIzaSyCvp_3TYWby9ZpS7YeEuzklrXe_0OEyNpw"  # Store your API key in an .env file or in Streamlit secrets
genai.configure(api_key=GOOGLE_API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

def main():
    st.set_page_config(page_title="SQL Query Generator", page_icon="📝")

    st.markdown("""
        <div style="text-align: center;">
            <h1>SQL Query Generator 📃🤖</h1>
            <h3>Generates SQL queries for your data analysis needs 📊</h3>
            <h4>With explanation for your understanding</h4>
            <p>This tool helps generate SQL queries based on your prompts.</p>
        </div>
        """, unsafe_allow_html=True)

    text_input = st.text_area("What do you want to do with your data?", 
                              placeholder="e.g., Show total sales for each product in 2024...")

    submit = st.button("Generate SQL Query")

    if submit and text_input.strip():
        try:
            with st.spinner("Generating SQL..."):
                response = model.generate_content(text_input)
                sql_output = response.candidates[0].content.parts[0].text.strip()

                st.subheader("Generated SQL Query & Explanation")
                st.markdown(sql_output)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
