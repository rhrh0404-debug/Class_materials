# i = 0

# while i <= 3:
#     i += 1
#     print(i)

# print("반복문이 끝났습니다")

# answer = 7
# guess = 0

# while guess != answer:
#     guess = int(input("맞혀 보세요"))

# print("정답입니다")

# while True:
#     x = input("입력 (q=종료):")
#     if x == "q":
#         break
# print("입력:", x)

# n = int(input("최대 횟수를 입력하세요"))
# for i in range(n):
#     v = int(input("측정값: "))
#     if v > 80:
#         print("이상값 발견, 중단")
#         break
#     print("정상")

# total = 0
# n = int(input("횟수"))
# for i in range(n):
#     v = int(input("측정값"))
#     if v < 0:
#         continue
#     total += v
# print(f"합계 : {total}")

# n = int(input("입력 횟수:"))
# first = int(input("1번째 값:"))
# max_value = first
# mini_value = first
# for i in range(n):
#     next_score = int(input("2번째 값:"))
#     if max_value < next_score:
#         max_value = next_score
#     if mini_value > next_score:
#         mini_value = next_score
# print(f"최대값 : {max_value}\n 최솟값 : {mini_value}")

# flag = False
# n = int(input("횟수를 입력하세요"))
# for i in range(n):
#     count = int(input("측정값 :"))
#     if count > 80:
#         flag = True
#         break
#     if count <= 80:
#         flag = False
# if flag:
#     print("발견")
# else:
#     print("없음")

# n = int(input("횟수를 입력하세요"))
# total = 0
# count = 0
# flag = False
# for i in range(n):
#     v = int(input("측정값 :"))
#     total += v
#     if v > 80:
#         count += 1
#         flag = True
# print(f"평균 : {total/n}, 초과개수 : {count}, 이상{flag}")

# temps = [20, 32, 29, 31, 50, 1]
# for i in temps:
#     if i >= 30:
#         print(f"{i}, 고온주의")
#     elif i < 30:
#         print(f"{i}, 고온은 아니야!")

# hours = [5, 3, 7, 12, 11, 9, 3]
# for i in hours:
#     if i >= 5 and i <= 10:
#    if 5 <= i <= 10:       둘 다 가능
#         print(i)

# temps = [10, 32, 22, 50, 38, 4, 20]
# max_value = temps[0]
# min_value = temps[0]
# for i in temps:
#     if i > max_value:
#         max_value = i
#     if i <= min_value:
#         min_value = i
# print(f"최대값 : {max_value}, 최솟값 : {min_value}")

# temps = [32, 36, 31, 30, 29, 27, 12, 28]
# total = 0
# count = 0
# for i in temps:
#     if i > 30:
#         total += i
#         count += 1
#     elif i < 30: 이건 안적어도 됨!
#         continue
# print(f"합 : {total}, 개수 {count}, 평균 : {total/count}")

# temps = [25, 32, 29, 36, 27, 31, 24]
# list = []
# for i in temps:
#     if i > 31:
#         list.append(i)
# print(list)

# temps = [25, 32, 29, 36, 27, 31, 24]
# list = []
# for i in temps:
#     list.append(i * 1.8 + 32)
# print(list)

temps = [25, 32, 29, 36, 27, 31, 24]
total = 0
count = 0
total_2 = 0
list = []
for i in temps:
    total += i
    if i > 30:
        list.append(i)
        count += 1
        total_2 += i
print(f"전체 평균 {total/len(temps)}, 고온 개수 : {count}, 고온 평균 : {total_2/count}")
