import pandas as pd  # importing pandas library into the program
import matplotlib.pyplot as plt  # importing matplotlib into the program
import numpy as np  # importing numpy into the program

df = pd.read_csv(r'/Users/evanspencer/Downloads/degrees-that-pay-back_v1-0.csv')  # loading csv file into program

print('\nDataFrame Shape :', df.shape)  # displaying data shape
print('\nDataFrame Head :', df.head())  # displaying the head of dataset
print('\nDataFrame Tail :', df.tail())  # displaying the tail of dataset
print('\nDataFrame Summary :', df.info())  # priniting a summary of the data set

print('\nChecking empty cells :', df.isna())  # checking if the data set has empty cells
print('\nChecking duplicate cells :', df.duplicated())  # checking if the data set has duplicated cells

df.drop([2, 53], axis=0, inplace=True)  # dropping the 2nd row, and the 53rd row, axis means its a row that should
# be deleted, and inplace=True puts the change into the original data frame

df = df.replace(['\$', '\,'], ['', ''], regex=True)  # removing $ and , from the data set

df['StartingMedianSalary'] = df['StartingMedianSalary'].astype(float)  # converting 'StartingMedianSalary' to float so
# the values are now in number form so we can calculate the percent change
df['MidCareerMedianSalary'] = df['MidCareerMedianSalary'].astype(float)  # converting 'MidCareerMedianSalary' to float so
# the values are now in number form so we can calculate the percent change

percent_change = ((df['MidCareerMedianSalary'] - df['StartingMedianSalary']) / df['StartingMedianSalary']) * 100
# calculating the percent change

percent_change = round(percent_change, 2)  # rounding the percent change values to 2 decimal points

df['PercentChangeFromStartingToMidCareerSalary'].fillna(percent_change, inplace=True)  # replacing the
# 'PercentChangeFromStartingToMidCareerSalary' column with the calculated value

df.drop_duplicates(inplace=True)  # removing duplicate cells

df['StartingMedianSalary'] = pd.to_numeric(df['StartingMedianSalary']) #switching 'StartingMedianSalary' to a numeric
# value so it can be sorted
df['MidCareerMedianSalary'] = pd.to_numeric(df['MidCareerMedianSalary']) #switching 'MidCareerMedianSalary' to a numeric
# value so it can be sorted

df = df.sort_values(by='StartingMedianSalary', ascending=True)  # sorting the values of StartingMedianSalary to be ascending
df = df.sort_values(by='MidCareerMedianSalary', ascending=True)  # sorting the values of MidCareerMedianSalary to be ascending

last_seven_rows = df.tail(7)  # defining function to retrieve last 7 rows

mid_career_salary_list = last_seven_rows[
    'MidCareerMedianSalary']  # applying last_seven_rows rows to MidCareerMedianSalary to get the last 7 rows of jt
starting_salary_list = last_seven_rows[
    'StartingMedianSalary']  # applying last_seven_rows rows to StartingMedianSalary to get the last 7 rows of jt
degree_list = last_seven_rows[
    'UndergraduateMajor']  # applying last_seven_rows rows to UndergraduateMajor to get the last 7 rows of jt

x_axis = np.arange((len(degree_list))) # making the x axis the length of the degree list or 7

plt.bar(x_axis -0.2, mid_career_salary_list, width = 0.8, label = 'Mid Career Salary', color = "indianred")
#ploting the top 7 highest earning mid career salaries as a bar plot, with bar width of 0.8 and color indian red
plt.bar(x_axis -0.2, starting_salary_list, width = 0.8, label = 'Starting Salary', color = "mediumaquamarine")
#ploting the corresponding starting salaries to the top 7 highest earning mid career salaries as a bar plot, with bar width of 0.8 and color aquamarine

plt.xlabel("Degrees") #labeling x axis
plt.ylabel("Salary ($)")#labeling y axis
plt.legend() # adding a legend to the graph

plt.show() #showing the graph

