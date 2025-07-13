import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyCvp_3TYWby9ZpS7YeEuzklrXe_0OEyNpw"

genai.configure(api_key = GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.5-pro")

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
        with st.spinner("Generating SQL..."):
            template = """

            Create a SQL query snipper using the following prompt.

            ```
            {text_input}

            ```
            I just want the sql query.
            
            """
            formatted_template = template.format(text_input= text_input)
            
            # st.write(formatted_template)
            response = model.generate_content(formatted_template)
            sql_query = response.candidates[0].content.parts[0].text.strip()   
            sql_query = sql_query.replace("```sql", "").replace("```", "").strip()


            expected_template = """

            What would be the expected response of this sql query snippet:

            ```
            {sql_query}

            ```
            Provide the sample tabular response with no explanation.
            
            """
            expected_template_formatted = expected_template.format(sql_query=sql_query)
            eoutput = model.generate_content(expected_template_formatted)
            expected_table  = eoutput.candidates[0].content.parts[0].text.strip()
            #st.write(expected_table)


            explanation_template = """
            Explain the SQl snipped provided below:
           
             ```
            {sql_query}
            ```

            Provide the simplest of explanations.
"""
            explanation_template_formatted = explanation_template.format(sql_query=sql_query)
            explanation_output = model.generate_content(explanation_template_formatted)
            explanation = explanation_output.candidates[0].content.parts[0].text.strip()
            #st.write(explanation)
            with st.container():
                st.success("SQL Query Generated Successfully!")
                st.code(sql_query, language='sql')

                st.success("Expected Output for this SQL Query")
                st.markdown(expected_table)

                st.success("Explanation of the SQL Query")
                st.markdown(explanation)
main()