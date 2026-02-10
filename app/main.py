import streamlit as st

st.set_page_config(page_title="CV Scanner", layout="wide")

st.title("AI CV Scanner")

st.write("Upload a job description and candidate CVs to rank matches.")

job_description = st.text_area("Job Description")

uploaded_files = st.file_uploader("Upload CVs (PDF)", accept_multiple_files=True)

if st.button("Analyze Candidates"):
    st.success("Analysis will appear here soon.")

