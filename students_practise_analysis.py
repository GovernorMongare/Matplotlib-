import pandas as pd

data={
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Grade': ['A', 'B', 'A', 'C'],
    'Course': ['Math', 'Science', 'History', 'Art'],
    'City': ['Nairobi', 'Kisumu', 'Mombasa', 'Eldoret']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
