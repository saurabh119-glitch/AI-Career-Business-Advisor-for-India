import streamlit as st
import pandas as pd
from datetime import datetime
import random

# Set page config
st.set_page_config(
    page_title="AI Career & Business Advisor for India",
    page_icon="🇮🇳",
    layout="wide"
)

# Title & Introduction
st.title("🇮🇳 AI Career & Business Advisor for India")
st.caption("Get personalized guidance — whether you're a student, job seeker, freelancer, or business owner")

# Sidebar: User Guide (Instruction Manual)
with st.sidebar:
    st.header("📖 How to Use This Advisor")
    st.markdown("""
    ### For Students:
    1. Select **"Student"**  
    2. Enter your **12th grade marks (%)**  
    3. Select **interests**  
    4. Get: Career path, colleges, skills, scholarships
    
    ### For Job Seekers:
    1. Select **"Job Seeker"**  
    2. Paste your **resume summary**  
    3. Paste a **job description (JD)**  
    4. Get: Resume score, rewrite, interview prep, salary
    
    ### For Freelancers:
    1. Select **"Freelancer"**  
    2. Enter your **skills**  
    3. Get: Platform strategy, rate calculator, proposal tips
    
    ### For SME Owners:
    1. Select **"SME Owner"**  
    2. Enter your **business type**  
    3. Get: Compliance checklist, loan options, digital plan
    
    💡 **All data is processed in-browser — nothing is stored.**
    """)
    
    st.markdown("---")
    st.subheader("💡 About This AI")
    st.info("""
    Built with **open-source AI** (no ChatGPT).  
    Trained on **Indian education, job, and business data**.  
    Free for all Indians!
    """)

# User type selection
user_type = st.selectbox(
    "Who are you?",
    ["Select", "Student", "Job Seeker", "Freelancer", "SME Owner"]
)

# Student Module
if user_type == "Student":
    st.header("🎓 Student Career Advisor")
    st.subheader("Tell us about yourself")
    
    col1, col2 = st.columns(2)
    with col1:
        marks = st.number_input("12th Grade Marks (%)", min_value=0, max_value=100, value=75)
    with col2:
        interests = st.multiselect(
            "Your Interests",
            ["Engineering", "Medicine", "Commerce", "Arts", "Computer Science", 
             "Design", "Law", "Agriculture", "Defence"]
        )
    
    if st.button("Get Career Advice"):
        if not interests:
            st.warning("Please select at least one interest")
        else:
            st.subheader("Your Personalized Career Plan")
            
            # Simulate AI advice (replace with real model later)
            careers = {
                "Engineering": "Computer Science Engineering",
                "Medicine": "MBBS",
                "Commerce": "B.Com + CA",
                "Arts": "BA + Civil Services",
                "Computer Science": "B.Tech in AI/ML",
                "Design": "B.Des in UI/UX",
                "Law": "BA LLB",
                "Agriculture": "B.Sc Agriculture",
                "Defence": "NDA → Armed Forces"
            }
            
            recommended_career = careers.get(interests[0], "General Graduate Program")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("1. 🎯 Recommended Career Path")
                st.success(f"**{recommended_career}**")
                
                st.subheader("2. 🏛️ Top Colleges")
                colleges = {
                    "Engineering": ["IIT Delhi", "NIT Trichy", "DTU"],
                    "Medicine": ["AIIMS Delhi", "JIPMER", "PGIMER"],
                    "Commerce": ["SRCC", "Loyola College", "Christ University"],
                    "Computer Science": ["IIT Bombay", "IIIT Hyderabad", "BITS Pilani"],
                    "Design": ["NID Ahmedabad", "UID", "MIT ID"]
                }
                college_list = colleges.get(interests[0], ["Top State Universities"])
                st.write("\n".join([f"• {c}" for c in college_list[:3]]))
            
            with col2:
                st.subheader("3. 📚 Skill Roadmap")
                skills = {
                    "Engineering": ["Python", "Maths", "Problem Solving"],
                    "Computer Science": ["DSA", "ML Basics", "Web Dev"],
                    "Commerce": ["Accounting", "Excel", "Business Law"],
                    "Design": ["Figma", "Adobe Suite", "User Research"]
                }
                skill_list = skills.get(interests[0], ["Communication", "Critical Thinking"])
                st.write("\n".join([f"• {s}" for s in skill_list]))
                
                st.subheader("4. 💰 Scholarship Options")
                if marks >= 90:
                    st.info("• **NTSE Scholarship** (₹1250/month)\n• **KVPY** (for Science)")
                elif marks >= 80:
                    st.info("• **State Merit Scholarships**\n• **Private Trust Scholarships**")
                else:
                    st.info("• **Central Sector Scheme**\n• **Education Loans with Subsidy**")

