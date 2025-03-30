import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import pytz

def check_time_window():
    """Check if current time is between 3 PM and 5 PM IST."""
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).time()
    return current_time >= datetime.strptime("15:00:00", "%H:%M:%S").time() and \
           current_time <= datetime.strptime("17:00:00", "%H:%M:%S").time()

# Sample DataFrame for demonstration
data = pd.DataFrame({
    'Country': ['India', 'Germany', 'USA', 'France', 'India', 'Germany'],
    'Job Title': ['Data Scientist', 'AeroSpace Engineer', 'AI Engineer', 'ML Engineer', 'Art Teacher', 'Data Scientist'],
    'Role': ['Senior', 'Junior', 'Mid', 'Senior', 'Junior', 'Mid'],
    'Preference': ['Female', 'Male', 'Female', 'Female', 'Female', 'Male'],
    'Work Type': ['Intern', 'Full time', 'Intern', 'Full time', 'Full time', 'Intern'],
    'Latitude': [5, 15, 8, 12, 3, 9],
    'Company Size': [10000, 40000, 30000, 60000, 20000, 10000],
    'Experience': [3, 5, 2, 4, 6, 3],
    'Salary': [15000, 20000, 12000, 25000, 18000, 13000],
    'Job Portal': ['Indeed', 'LinkedIn', 'Indeed', 'Monster', 'Indeed', 'Indeed'],
    'Posting Date': ['2023-01-07', '2023-02-10', '2022-12-30', '2023-01-05', '2022-12-15', '2022-11-25']
})

data['Posting Date'] = pd.to_datetime(data['Posting Date'])

# Chart 1: Country, Job Title, and Role
plt.figure(figsize=(10, 5))
sns.countplot(data=data, x='Country', hue='Job Title')
plt.title("Country vs Job Title and Role")
plt.xticks(rotation=45)
plt.show()

# Chart 2: Preference vs Work Type (Filtered)
if check_time_window():
    filtered_data = data[(data['Work Type'] == 'Intern') & (data['Latitude'] < 10) &
                         (~data['Country'].str.startswith(('A', 'B', 'C', 'D'))) &
                         (data['Job Title'].str.len() <= 10) & (data['Company Size'] < 50000)]
    
    plt.figure(figsize=(10, 5))
    sns.countplot(data=filtered_data, x='Preference', hue='Work Type')
    plt.title("Preference vs Work Type (Intern)")
    plt.show()

# Chart 3: Country, Qualification, Work Type, and Job Title (Filtered)
if check_time_window():
    filtered_data = data[(data['Country'].isin(['India', 'Germany'])) & (data['Qualification'] == 'B.tech') &
                         (data['Work Type'] == 'Full time') & (data['Experience'] > 2) &
                         (data['Job Title'].isin(['Data Scientist', 'Art Teacher', 'AeroSpace Engineer'])) &
                         (data['Salary'] > 10000) & (data['Job Portal'] == 'Indeed') &
                         (data['Preference'] == 'Female') & (data['Posting Date'] < '2023-01-08')]
    
    plt.figure(figsize=(10, 5))
    colors = {'India': 'orange', 'Germany': 'green'}
    
    for country in filtered_data['Country'].unique():
        subset = filtered_data[filtered_data['Country'] == country]
        sns.countplot(data=subset, x='Job Title', color=colors[country], label=country)
    
    plt.legend()
    plt.title("Filtered Job Titles by Country")
    plt.xticks(rotation=45)
    plt.show()
