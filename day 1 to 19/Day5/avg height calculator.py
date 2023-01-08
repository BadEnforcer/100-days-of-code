student_heights = input("Input a list of student heights ").split()
for num in range(0, len(student_heights)):
    # noinspection PyTypeChecker
    student_heights[num] = int(student_heights[num])
total_sum = 0
total = 0

for height in student_heights:
    total_sum += height
    total = total + 1

result = round(total_sum / total)
print(f"{result}")
