
import streamlit as st 
from PyPDF2 import PdfReader

from backend import get_details, recommend_courses, industry_trends, highlight_action_items, SMART, career_dev_ops, soft_skills

with open('main.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("IntelliReview Solutions")

st.subheader("""Empowering Growth: Transforming Performance Reviews into Actionable Insights""")

placeholder = st.empty()

with st.sidebar:
    st.header("Please add the performance review file")
    uploaded_file = st.file_uploader("Choose a file", type='pdf')
    submit_button = st.sidebar.button(label='Submit Data')

if submit_button:
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    with open('uploaded.pdf', 'wb') as f:
        f.write(uploaded_file.getvalue())

    reader = PdfReader('uploaded.pdf')
    pages = len(reader.pages)

    tabs = st.tabs(["Details", "Career Opportunities", "Recommended Courses", "1:1 Optimizer", "Action Items", "Soft Skills", "Personal Skills"])
    with tabs[0]:
        
        with st.spinner("Getting Details"):

            st.subheader("Details")
            out = get_details(reader.pages[0].extract_text())
            st.markdown(f"<p>{out}</p>", unsafe_allow_html=True)

    with tabs[1]:
        with st.spinner("Carrer Opportunities"):
            st.subheader("Career opportunities")
            performance_text = ''
            for i in range(pages-2, pages):
                performance_text += reader.pages[i].extract_text()
            out = career_dev_ops(performance_text)
            st.markdown(out)

    with tabs[2]:
        with st.spinner("Recommending Courses"):
            st.subheader("Recommended Courses")
            performance_text = ''
            for i in range(pages-2, pages):
                performance_text += reader.pages[i].extract_text()
            output = recommend_courses(performance_text)
            st.markdown(output)

    with tabs[3]:
        with st.spinner("Getting Subjects"):
            st.subheader("1:1 Optimizer")
            input_text = ''
            if pages >= 2:
                input_text = reader.pages[0].extract_text() + reader.pages[1].extract_text()
            output = industry_trends(input_text)
            st.markdown(output)

    with tabs[4]:
        with st.spinner("Generating Actions"):
            st.subheader("Action Items for next Year")
            input_text = ''
            if pages >= 4:
                input_text = reader.pages[2].extract_text() + reader.pages[3].extract_text()
            out = highlight_action_items(input_text)
            st.markdown(out)

    with tabs[5]:
        with st.spinner("Soft Skills"):
            st.subheader("Soft Skills")
            input_text = ''
            if pages >= 4:
                input_text = reader.pages[2].extract_text() + reader.pages[3].extract_text()
            output = soft_skills(input_text)
            st.markdown(output)

    with tabs[6]:
        with st.spinner("SMART Goals"):
            st.subheader("Smart Goal setting")
            performance_text = ''
            for i in range(pages-2, pages):
                performance_text += reader.pages[i].extract_text()
            output = SMART(performance_text)
            st.markdown(output)

