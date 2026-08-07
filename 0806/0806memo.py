# print("8월 6일 아자아자 화이팅!!!")
# # 8월 5일에 먼저 배운 내용 있음
# # 8월 5일에 다 적어버림..
import numpy as np
import csv

# with open("data/10_mct_tool.csv", "r", encoding="utf-8") as f:
#     rows = list(csv.reader(f))
# header = rows[0]
# body = rows[1:0]

# # 1차원 인덱싱
# arr_1d = np.array([1, 2, 3, 4, 5])
# print(arr_1d[3])  # 4
# list_2d = [[1, 2, 3], [4, 5, 6]]
# # [1, 2, 3] -> 0번 인덱스
# # [4, 5, 6] -> 1번 인덱스
# # 4 -> 0번 인덱스
# # 5 -> 1번 인덱스
# # 6 -> 2번 인덱스
# print(list_2d[1])  # [4, 5, 6]
# print(list_2d[1][1])  # 5

# # 2차원 배열에서 인덱스로 값 뽑기
# arr_2d = np.array(body)
# # print(arr_2d[4, 3])

# # print(np.array(body[4,3])) # Error
# # print(np.array(body)[4, 3])  # 정상 작동
# # 괄호 위치가 다름
# # Error 발생 코드는 np.array에
# # 변환하고자 하는 리스트를 넘기는 위치에서 인덱싱
# # 그러면 결국 np.array는 "18.67"만 받게 됨
# # "18.67"는 str이기 때문에 list를 받지 못해서
# # np.array가 에러를 발생하는 것

# # print(np.array(body)[4, 3])  # 정상 작동
# # np.array가 전달받은 값이 2차원의 리스트
# # np.array를 통해서 정상적으로 배열을 변환
# # 배열로 변환한 뒤에 [4, 3]이라는 인덱스로 접근해
# # 값을 뽑아오는 것

# # 2차원 리스트에서 인덱스로 접근하는 방법
# # 대괄호를 중첩 body[4][3]
# # 2차원 배열에서 인덱스로 접근하는 방법
# # 대괄호에 행, 열을 전달 arr_2d[4, 3]

# # 추가) 배열의 값 수정 가능
# # print(cycle_time_np)
# # [ 2223 15603 15631 15558 15634 15607 15600 15610 15605 15605  2154 15557]
# # 0번 인덱스의 값인 2223을 0으로 변경
# # cycle_time_change = cycle_time_np.copy()
# # .copy()는 현재 변수에 담긴 값을 그대로 복제하는 것
# # cycle_time_change[0] = 0
# # print(cycle_time_change)
# # [    0 15603 15631 15558 15634 15607 15600 15610 15605 15605  2154 15557]
# # 배열도 값 수정 가능
# # ==========================================================
# # 배열의 슬라이싱
# temp = np.array([27, 30, 33, 27, 28])
# print(temp[1:4])  # [30 33 27]
# print(temp[:2])  # [27 30]
# print(temp[1:4].size)  # 3

# print("===")

# # 음수도 가능
# print(temp[::-1].size)  # [28 27 33 30 27]
# # 인덱싱은 값 하나를 뽑아오는 것
# # 슬라이싱은 구역을 추출해서 리스트면 리스트, 배열이면 배열로 돌려줌

# # 2차원 슬라이싱
# temp_2d = np.array(
#     [
#         [27, 30, 33, 27, 28],
#         [87, 76, 92, 81, 85],
#         [27, 30, 33, 27, 28],
#         [87, 76, 92, 81, 85],
#     ]
# )

# print(temp_2d[0:3])
# # [[27 30 33 27 28]
# #  [87 76 92 81 85]
# #  [27 30 33 27 28]]

# print("===")
# print(temp_2d[0:3, 0])  # [27 87 27]
# # 3행까지의 1열 값들을 가져옴

# print("===")
# print(temp_2d[0:2, 1:4])
# # 행 기준으로 2번째 행까지 뽑아옴
# # [27, 30, 33, 27, 28], [87, 76, 92, 81, 85]
# # 열 기준으로 2열부터 4열까지 뽑음
# # [[30, 33, 27]
# # [76, 92, 81]]

# # 실습 1. 특정 구간 꺼내기
# test = np.array([4603, 212, 33, 42346, 258, 6123, 7458, 8908, 9921, 4603])
# print(test[0])
# print(test[-1])
# print(test[1:4])
# print(test[5:])

# # 리더님 답
# # 방법 1. 리스트에서 구간 슬라이싱
# rpm1 = np.array([int(row[4]) for row in body[-10:]])

