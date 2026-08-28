import pandas as pd
df = pd.read_csv('student_performance.csv')
print(df.head())
print("Rows and Columns:", df.shape)
print("Columns:")
for i in df.columns.tolist():
    print(i, end=", ")
print()
if (df.isnull().sum().sum()==0):
    print("No Null values")
else:
    print("Null values exist")
avg_final = df['Final_Score'].mean()
print("Average Final Score:", avg_final)
hs = df.loc[df['Final_Score'].idxmax()]
print("Highest Scorer: ", hs['Student'])
df['Improvement'] = df['Final_Score'] - df['Previous_Score']
ha = df[df['Attendance'] >= 80]
print("Students with Attendance >= 80:\n", ha["Student"])
df_sorted = df.sort_values(by='Final_Score', ascending=False)
print("Sorted DataFrame:\n", df_sorted)
df_sorted.to_csv('processed_student_performance.csv', index=False)





