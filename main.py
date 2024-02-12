import pandas as pd

# Q.1 :Writer pandas series code to get following output without using dictionary:

# data=[1,4,9,6,7]
# index=['a','x','x',2,'e']
#
# series=pd.Series(data=data,index=index)
# print(series)

# Q.2 : : Writer pandas series code to get following output using dictionary

# creating dectionary
# dictionary={
#     "Bilal": 42,
#     "Ayesha":38,
#     "Hadia":39
# }
#
# series=pd.Series(dictionary)
# print(series)


# Q.3 : : Writer pandas series code to get following output using dictionary:


# Sample dataset
data = {
    'Day': ['2024-02-01', '2024-02-02', '2024-02-03', '2024-02-04', '2024-02-05'],
    'Temperature': [20, 22, 19, 25, 23],
    'Wind Speed': [10, 12, 15, 8, 11],
    'Event': ['Sunny', 'Cloudy', 'Rainy', 'Sunny', 'Snow']
}

# making dataframe
df=pd.DataFrame(data)

print(df)


# Q.4: In extension to above question, you are required to replace index by ['a','b','c','d','e']
index= ['a','b','c','d','e']
df=pd.DataFrame(data,index=index)

print(df)

# Q4: In extension to above Q.3, calculate mean, miximum and minimum for label “temperature”


# calculating mean,max and minimun of temprature
mean_temp = df['Temperature'].mean()
max_temp= df['Temperature'].max()
min_temp= df['Temperature'].min()


# printing data

print("Mean of temprature :",mean_temp)
print("Max of temprature :",max_temp)
print("Min of temprature :",min_temp)

# Import only specific columns from the people dataset
people_data=pd.read_csv("D:/EDA internship/EDA Internship 2.0 Week 2/people.csv",usecols=["First Name", "Sex", "Email","Phone","Job Title"])
pd.set_option('display.max_colwidth', None)
# making sex and job title as index
people_data.set_index(["Sex", "Job Title"], inplace=True)

# Skip following rows [1,5]
people_data=people_data.drop([1,5])


# Export the CSV as “NewPeople.csv”
people_data.to_csv("D:/EDA internship/EDA_ week 2/new_people.csv")
print(people_data)



# Import excel sheet ‘SampleWork.xlsx’
sheet_data=pd.read_excel("D:/EDA internship/EDA Internship 2.0 Week 2/SampleWork.xlsx",sheet_name="Sheet1",skiprows=2,header=1)
print(sheet_data)

print("First and last row")
print(sheet_data.head(1))
print("Last row")
print(sheet_data.tail(1))

# with pd.ExcelWriter("D:/EDA internship/EDA Internship 2.0 Week 2/SampleWork.xlsx", engine='openpyxl', mode='a') as writer:
#     # Write the DataFrame to a new sheet named 'NewSheet'
#     sheet_data.to_excel(writer, sheet_name='NewSheet', index=False)


sdata = {
    'Name': ['Sonia', 'Bilal', 'Hifza', 'kabir', 'Jazim'],
    'Age': [30, 25, 35, 28, 40],
    'Address': ['Lahore', 'Karachi', 'Sialkot', 'Pesh', 'lhr'],
    'Qualification': ['Msc','MA','MCA','Phd','Bsc']
}


AICP_DF=pd.DataFrame(sdata)
AICP_DF["Height"]= [5.1, 6.2, 5.1, 5.2,5.1]
AICP_DF.set_index("Name",inplace=True)
AICP_DF.drop("Bilal",inplace=True)
print(AICP_DF)

print(AICP_DF.loc["Hifza"])
# df1=AICP_DF[["Name","Qualification"]]
# print(df1)