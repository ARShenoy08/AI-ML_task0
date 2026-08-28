import numpy as np
hours_studied = np.array([4, 6, 2, 8, 5, 9, 3, 7])
attendance = np.array([85.0, 90.5, 60.0, 95.0, 80.0, 98.0, 70.0, 88.5])
previous_scores = np.array([65, 72, 50, 88, 70, 92, 58, 81])
final_scores = np.array([70, 78, 52, 90, 72, 95, 61, 84])
print("Hours studied shape: ",hours_studied.shape)
print("Attendance shape: ",attendance.shape)
print("Previous scores shape: ",previous_scores.shape)
print("Final scores shape: ",final_scores.shape)
print("Hours studied data type",type(hours_studied))
print("Attendance data type",type(attendance))
print("Previous scores data type",type(previous_scores))
print("Final scores data type",type(final_scores))
print("Mean final score: ",np.mean(final_scores))
print("Max final score: ",np.max(final_scores))
print("Min final score: ",np.min(final_scores))
print("Standard deviation final score: ",np.std(final_scores))
final_scores=final_scores+5
b=final_scores >= 75
print("Scores greater than 75: ",end="")
for i in final_scores[b]:
    print(i,end=", ")