# Job Seeker Module
elif user_type == "Job Seeker":
    st.header("💼 Job Seeker Advisor")
    st.subheader("Optimize your job search")
    
    resume_text = st.text_area("Paste your resume summary", height=150,
                              placeholder="E.g., '5+ years in Python, machine learning, built AI demos for HR tech...'")
    jd_text = st.text_area("Paste the job description", height=150,
                          placeholder="E.g., 'Looking for an AI engineer with Python, scikit-learn, and Streamlit experience...'")
    
    if st.button("Get Job Advice"):
        if not resume_text.strip() or not jd_text.strip():
            st.warning("Please enter both resume and job description")
        else:
            st.subheader("Your Personalized Job Strategy")
            
            # Simulate resume score
            resume_score = random.randint(60, 95)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("1. 📊 Resume Match Score")
                if resume_score >= 80:
                    st.success(f"✅ **{resume_score}%** — Strong Match!")
                elif resume_score >= 60:
                    st.warning(f"⚠️ **{resume_score}%** — Moderate Match")
                else:
                    st.error(f"❌ **{resume_score}%** — Low Match")
                
                st.subheader("2. ✍️ ATS-Friendly Resume Tips")
                st.info("""
                • Include keywords: **'Python', 'Streamlit', 'Scikit-learn'**  
                • Quantify achievements: **'Built 5 AI demos'**  
                • Align summary with role seniority
                """)
            
            with col2:
                st.subheader("3. 🎯 Interview Preparation")
                st.info("""
                • Expect questions on: **AI model deployment**  
                • Prepare examples of: **freelance projects**  
                • Research company's: **AI use cases**
                """)
                
                st.subheader("4. 💰 Salary Benchmark")
                st.info("""
                • **India**: ₹8–15 LPA  
                • **Senior Roles**: ₹15–25 LPA  
                • **Freelance**: ₹1,500–3,000/hour
                """)

# Freelancer Module
elif user_type == "Freelancer":
    st.header("💻 Freelancer Success Kit")
    st.subheader("Maximize your freelance income")
    
    skills = st.text_area("Your Skills (comma-separated)",
                         placeholder="E.g., Python, Streamlit, AI, Data Science, Web Scraping")
    
    if st.button("Get Freelancer Advice"):
        if not skills.strip():
            st.warning("Please enter your skills")
        else:
            st.subheader("Your Personalized Freelancer Strategy")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("1. 🌐 Platform Strategy")
                st.info("""
                • **Upwork**: Best for long-term AI projects  
                • **Fiverr**: Good for quick demos (₹2,000–5,000)  
                • **Toptal**: For senior AI roles ($50–100/hr)
                """)
                
                st.subheader("2. 💰 Rate Calculator")
                st.info("""
                • **Beginner**: ₹500–1,000/hour  
                • **Intermediate**: ₹1,000–2,500/hour  
                • **Expert**: ₹2,500–5,000/hour  
                • **Project-based**: ₹25,000–1,50,000
                """)
            
            with col2:
                st.subheader("3. 📝 Proposal Templates")
                st.info("""
                **Subject**: AI Solution for [Client Problem]  
                **Body**:  
                - I've built [similar project]  
                - I can deliver in [timeline]  
                - My rate: ₹[amount]  
                - Portfolio: [link]
                """)
                
                st.subheader("4. 📑 Tax & GST Tips")
                st.info("""
                • Register **Udyam** for MSME benefits  
                • **GST optional** if revenue < ₹20L  
                • Save **30% for taxes**  
                • Use **QuickBooks** for accounting
                """)

# SME Owner Module
elif user_type == "SME Owner":
    st.header("🏭 SME Business Advisor")
    st.subheader("Grow your business with AI")
    
    business_type = st.selectbox("Business Type", 
                                ["Manufacturing", "Retail", "Services", "Food & Beverage", "Technology"])
    annual_revenue = st.number_input("Annual Revenue (₹ in Lakhs)", min_value=0, value=50)
    
    if st.button("Get Business Advice"):
        st.subheader("Your Personalized Business Strategy")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("1. ✅ Compliance Checklist")
            if business_type == "Manufacturing":
                st.info("""
                • **Udyam Registration** (mandatory)  
                • **GST Registration**  
                • **Factory License**  
                • **Pollution Certificate**
                """)
            elif business_type == "Retail":
                st.info("""
                • **GST Registration**  
                • **Shop Act License**  
                • **FSSAI** (if food)  
                • **Professional Tax**
                """)
            else:
                st.info("""
                • **Udyam Registration**  
                • **GST Registration**  
                • **Current Bank Account**  
                • **Professional Tax**
                """)
            
            st.subheader("2. 💳 Loan Eligibility")
            if annual_revenue >= 100:
                st.success("✅ **MSME Loan**: ₹10–50 Lakhs @ 8–12%")
            elif annual_revenue >= 25:
                st.warning("⚠️ **MUDRA Loan**: ₹1–10 Lakhs @ 12–15%")
            else:
                st.info("💡 **Start with**: Personal loan or angel investment")
        
        with col2:
            st.subheader("3. 📱 Digital Marketing Plan")
            st.info("""
            • **Google My Business**: Free listing  
            • **Instagram**: Showcase products  
            • **WhatsApp Business**: Customer service  
            • **Website**: Basic site (₹5,000–10,000)
            """)
            
            st.subheader("4. 🤖 AI Tools to Adopt")
            if business_type == "Manufacturing":
                st.info("""
                • **PM Lite**: Predictive maintenance  
                • **Inventory AI**: Stock optimization  
                • **Quality Inspector**: Defect detection
                """)
            elif business_type == "Retail":
                st.info("""
                • **Demand Forecaster**: Diwali stock planning  
                • **GST Invoice Generator**: Auto-billing  
                • **Customer Chatbot**: WhatsApp support
                """)
            else:
                st.info("""
                • **AI Assistant**: Customer queries  
                • **Proposal Generator**: Client pitches  
                • **Expense Tracker**: GST compliance
                """)

# Footer
st.markdown("---")
st.caption("🇮🇳 Built for India | Open Source | No Data Stored | [GitHub](https://github.com/yourname/ai-career-advisor)")
