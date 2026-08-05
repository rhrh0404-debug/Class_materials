# temps = [25, 17, 30, 18, 27, 21, 20, 29]
# temps.sort()
# print(temps)
# temps.sort(reverse=True)
# print(temps)
# temps.sort()
# print(temps[::-1])

# temps = [2, 25, 18, 1, 49, 43, 45, 1, 1]

# temps.append(2)
# temps.append(2)
# print(temps.count(2))

# temps.remove(1)
# temps.remove(1)
# temps.remove(1)
# print(temps.count(1))

# temps.sort(reverse=True)
# print(temps.index(49))

# temps = [2, 25, 18, 1, 49, 43, 45, 1, 1]
# temp = [2, 2]
# temps.extend(temp)
# print(temps.count(2))

# temps.sort()
# del temps[0:3]
# print(temps.count(1))

# print(temps[::-1].index(49))

# age = int(input("나이를 입력하세요: "))
# if age >= 19:
# print("성인입니다.")
# if age < 19:
# print("미성년자입니다.")

# score = int(input("점수를 입력하세요: "))
# if score >= 95:
# print("A+")
# elif score >= 90:
# print("A")
# elif score >= 85:
# print("B+")
# elif score >= 80:
# print("B")
# elif score >= 75:
# print("c+")
# elif score >= 70:
# print("C")
# elif score >= 65:
# print("D+")
# elif score >= 60:
# print("D")
# else:
# print("F")

# temp = int(input("측정 온도를 입력하세요: "))
# if temp > 80:
# print("위험")
# elif temp > 60:
# print("주의")
# else temp <= 60:
# print("정상")

# id = "admin"
# pw1 = "1234"
# pw2 = "2345"

# user_id = input("아이디를 입력하세요: ")
# user_pw = input("비밀번호를 입력하세요: ")

# if user_id == id and (user_pw == pw1 or user_pw == pw2):
# print("로그인 성공!")
# else:
# print("로그인 실패")

# a = int(input("1. 숫자를 입력하세요: "))
# b = int(input("2. 숫자를 입력하세요: "))
# c = int(input("3. (1)더하기 (2)빼기 (3)나누기 (4)곱하기 를 입력하세요: "))

# if c == 1:
#     print(a + b)
# elif c == 2:
#     print(a - b)
# elif c == 3:
#     print(a / b)
# elif c == 4:
#     print(a * b)
# else:
#     print("잘못된 번호입니다.")

# 0 , 1, 2, 3, 4
# print(range(5)) = print(range(0,5))

# print(range(0,5,2)) 0, 2, 4

# n = int(input("숫자를 입력하세요: "))
# for i in range(1, n + 1):
#     print(i)
# for i in range(2, n + 1, 2):
#     print("짝수:", i)
# for i in range(n, 0, -1):
#     print(i)

# total = 0
# for i in range(5):
#     total += i
# print(i)

# total2 = 0
# for i in range(1, 5):
#     total2 = 0
#     total2 += i
# print(i)

# # total 0으로 초기화
# total = 0
# # count를 0으로 초기화
# count = 0

# # i가 1부터 5까지 반복
# for i in range(1, 6):
#     # 반복되는 동안 i를 total 덧셈
#     total += i
#     # 반복되는 동안 1씩 증가
#     count += 1

# # count가 0보다 크면 실행
# if count > 0:
#     # 평균
#     print("평균", total / count)

# # for k in range(10):
# #     print(k**2, end=",")

# n = int(input("숫자를 입력하세요"))

# total = 0
# for a in range(1, n + 1):
#     total += a
#     print("합 : ", total)
# print("=" * 20)
# total_1 = 0
# for b in range(1, n + 1, 2):
#     total_1 += b
#     print("1부터 n까지 홀수의 합 : ", total_1)
# print("=" * 20)
# total_2 = 0
# for c in range(2, n + 1, 2):
#     total_2 += c
#     print("2부터 n까지 짝수의 합 : ", total_2)
# print("=" * 20)
# total_3 = 0
# total_4 = 0
# total_5 = 0
# for d in range(2, n + 1, 2):
#     total_3 += d
# for e in range(3, n + 1, 3):
#     total_4 += e
# for f in range(6, n + 1, 6):
#     total_5 += f
#     print("1부터 n까지 2의 배수, 3의 배수 들의 합 : ", (total_3 + total_4 - total_5))
# 2의 배수 3의 배수 저렇게 말고 간단하게 하면
# total = 0
# for d in range(n+1):
#     if d % 2==0 or d%3==0:
#     total += d
#     print(total)

# for i in range(10):
#     if not i % 5:
#         print(i)

# n = int(input("측정 횟수 : "))
# total = 0
# count = 0
# for i in range(n):
#     a = int(input("측정값 : "))
#     total += a
#     count += 1
#     print("평균 : ", total / count)

# for a in range(2, 10):
#     print(f"{a}단")
#     for b in range(1, 10):
#         print(f"{a}*{b}={a*b}")
#     print()

# n = int(input("측정 횟수: "))
# count_1 = 0
# for i in range(n):
#     temp = int(input("측정값 : "))
#     if temp > 80:
#         count_1 += 1
#         print(f"초과 개수: {count_1}")

# print("=" * 20)

# a = int(input("측정 횟수: "))
# total = 0
# count_2 = 0
# for i in range(a):
#     b = int(input("측정값: "))
#     total += b
#     if b > 80:
#         count_2 += 1
#     print(f"평균: {total/a} 초과: {count_2}")

evens = []
odds = []
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list:
    if i % 2:
        evens.append(i)
    else:
        odds.append(i)
print(f"짝수 : {evens} / 홀수 : {odds}")