# # 방법 2. 배열에서 구간 슬라이싱
# rpm2 = np.array(body)[-10:, 4]  # 결과가 문자열의 배열
# rpm2 = rpm2.astype(int)
# # rpm2 = np.array(body)[-10:, 4].astype(int) -> 이것도 됨!
# print(rpm1)
# print(rpm2)
# print("===")

# # 맨 앞, 맨 뒤 값 꺼내기
# print(rpm1[0], rpm1[-1])

# # 두 번째 에서 4번째 값 꺼내기
# print(rpm1[1:4])

# # 하나씩 걸러서 값 꺼내기
# print(rpm1[::2])

# # ========================================

# print(
#     [
#         1,
#         2,
#         3,
#     ]
#     + [4, 5, 6]
# )  # [1, 2, 3, 4, 5, 6]
# # 하나의 리스트로 연결

# # 배열의 연산
# arr_a = np.array([1, 2, 3])
# arr_b = np.array([100, 200, 300])
# print(arr_a + arr_b)  # [101 202 303]
# print(arr_a - arr_b)  # [ -99 -198 -297]
# print(arr_a * arr_b)  # [100 400 900]
# print(arr_a / arr_b)  # [0.01 0.01 0.01]
# print(arr_a % arr_b)  # [1 2 3]
# print(arr_a // arr_b)  # [0 0 0]
# print(arr_a**arr_b)  # [                  1                   0 4157753088978724465]

# arr_c = np.array([1, 2, 3])
# arr_d = np.array([100, 200, 300, 400])
# # print(arr_c + arr_d)
# # ValueError: operands could not be broadcast together with shapes (3,) (4,)
# # 배열 연산은 값의 개수가 동일해야 함

# arr_e = np.array([[1, 2, 3], [4, 5, 6]])
# arr_f = np.array([100, 200, 300])

# print(arr_e + arr_f)
# # [[101 202 303]
# #  [104 205 306]]
# # arr_f = np.array([100, 200, 300])를
# # arr_f = np.array([[100, 200, 300], [100, 200, 300]])로 바꿔 연산

# # arr_g = np.array([[1, 2], [4, 5, 6]])
# # arr_h = np.array([[100, 200, 300], [400, 500, 600]])

# # print(arr_g + arr_h) # ValueError

# # arr_g = np.array([[1, 2], [4, 5, 6]])
# # arr_h = np.array([[100, 200], [400, 500, 600]])
# # print(arr_g + arr_h)  # ValueError

# print("===")
# # 실습 3. 회전수를 0과 1사이로 맞추기
# rpm = np.array([int(row[4]) for row in body[-10:]])
# min_num = min(rpm)  # 1241
# max_num = max(rpm)  # 4987
# avg_rpm = max_num - min_num
# rpm_min_list = rpm - min_num
# rpm_list = rpm_min_list / avg_rpm
# print(rpm_list.round(2))
# # [0.9  0.9  0.   0.9  0.9  0.51 0.9  0.99 0.9  1.  ]

# print("=== 정규화 ===")
# # 정규화 "norm" 이라고 많이 씀
# # 값의 범위를 0~1 사이로 정리하는 것
# # 나머지를 그 사이 비율로 표현
# # 단위와 크기 각기 다른 값들을 0~1 사이라는 같은 기준으로
# # 공평하게 계산하기 위해 사용

# # ==================================================================

# arr_score = np.array([61, 78, 59, 20, 83])
# print(arr_score >= 60)
# # [ True  True False False  True]

# # NumPy 안쓰고 동일하게 출력하기
# score = [61, 78, 59, 20, 83]
# score_result = []
# for i in score:
#     if i >= 60:
#         score_result.append(True)
#     else:
#         score_result.append(False)
# print(score_result)

# print((arr_score >= 60).dtype)  # bool
# print((arr_score >= 60).astype(int))  # [1 1 0 0 1]

# # 불리언 인덱싱
# print(arr_score[arr_score >= 60])
# # [61 78 83]
# # 조건에 만족하는 값만 남김
# # 60을 넘는 값은 어떤 값인지 알 수 있음
# # 조건을 만족하지 못한다면 버려버림
# # 블리언 인덱싱 결과는 기존 크기와 같거나 작아짐

# # np.where
# # 조건을 기준으로 True와 False일 때 치환할 값을 설정할 수 있음
# # np.where(조건, True일_때_치환할_값, False일_때_치환할_값)
# print(np.where(arr_score >= 60, 1, 0))
# print(np.where(arr_score >= 60, "합격", "불합격 ㅋ"))
# print(np.where(arr_score >= 60, arr_score, 0))  # 기준 이하를 0으로

# print(np.where(arr_score >= 60))  # (array([0, 1, 4]),)
# # np.where에 조건만 넘기면 True인 인덱스만 출력
# print(np.where(arr_score >= 60)[0])  # [0 1 4]

