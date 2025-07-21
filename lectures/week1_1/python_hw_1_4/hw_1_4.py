'''
학생 점수 정보
   "Alice" = 85,
   "Bob" = 78,
   "Charlie" = 92,
   "David" = 88,
   "Eve" = 95
'''

# 아래에 코드를 작성하시오.


students = ["Alice", "Bob", "Charlie", "David", "Eve"]
scores = [85, 78, 92, 88, 95]

students_list = []

student_dict = dict(zip(students, scores))

print("1. 학생들의 이름과 점수를 딕셔너리에 저장")
print(f"students type: {type(student_dict)}")
print(f"학생들의 이름과 점수: {student_dict}")
average = (sum([score for score in student_dict.values()])/5)
print(f"2. 모든 학생들의 평균 점수: {average}")
print(f"3. 기준 점수(80점) 이상을 받은 학생 수: {[name for name, score in student_dict.items() if score >= 80]}")
print("4. 점수 순으로 정렬:")
sorted_by_score = dict(sorted(student_dict.items(), key=lambda item: item[1], reverse=True))
for name, score in sorted_by_score.items():
    print(f"{name}: {score}")

print(f"5. 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이: {max(student_dict.values()) - min(student_dict.values())}")
print(f"6. 각 학생의 점수가 평균보다 높은지 낮은지 판단:")
for name, score in student_dict.items():
    if score > average:
        print(f"{name} 학생의 점수({score})는 평균 이상입니다.")
    elif score < average:
        print(f"{name} 학생의 점수({score})는 평균 이하입니다.")
    else:
        print(f"{name} 학생의 점수({score})는 평균입니다.")