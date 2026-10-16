import streamlit as st
from utils import predict_attrition

st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="🏢",
    layout="wide"
)

EDUCATION_MAPPING = {
    "Below College": 1,
    "College": 2,
    "Bachelor": 3,
    "Master": 4,
    "Doctor": 5
}

SATISFACTION_MAPPING = {
    "Very Low": 1,
    "Low": 2,
    "High": 3,
    "Very High": 4
}

JOB_INVOLVEMENT_MAPPING = {
    "Low": 1,
    "Medium": 2,
    "High": 3,
    "Very High": 4
}

WORK_LIFE_MAPPING = {
    "Bad": 1,
    "Good": 2,
    "Better": 3,
    "Best": 4
}

PERFORMANCE_MAPPING = {
    "Good": 3,
    "Excellent": 4
}

JOB_LEVEL_MAPPING = {
    "Entry Level": 1,
    "Junior": 2,
    "Mid Level": 3,
    "Senior": 4,
    "Executive": 5
}

STOCK_OPTION_MAPPING = {
    "None": 0,
    "Level 1": 1,
    "Level 2": 2,
    "Level 3": 3
}

st.sidebar.title("Project Information")

st.sidebar.subheader("Employee Attrition Prediction")

st.sidebar.divider()

st.sidebar.subheader("**Developer**")
st.sidebar.write("Aditya Verma")

st.sidebar.subheader("**Institution**")
st.sidebar.write("IIHMF, MNNIT Prayagraj")

st.sidebar.subheader("**Program**")
st.sidebar.write("Summer Internship 2026")

st.sidebar.divider()

st.sidebar.subheader("**Dataset**")
st.sidebar.write("IBM HR Analytics Employee Attrition Dataset")

st.sidebar.subheader("**Machine Learning Model**")
st.sidebar.write("Logistic Regression")

st.sidebar.subheader("**Model Accuracy**")
st.sidebar.success("86.05%")


st.title("Employee Attrition Prediction System")

st.caption("Machine Learning Internship Project")

st.markdown("""
This application predicts whether an employee is likely to leave the organization
based on employee-related information using a trained Logistic Regression model.
""")

st.divider()

st.header("Employee Information")

st.subheader("Personal Information")

col1, col2 = st.columns(2)

with col1:

    age = st.slider(
        "Age",
        min_value=18,
        max_value=60,
        value=30
    )

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female"
        ]
    )

    marital_status = st.selectbox(
        "Marital Status",
        [
            "Single",
            "Married",
            "Divorced"
        ]
    )

with col2:

    education = st.selectbox(
        "Education",
        [
            "Below College",
            "College",
            "Bachelor",
            "Master",
            "Doctor"
        ]
    )

    education_field = st.selectbox(
        "Education Field",
        [
            "Life Sciences",
            "Medical",
            "Marketing",
            "Technical Degree",
            "Human Resources",
            "Other"
        ]
    )

    distance_from_home = st.slider(
        "Distance From Home",
        min_value=1,
        max_value=29,
        value=5
    )

st.divider()

st.subheader("Job Information")

col3, col4 = st.columns(2)

with col3:

    department = st.selectbox(
        "Department",
        [
            "Research & Development",
            "Sales",
            "Human Resources"
        ]
    )

    job_role = st.selectbox(
        "Job Role",
        [
            "Sales Executive",
            "Research Scientist",
            "Laboratory Technician",
            "Manufacturing Director",
            "Healthcare Representative",
            "Manager",
            "Sales Representative",
            "Research Director",
            "Human Resources"
        ]
    )

    business_travel = st.selectbox(
        "Business Travel",
        [
            "Travel_Rarely",
            "Travel_Frequently",
            "Non-Travel"
        ]
    )

with col4:

    overtime = st.selectbox(
        "OverTime",
        [
            "No",
            "Yes"
        ]
    )

    job_level = st.selectbox(
        "Job Level",
        [
            "Entry Level",
            "Junior",
            "Mid Level",
            "Senior",
            "Executive"
        ]
    )

    num_companies_worked = st.slider(
        "Number of Companies Worked",
        min_value=0,
        max_value=10,
        value=2
    )

st.divider()

st.subheader("Salary & Performance")

col5, col6 = st.columns(2)

with col5:

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=1000,
        max_value=50000,
        value=5000,
        step=500,
        help="Monthly salary of the employee."
    )

    daily_rate = st.number_input(
        "Daily Rate",
        min_value=100,
        max_value=1500,
        value=800
    )

    hourly_rate = st.number_input(
        "Hourly Rate",
        min_value=30,
        max_value=100,
        value=65
    )

    monthly_rate = st.number_input(
        "Monthly Rate",
        min_value=2000,
        max_value=30000,
        value=14000,
        step=500
    )