# # 다중조건 사용 가능!
# # 18~25도가 쾌적할 때
# arr_temps = np.array([18, 15, 24, 30, 33, 21, 15])

# # 쾌적 온도 구간만 출력
# print(arr_temps[(arr_temps >= 18) & (arr_temps <= 25)])  # [18 24 21]
# # print(np.where((arr_temps[(arr_temps >= 18) and (arr_temps <= 25)]))) # Error
# # and 연산자는 값 하나에 대한 연산을 한 (배열에서 사용 불가)

# print("===")
# # 결과 뒤집기
# print(arr_temps[~(arr_temps > 30)])  # [18 15 24 30 21 15]
# # ~은 부정 연산자로 not과 동일하게 적용

# # 실습4. 저회전 이상 시점 걸러내기
# # 단계
# # ① 회전수와 토크 묶음을 각각 준비
# # ② 회전수가 2000 미만 시점마다 판단해 참거짓 묶음 만들어 출력하기
# # ③ 회전수가 2000 미만이거나 전류가 25을 초과 시점을 참거짓 묶음으로 만들어 출력하기
# # ④ 조건을 만족하는 시점이 각자 몇 개인지 출력하기
# # ⑤ 회전수 2000 미만은 전체의 몇 퍼센트인지, 회전수가 2000 미만이거나 전류가 25초과 시점은 전체의 몇 퍼센트인지 구하기
# # 예상 결과
# # 저회전 횟수와 비율, 저회전이면서 고전류 횟수와 비율

# electric_rpm_1 = np.array([(row[3:5]) for row in body])
# electric_rpm = electric_rpm_1.astype(float)
# True_False_rpm = electric_rpm[:, 1] < 2000
# print("2단계")
# print(True_False_rpm)  # 회전수가 2000미만 판단 결과 출력
# # [False False False False False False False False False False False False
# #  False False False False False False False False  True False False  True
# #  False False  True False False False False False  True False False False
# #  False False False False]
# print("3단계")
# True_False_electric_rpm = []
# for row in electric_rpm:
#     if row[1] < 2000 or row[0] > 25:
#         True_False_electric_rpm.append(True)
#     else:
#         True_False_electric_rpm.append(False)
# print(np.array(True_False_electric_rpm))
# # [False False  True False False False False  True False  True False False
# #  False False False False False False False False  True False False  True
# #  False False  True False False False False False  True False False  True
# #  False  True False False]
# print("4단계")
# print(len(True_False_rpm))  # 40
# total = 0
# for i in True_False_rpm:
#     if i == True:
#         total += 1
# print(total)
# # 회전수가 2000미만인 True의 갯수 # 4개
# count = 0
# for i in True_False_electric_rpm:
#     if i == True:
#         count += 1
# print(count)
# print("5단계")
# print(
#     f"회전수 2000미만 전체 몇 퍼센트인지 : {(total/ len(True_False_rpm))*100}%\n회전수가 2000미만이고 전류가 25 초과인 것이 몇 퍼센트인지 : {count/len(True_False_electric_rpm)*100}%"
# )

# # 리더님 답
# # with open("data/10_mct_tool.csv", "r", encoding="utf-8") as f:
# #     rows = list(csv.reader(f))
# # header = rows[0]
# # body = rows[1:0]

# # # 회전수
# # prac_rpm = np.array([int(row[4]) for row in body])
# # # 전류 1차원 배열
# # prac_elect = np.array(float(row[3]) for row in body)

# # # 회전수 2000 미만 검사 -> bool 배열
# # prac_rpm_bool = prac_rpm < 2000  # 블리언 배열 출력
# # print("저회전 여부 :", prac_rpm_bool)

# # # 회전수 2000 미만 "이거나" 전류 25 초과 검사 -> bool 배열
# # prac_rpm_elec_arr = (prac_rpm < 2000) or (prac_elect > 25)
# # print("저회전이거나 고전류 여부:", prac_rpm_elec_arr)

# # # 각각 True 갯수 구하기
# # prac_rpm_count = prac_rpm_bool.sum()
# # prac_rpm_elec_count = prac_rpm_elec_arr.sum()
# # print("저회전 개수: ", prac_rpm_count)
# # print("저회전이거나 고전류 개수: ", prac_rpm_elec_count)

# # # 전체 대비 비율 구하기
# # prac_rpm_per = prac_rpm_count / len(prac_rpm)
# # prac_rpm_elec_per = prac_rpm_elec_count / len(prac_rpm)
# # print("저회전 비율: ", prac_rpm_per * 100, "%")
# # print("저회전이거나 고전류 비율: ", prac_rpm_elec_per * 100, "%")

# # =================================================================
tall = np.array([153, 169, 173])
