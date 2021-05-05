import pandas as pd

cols = [2, 3, 4, 5]
df = pd.read_excel('student_scores.xlsx', engine='openpyxl')
print(f'df =\n{df}\n')

df_per_student = pd.read_excel(
    'student_scores.xlsx', usecols=cols, engine='openpyxl')
avgs_per_student = df_per_student.mean(1)
df.loc[:, 'Avg'] = avgs_per_student
avgs_per_class = df.mean()
df.loc[len(df)] = avgs_per_class
df.at[len(df) - 1, 'st_name'] = "Total_Avg"

print(f'avgs_per_student =\n{avgs_per_student}\n')
print(f'avgs_per_class =\n{avgs_per_class}\n')
print(f'df =\n{df}\n')

with pd.ExcelWriter("processed_scores.xlsx") as excel_writer:
    df.to_excel(excel_writer, sheet_name='Students Records')
