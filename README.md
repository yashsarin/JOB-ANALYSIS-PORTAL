# JOB-ANALYSIS-PORTAL
This project provides interactive Tableau dashboards to analyze job data across multiple dimensions such as Country, Job Title, Role, Preference, Work Type, Salary, and Experience. The dashboards incorporate conditional filters, time-based visibility restrictions, and color encoding to enhance insights.

1. Relationship Between Country, Job Title, and Role
   
Steps to Create in Tableau:

✅ Connect to Data Source (CSV, Excel, Database, etc.)
✅ Drag Country to the Columns shelf.
✅ Drag Job Title and Role to the Rows shelf.
✅ Choose an appropriate chart type (e.g., Bar Chart or Treemap).
✅ Format the chart by adding labels, tooltips, and filters.
✅ Add the chart to the Dashboard for interactive analysis.


2. Preference vs. Work Type (Conditional Display Based on Time and Filters)
   
Filters Applied:

✅ Work Type = ‘Intern’
✅ Latitude < 10
✅ Country Name does NOT start with A, B, C, or D
✅ Job Title should have ≤ 10 characters
✅ Company Size < 50,000


3. Country-wise Salary Analysis (India & Germany) with Filters
   
Filters Applied:

✅ Country = 'India' OR 'Germany'
✅ Qualification = ‘B.Tech’
✅ Work Type = ‘Full-time’
✅ Experience > 2 years
✅ Job Title IN (‘Data Scientist’, ‘Art Teacher’, ‘Aerospace Engineer’)
✅ Salary Range > $10K
✅ Job Portal = ‘Indeed’
✅ Preference = Female
✅ Job Posting Date < 08/01/2023
✅Set Color Encoding:
  India = 🟠 Orange
  Germany = 🟢 Green

  
Netlify (Deployment & Hosting)
🌍 Live Demo: 🔗https://jobanalysisys.netlify.app/

📊DATASET LINK: 🔗 https://www.kaggle.com/datasets/ravindrasinghrana/job-description-dataset