with col6:

    percent_salary_hike = st.slider(
        "Percent Salary Hike",
        10,
        25,
        15
    )

    performance_rating = st.selectbox(
        "Performance Rating",
        [
            "Good",
            "Excellent"
        ]
    )

    stock_option_level = st.selectbox(
        "Stock Option Level",
        [
            "None",
            "Level 1",
            "Level 2",
            "Level 3"
        ]
    )

st.divider()

st.subheader("Career Information")

col7, col8 = st.columns(2)

with col7:

    total_working_years = st.slider(
        "Total Working Years",
        0,
        40,
        10
    )

    years_at_company = st.slider(
        "Years At Company",
        0,
        40,
        5
    )

    years_in_current_role = st.slider(
        "Years In Current Role",
        0,
        18,
        3
    )

with col8:

    years_since_last_promotion = st.slider(
        "Years Since Last Promotion",
        0,
        15,
        1
    )

    years_with_current_manager = st.slider(
        "Years With Current Manager",
        0,
        17,
        3
    )

    training_times_last_year = st.slider(
        "Training Times Last Year",
        0,
        6,
        2
    )

st.divider()

st.subheader("Work Environment")

col9, col10 = st.columns(2)

with col9:

    environment_satisfaction = st.selectbox(
        "Environment Satisfaction",
        [
            "Very Low",
            "Low",
            "High",
            "Very High"
        ]
    )

    job_satisfaction = st.selectbox(
        "Job Satisfaction",
        [
            "Very Low",
            "Low",
            "High",
            "Very High"
        ]
    )

    relationship_satisfaction = st.selectbox(
        "Relationship Satisfaction",
        [
            "Very Low",
            "Low",
            "High",
            "Very High"
        ]
    )

with col10:

    work_life_balance = st.selectbox(
        "Work Life Balance",
        [
            "Bad",
            "Good",
            "Better",
            "Best"
        ]
    )

    job_involvement = st.selectbox(
        "Job Involvement",
        [
            "Low",
            "Medium",
            "High",
            "Very High"
        ]
    )

st.divider()

st.subheader("Prediction")

predict = st.button("Predict Employee Attrition",use_container_width=True,type="primary")

if predict:

    education = EDUCATION_MAPPING[education]

    environment_satisfaction = SATISFACTION_MAPPING[environment_satisfaction]

    job_satisfaction = SATISFACTION_MAPPING[job_satisfaction]

    relationship_satisfaction = SATISFACTION_MAPPING[relationship_satisfaction]

    work_life_balance = WORK_LIFE_MAPPING[work_life_balance]

    job_involvement = JOB_INVOLVEMENT_MAPPING[job_involvement]

    performance_rating = PERFORMANCE_MAPPING[performance_rating]

    stock_option_level = STOCK_OPTION_MAPPING[stock_option_level]

    job_level = JOB_LEVEL_MAPPING[job_level]

    employee_data = {

        "Age": age,
        "DailyRate": daily_rate,
        "DistanceFromHome": distance_from_home,
        "Education": education,
        "EnvironmentSatisfaction": environment_satisfaction,
        "HourlyRate": hourly_rate,
        "JobInvolvement": job_involvement,
        "JobLevel": job_level,
        "JobSatisfaction": job_satisfaction,
        "MonthlyIncome": monthly_income,
        "MonthlyRate": monthly_rate,
        "NumCompaniesWorked": num_companies_worked,
        "PercentSalaryHike": percent_salary_hike,
        "PerformanceRating": performance_rating,
        "RelationshipSatisfaction": relationship_satisfaction,
        "StockOptionLevel": stock_option_level,
        "TotalWorkingYears": total_working_years,
        "TrainingTimesLastYear": training_times_last_year,
        "WorkLifeBalance": work_life_balance,
        "YearsAtCompany": years_at_company,
        "YearsInCurrentRole": years_in_current_role,
        "YearsSinceLastPromotion": years_since_last_promotion,
        "YearsWithCurrManager": years_with_current_manager,

        "BusinessTravel": business_travel,
        "Department": department,
        "EducationField": education_field,
        "Gender": gender,
        "JobRole": job_role,
        "MaritalStatus": marital_status,
        "OverTime": overtime
    }

    prediction, probability = predict_attrition(employee_data)

    if prediction == "Yes":
        confidence = probability[1] * 100
    else:
        confidence = probability[0] * 100

    st.divider()

    if prediction == "Yes":

        st.error("Employee is likely to leave the organization.")

    else:

        st.success("Employee is likely to stay in the organization.")

    st.metric(
        label="Prediction Confidence",
        value=f"{confidence:.2f}%"
    )

    st.progress(confidence / 100)

st.divider()

st.caption("Developed by Aditya Verma | Summer Internship 2026 | IIHMF, MNNIT Prayagraj | Powered by Streamlit & Scikit-learn")