📄 Resume Evaluation System
A powerful, AI-driven application designed to compare multiple resumes against a given Job Description (JD). This tool not only evaluates candidates based on key skill matches, missing skills, and evaluation scores, but also provides actionable recommendations to close the gaps, ensuring candidates align with the desired role.

🚀 Features
Key Skills Match:

Identify and highlight the overlapping skills between the JD and candidate resumes.
Present the results in a clean and detailed tabular format for better insights.
Missing Requirements:

Pinpoint missing skills, qualifications, or experiences in the resumes when compared to the JD.
Provide a comparative table to highlight areas for improvement.
Candidate Evaluation Scores:

Score resumes out of 100 based on:
Skill Match (40%)
Experience Relevance (30%)
Certifications/Education (20%)
Other Factors (10%)
Get a detailed breakdown for each candidate.
Gap Fulfillment Recommendations:

Suggest actionable tasks, such as:
Online courses and certifications to bridge skill gaps.
Hands-on projects for practical experience.
Networking opportunities to build connections.
Provide personalized advice for optimizing resumes and LinkedIn profiles.
🛠️ How It Works
Upload Resumes:

Upload multiple resumes in PDF format for evaluation.
Provide Job Description:

Enter the JD in the text area to set the evaluation context.
Choose an Evaluation Mode:

Key Matches: Lists the skills matching the JD.
Missing Requirements: Lists the gaps in each resume.
Percentage Match: Assigns a score based on the evaluation criteria.
Task Recommendations: Provides actionable steps for candidates to improve.
View Results:

The application processes the resumes and JD using an advanced AI model and displays the results directly in the app.
🧑‍💻 AI-Powered Evaluation
The application uses Google's Generative AI Gemini 1.5 to:

Analyze resumes and job descriptions.
Generate human-like responses with deep insights.
Provide recommendations tailored to the candidate's profile.
📝 Usage Instructions
Clone the repository:

git clone https://github.com/your-repo/resume-evaluation-system.git
cd resume-evaluation-system
Install the dependencies:


pip install -r requirements.txt
Run the application:

streamlit run app.py
Open the application in your browser and follow the steps to upload resumes and evaluate them against the JD.

🌟 Example Use Cases
For Recruiters: Streamline resume screening and identify top candidates effortlessly.
For Job Seekers: Understand skill gaps and get actionable advice to enhance your profile.
For Career Coaches: Provide data-driven insights to clients for better career planning.
📚 Tech Stack
Frontend: Streamlit for interactive UI.
Backend: Python with the pdf2image and Pillow libraries for PDF processing.
AI Model: Google Generative AI Gemini 1.5 for text analysis and recommendations.
💡 Future Enhancements
Add support for other file formats (e.g., DOCX).
Introduce candidate ranking based on evaluation scores.
Enable custom evaluation criteria set by users.
Integrate email notifications for sharing results.
🤝 Contributions
Contributions are welcome! If you’d like to improve this application, feel free to fork the repo and submit a pull request.

📞 Contact
For queries or support, please contact wmagdum@gmail.com.


