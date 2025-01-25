import streamlit as st
import google.generativeai as genai
import base64
import os
import io
from PIL import Image
import pdf2image

genai.configure(api_key="AIzaSyBG34MCMvKKn1tEITnhxhCVkypRcrSFIQs")

def get_model_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_files):
    if uploaded_files is not None:
       images=pdf2image.convert_from_bytes(uploaded_files.read())

       first_page=images[0]
       img_byte_arr=io.BytesIO()
       first_page.save(img_byte_arr,format="JPEG")
       img_byte_arr=img_byte_arr.getvalue()

       pdf_parts=[
          {
            "mime_type": "image/jpeg",
            "data":base64.b64encode(img_byte_arr).decode(encoding=str("utf-8"))
          }
        ]
       return pdf_parts
    else:
        raise FileNotFoundError("No File Uploaded")

st.set_page_config(page_title="Resume_Comparator")
st.header("Resume Evaluation System")
input_text=st.text_area("Job Description : ",key="Input")
uploaded_files=st.file_uploader("Upload Resumes to compare (PDF)..",type=["pdf"])

if uploaded_files is not None:
    st.write("PDFs uploaded Successfully")

submit1=st.button("Key Matches")
submit2=st.button("Missing Requirenments")
submit3=st.button("Percentage Match")
submit4=st.button("Task Recomendation")

input_prompt1="""
You are an expert Technical Human Resource Manager, your task is to evaluate the resumes provided to you against the job description and list out the key highliting skills of the resumes that are also present in Job description.
Based on the evaluation The skills that are mating with the job description are to be listedout in a tabular format.
"""

input_prompt2="""You are an expert Technical Human Resource Manager, your task is to evaluate the resumes provided to you against the job description.
you have to list outthe missing skills, requirements that each of the resume has when compared to Job description. list it out in a comparison table
"""
input_prompt3="""You are an expert ATS scanner with deep understanding on Data science, artificial intellegence and Machine learning.Your task is to evaluate the resumes against job description.
To evaluate the resumes against the Job Description, use the following scoring guidelines:
- Match on Skills: Assign 40% weightage to how well the candidate's skills align with the JD.
- Match on Experience: Assign 30% weightage to the relevance and duration of the candidate's experience.
- Match on Certifications and Education: Assign 20% weightage to certifications, degrees, or other qualifications.
- Other Factors: Assign 10% weightage to additional relevant elements, such as soft skills, location, or languages.
Each resume should receive a total score out of 100, based on these criteria. Provide a breakdown of scores for each candidate, along with a brief explanation of how the scores were derived.
"""
input_prompt4="""
You are an AI assistant tasked with helping job candidates align their skills and experiences with a specific job description (JD). For each candidate, you will recommend actionable tasks to improve their fit for the role. The tasks should focus on addressing skill gaps, gaining relevant experience, optimizing their resume, and enhancing their overall profile.

Steps to Follow:

Identify Skill Gaps:

Review the provided JD and highlight the key skills and qualifications required.

Compare these requirements with the candidate’s current skills and experience.

Recommend Training and Courses:

Suggest online courses, certifications, or workshops that focus on the skills required by the JD.

Platforms like Coursera, Udemy, LinkedIn Learning, and edX offer a plethora of courses across different domains.

Practical Experience:

Recommend projects or hands-on tasks that can help the candidate gain practical experience.

Encourage participation in relevant workshops, hackathons, or volunteering for related projects.

Networking:

Advise the candidate to attend industry conferences, webinars, and networking events.

Encourage them to connect with professionals in the field and join relevant groups or associations.

Resume and LinkedIn Optimization:

Suggest specific changes to their resume and LinkedIn profile to better highlight relevant experiences and skills.

Emphasize the importance of keywords from the JD in their profiles.

Mock Interviews and Feedback:

Conduct mock interviews focused on the job role and provide constructive feedback.

Suggest improvements in their answers, presentation, and technical knowledge.

Soft Skills Development:

Recommend workshops or training sessions for improving soft skills like communication, leadership, and teamwork.

Encourage participation in activities that build these skills, such as public speaking groups or team sports.

Stay Updated with Industry Trends:

Advise reading industry-related blogs, journals, and news articles to stay updated with the latest trends.

Encourage following thought leaders and joining discussions on platforms like LinkedIn and Twitter.

Mentorship:

Suggest finding a mentor in the industry who can provide guidance and support.

Encourage reaching out to alumni networks or professional organizations for mentorship opportunities.

Example:

Candidate Profile:

Current Skills: Basic Python, Data Analysis, Communication

Experience: 1 year as a Data Analyst

JD Requirements: Advanced Python, Machine Learning, Team Leadership

Recommended Tasks:

Skill Gaps:

Enroll in an advanced Python course on Coursera.

Take an introductory Machine Learning course on Udemy.

Practical Experience:

Complete a machine learning project on Kaggle.

Volunteer for a data analysis project in a local tech community.

"""
if submit1:
    if uploaded_files is not None:
        pdf_content=input_pdf_setup(uploaded_files)
        response=get_model_response(input_prompt1,pdf_content,input_text)
        st.subheader("Response :")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2:
    if uploaded_files is not None:
        pdf_content=input_pdf_setup(uploaded_files)
        response=get_model_response(input_prompt2,pdf_content,input_text)
        st.subheader("Response :")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_files is not None:
        pdf_content=input_pdf_setup(uploaded_files)
        response=get_model_response(input_prompt3,pdf_content,input_text)
        st.subheader("Response :")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit4:
    if uploaded_files is not None:
        pdf_content=input_pdf_setup(uploaded_files)
        response=get_model_response(input_prompt4,pdf_content,input_text)
        st.subheader("Response :")
        st.write(response)
    else:
        st.write("Please upload the resume")