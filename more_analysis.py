import pandas as pd
data={
    
    "Name": ["Alice", "Brian", "Catherine", "David", "Eva", "Frank", "Grace", "Henry"],
    "Course": ["Mathematics", "Physics", "Chemistry", "Biology", "Mathematics", "Physics", "Chemistry", "Biology"],
    "Marks": [92, 68, 75, 83, 59, 95, 88, 77],
    "Attendance": [95, 80, 85, 90, 70, 98, 92, 88] #new column
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

#pass or fail
df['Result'] = df['Marks'].apply(lambda x: 'Pass' if x >= 70 else 'Fail')
print("\nDataFrame with Pass/Fail:")
print(df)

#students with above average marks
average_marks = df['Marks'].mean()
above_average = df[df['Marks'] > average_marks]
print("\nStudents with Above Average Marks:")
print(above_average)

#sort marks
sorted_df = df.sort_values(by='Marks', ascending=False)
print("\nSorted DataFrame by Marks:")
print(sorted_df)