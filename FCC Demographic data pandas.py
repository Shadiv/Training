import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(r'F:\Python\PycharmProjects\Training\data\adult.data.csv')
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].nunique()

    # What is the average age of men?
    average_age_men = df.loc[df['sex']=='Male', 'age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = len(df.loc[df['education']=='Bachelors'])/len(df['education'])

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]['salary'])
    lower_education = len(df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]['salary'])
    high_inc = df.loc[df['salary'] == '>50K']

    # percentage with salary >50K
    higher_education_rich = higher_education / len(high_inc['salary'])
    lower_education_rich = lower_education / len(high_inc['salary'])

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours]

    rich_percentage = len(high_inc.loc[high_inc['hours-per-week']==min_work_hours, 'salary'])/len(high_inc['salary'])

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = high_inc['native-country'].value_counts().idxmax()
    highest_earning_country_percentage = high_inc['native-country'].value_counts().max()/sum(high_inc['native-country'].value_counts())

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df['native-country']=='India') & (df['salary'] == '>50K')]['occupation'].mode()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

df = pd.read_csv(r'F:\Python\PycharmProjects\Training\data\adult.data.csv')
pd.set_option('display.max_columns', None)
race_count = df['race'].nunique()
average_age_men = round(df.loc[df['sex']=='Male', 'age'].mean(), 1)
percentage_bachelors = round(len(df.loc[df['education']=='Bachelors'])/len(df['education'])*100,1)

# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
# What percentage of people without advanced education make more than 50K?

# with and without `Bachelors`, `Masters`, or `Doctorate`
higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
high_inc = df.loc[df['salary'] == '>50K']
high_inc_high_edu = high_inc[high_inc['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
high_inc_low_edu = high_inc[~high_inc['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
# percentage with salary >50K
higher_education_rich = round(len(high_inc_high_edu['salary'])/len(higher_education['salary'])*100,1)
lower_education_rich = round(len(high_inc_low_edu['salary'])/len(lower_education['salary'])*100,1)

# What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = df['hours-per-week'].min()

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
num_min_workers = df.loc[df['hours-per-week'] == min_work_hours]

rich_percentage = len(num_min_workers.loc[num_min_workers['salary']=='>50K'])/len(num_min_workers['salary'])*100

# What country has the highest percentage of people that earn >50K?
highest_earning_by_country = high_inc['native-country'].value_counts()
df_countries = pd.DataFrame(df['native-country'].value_counts())
df_countries['High_inc'] = highest_earning_by_country
df_countries['High_inc'] = df_countries['High_inc'].fillna(0)
# df_countries['country'] = df_countries.index
df_countries['earning_percentage'] = round(df_countries['High_inc']/df_countries['native-country']*100, 1)
highest_earning_country_percentage = df_countries['earning_percentage'].max()
highest_earning_country = df_countries['earning_percentage'].idxmax()
# df_countries.loc[df_countries['earning_percentage'] == highest_earning_country_percentage]['country']

# Identify the most popular occupation for those who earn >50K in India.
top_IN_occupation = df.loc[(df['native-country']=='India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()
print(df.head(5))
print(race_count)
print(average_age_men)
print(percentage_bachelors)
print(min_work_hours)
print(higher_education_rich)
print(lower_education_rich)
# print(num_min_workers)
print(rich_percentage)
print(highest_earning_country)
print(highest_earning_country_percentage)
print(top_IN_occupation)
a = high_inc['native-country'].value_counts()
df_countries = pd.DataFrame(df['native-country'].value_counts())
df_countries['High_inc'] = a
df_countries['High_inc'] = df_countries['High_inc'].fillna(0)
df_countries['rich_percentage'] = round(df_countries['High_inc']/df_countries['native-country']*100, 1)
# print(df_countries.index)
# c = df_countries['earning_percentage'].value_counts().idxmax()
# # print(a)
# print(df_countries)
