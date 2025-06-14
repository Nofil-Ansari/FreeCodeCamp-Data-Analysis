import pandas as pd
import kagglehub

# Download latest version
path = kagglehub.dataset_download("nadezhda2019/adultdatacsv")

print("Path to dataset files:", path)
df = pd.read_csv(path + '/adult.data.csv')
print(df.head())
#How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
race_counts = df['race'].value_counts()
print(f'count of {race_counts}')
#What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean()
print(f'Average age of men: {average_age_men:.2f} years')
#What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100
print(f'Percentage of people with a Bachelors degree: {percentage_bachelors:.2f}%')
#What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
higher_education_rich = df[advanced_education & (df['salary'] == '>50K')]
percentage_higher_education_rich = (higher_education_rich.shape[0] / df[advanced_education].shape[0]) * 100
print(f'Percentage of people with advanced education earning >50K: {percentage_higher_education_rich:.2f}%')
#What is the minimum number of hours a person works per week?
min_work_hours = df['hours-per-week'].min()
print(f'Minimum number of hours worked per week: {min_work_hours}')
#What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
min_hours_rich = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]
rich_percentage = (min_hours_rich.shape[0] / df[df['hours-per-week'] == min_work_hours].shape[0]) * 100
print(f'Percentage of people who work {min_work_hours} hours per week and earn >50K: {rich_percentage:.2f}%')
#What country has the highest percentage of people that earn >50K and what is that percentage?
country_counts = df['native-country'].value_counts()
rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
country_percentages = (rich_country_counts / country_counts * 100).fillna(0)
highest_earning_country = country_percentages.idxmax()
highest_earning_country_percentage = country_percentages.max()
print(f'Country with highest percentage of >50K earners: {highest_earning_country} ({highest_earning_country_percentage:.2f}%)')
#rich_percentage = (min_hours_rich.shape[0] / df[df['hours-per-week'] == min_work_hours].shape[0]) * 100
#print(f'Percentage of people who work {min_work_hours} hours per week and earn >50K: {rich_percentage:.2f}%')
#Identify the most popular occupation for those who earn >50K in India.
top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]
print(f'Most popular occupation in India for those earning >50K: {top_IN_occupation}')