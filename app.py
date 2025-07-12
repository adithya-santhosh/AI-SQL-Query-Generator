import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyCvp_3TYWby9ZpS7YeEuzklrXe_0OEyNpw"

genai.configure(api_key = GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def main():
    st.set_page_config(page_title = "SQL Query Generator", page_icon="📝")
    st.markdown(
        """
    <div style ="text-align: center;">

    <h1>SQL Query Generator 📃🤖 </h1>
    <h3> Generates SQL queries for your data analysis needs 📊</h3>
    <h4> With explanation for your understanding </h4>

    <p> This is a simple tool which will help in generating SQL queries based on your input prompts. </p>

    </div>
    """
    , unsafe_allow_html=True)

    
    text_input = st.text_area("Enter your SQL Query here")
    
    
    submit = st.button("Generate SQL Query")
    if submit:
        response = model.generate_content(text_input)
        print(response.text)
        st.write(response.text)
main()