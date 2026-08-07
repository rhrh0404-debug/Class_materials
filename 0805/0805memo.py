print(f"8월 5일 화이팅!")
# ndarray : 배열 (우리가 학습했던 리스트와 다른 자료형)
# NumPy에서 데이터를 담는 그릇
# 같은 자료형만 담음 (ex. 정수 배열, 실수 배열)
# 정해진 형태를 가지고 있음 (한 줄로 구성되어 있거나 표 모양)

# =====================================================
# 리스트로 배열의 요소들에 * 5를 하는 코드 작성
py_list = [1, 2, 3, 4, 5]
for i in range(5):
    py_list[i] *= 5
print(py_list)

# 만약 리스트에 *5를 바로 쓴다면?
# print(py_list * 5)
# [5, 10, 15, 20, 25, 5, 10, 15, 20, 25, 5, 10, 15, 20, 25, 5, 10, 15, 20, 25, 5, 10, 15, 20, 25]
# 리스트가 5번 반복된 리스트 반환
# 이어붙이는 작업

# print(py_list + 5)
# TypeError: can only concatenate list (not "int") to list
# 리스트에 int 연산 불가

print(py_list + [5])
# [5, 10, 15, 20, 25, 5]

import numpy as np

# NumPy를 불러와서 np라는 별명으로 사용하겠다 명시

# ndarray : 배열
# 같은 자료형의 값만 담김
np_array = np.array([1, 2, 3, 4, 5])
print(np_array)  # [1 2 3 4 5]
# 배열은 각 값들이 곰마가 아닌 띄어쓰기로 구분되어 작성

# 배열을 사용해서 모든 요소에 * 5 진행
print(np_array * 5)  # [ 5 10 15 20 25]

# 1, 2, 3이라는 값을 가지고 있는 배열 만들기
# np_array2 = np.array(1, 2, 3) # TypeError: array() takes from 1 to 2 positional arguments but 3 were given
# np_array2 = np.array([1], [2], [3]) # TypeError: array() takes from 1 to 2 positional arguments but 3 were given
# np_array2 = np.array([1], [2]) # TypeError: Field elements must be 2- or 3-tuples, got '2'
np_array2 = np.array(
    [[1], [2]]
)  # 2차원 배열 완성! 부르는 법 >> 2차원의 array, nd array라고 함

# 10_mct_tool.csv 파일 데이터 가져와서 출력하기
import csv

with open("data/10_mct_tool.csv", "r", encoding="utf-8") as f:
    rows = list(csv.reader(f))

print(rows)
print("=== 구분선 ===")
# 헤더를 변수에 저장
header = rows[0]
# 데이터(body)만 변수에 저장
body = rows[1:]
print("header :", header)
print("=== 구분선 ===")
print("body :", body)

# 실습. 섭씨 온도를 화씨 온도로 변환 (ndarray)
print("===== 실습. 섭씨 온도를 화씨 온도로 변환 (ndarray) =====")
temps = [32, 30, 33, 29, 30, 31]
import numpy as np

np_temps = np.array([temps])
print(f"측정한 온도(섭씨)를 화씨로 전환한 값들 : {np_temps*1.8 + 32}")

# 배열에서의 자료형 확인
# .dtype를 활용
# 주의사항) 괄호 없이 사용해야 함
np_temps_convertot = np_temps * 1.8 + 32
print(np_temps.dtype)  # int64
print(np_temps_convertot.dtype)  # float64

# 배열의 자료형을 직접 지정하고 싶은 경우
np_ints = np.array([1, 2, 3, 4.5], dtype=int)
# 배열을 생성할 때 array에 인자로 dtype을 전달
print(np_ints.dtype)  # int64
print(np_ints)  # [1 2 3 4]
# 기존 리스트에서 float이었던 값이 있다면
# 소수점 뒤 부분이 버려짐(반올림 아님)

import csv

with open("data/10_mct_tool.csv", "r", encoding="utf-8") as f:
    rows = list(csv.reader(f))

print(rows)
print("=== 구분선 ===")
# 헤더를 변수에 저장
header = rows[0]
# 데이터(body)만 변수에 저장
body = rows[1:]

# 실습(제출해야함)
# 조건
# csv의 온도를 섭씨에서 화씨로 변환
# 현 상황 : body라는 리스트에 헤더를 제외한 행들이 리스트로 담겨있음
# [[2행 데이터], [3행 데이터], [4행 데이터], ...]
# 출력 결과 : 화씨로 변환한 온도 값의 배열 출력
body_np = np.array(body)
for i in range(len(body_np)):
    body_np[i][2] = float(body_np[i][2]) * 1.8 + 32
print(body_np)

# 리더님이 한 정답
fahrenheit_list = []  # 온도값만 저장할 빈 리스트

for row in body:
    celsius = float(row[2])  # 해당 행의 섭씨 온도를 추출
    fahrenheit_list.append(celsius)

# fahrenheit_list에 모든 섭씨 온도가 리스트로 저장됨
# ex). [30, 30, 30, 29, 30, ...]
# 목표인 "배열"로 바꾸기 위해 np.array()를 사용해 NumPy 배열로 변환
fahrenheit_array = np.array(fahrenheit_list)
fahrenheit_array = fahrenheit_array * 1.8 + 32
print(fahrenheit_array)

print("for문을 짧게 작성하는 방법")
# for문을 짧게 작성하는 방법
# 리스트 컴프리헨션
# 위 작업을 한 줄로 줄이는 것
# 형식 : for문을 돌며 반복할 간단한 로직for 변수 in 리스트명

# for row in body:
#     결과리스트.append(리스트에 삽입할 값)

# 리스트 컴프리헨션
# float(row[2]) for row in body

celsius = np.array([float(row[2]) for row in body])
# 대괄호로 감싸주면 for문을 돌면서 뽑아낸 온도값이
# 밖에 있는 대괄호 안에 하나씩 자동으로 들어감

# 배열 안에 있는 모든 값들에 일괄 연산 적용
fahrenheit = celsius * 1.8 + 32
print(fahrenheit)

# =============================================================

# np.arange로 일정 간격의 숫자 만들기

# 인자를 하나만 보내면
# 0부터 인자 -1까지 1씩 커지는 모든 숫자가 담긴 배열 생성
print(np.arange(3))  # [0 1 2]
print(np.arange(10, 15, 2))  # [10 12 14]
# np.arange(시작, 끝, 간격)

# 0부터 100까지 값이 들어간 배열이 필요한 경우
np.arange(100)  # 99까지만 나옴
np.arange(101)  # 100까지 필요하다면 101을 전달해야 함

print(np.arange(10, 0, -2))  # [10  8  6  4  2]
print(np.arange(0, 1, 0.11))  # [0.   0.11 0.22 0.33 0.44 0.55 0.66 0.77 0.88 0.99]

# np.arange로 생성한 배열이 궁금하다면
print(len(np.arange(5)))  # 5

# =====================================================================

# np.linspace
# 특정 구간(시작값과 끝값)을 전달받은 숫자만큼 동등하게 분할
print(np.linspace(5, 6, 3))  # [5.  5.5 6. ]
# 5부터 6까지를 3개로 나누겠다는 의미
print(np.linspace(5, 6, 4))  # [5.         5.33333333 5.66666667 6.        ]

# [0 2 4 6 8] 배열 arrange, linspace로 각자 만들기
print(np.arange(0, 10, 2))
print((np.linspace(0, 8, 5, dtype=int)))

# 초기화 배열 만들기
# 배열을 만든다는 것 자체가 어떠한 값들을 모아두겠다는 뜻
# 초기화 배열을 빈 배열이 아니도록 만드는 이유는
# 크기를 미리 정해두고 하나씩 채우기 위함
# 계산 전에 기본값을 깔아두기 위함

# 0이 5개 삽입된 배열 생성
print(np.zeros(5))  # [0. 0. 0. 0. 0.]

# 1이 3개 삽입된 배열 생성
print(np.ones(3))  # [1. 1. 1.]

# 원하는 값이 원하는 수만큼 삽입된 배열 생성
# full(삽입 할 갯수, 삽입 할 값)
print(np.full(8, 2))  # [2 2 2 2 2 2 2 2]
# full이 int 배열인 이유는 전달한 값의 자료형이 int이기 때문

print(np.full(3, 1.5))  # [1.5 1.5 1.5]
# 삽입할 값이 실수인 경우는 float 배열이 생성됨

# 실습 2. 전류 구간을 같은 간격의 값으로 채우기
print(np.linspace(0, 70, 8, dtype=int))  # [ 0 10 20 30 40 50 60 70]

# 실습 3. 측정 순번 배열 만들기
print(np.arange(0, 40, 5, dtype=int))  # [ 0  5 10 15 20 25 30 35]

# ==================================================

# .ndim
# 배열의 차원 출력

a = np.array([1, 2, 3])  # 1차원 배열
b = np.array([[1, 2, 3], [1, 2, 3]])  # 2차원 배열
# 직접 리스트를 전달한 위 코드에서는 차원을 바로 알 수 있음
# 하지만 변수로 배열을 만드는 경우
# 해당 변수에 담긴 값을 확인하기는 번거로움
# 배열로 바꾸고자 하는 리스트의 길이가 매우 길 경우 확인이 불편함
# 그럴 때 간단하게 배열의 차원을 확인하기 위해 사용
print(a.ndim)  # 1
print(b.ndim)  # 2
# ndim은 속성이기 때문에 괄호를 사용하지 않음
# 1차원은 값이 왼쪽에서 오른쪽으로 나열되어있는 형대
# 2차원은 표 형태로 행과 열이 있는 형태
# 설비 데이터는 보통 행과 열로 이루어져있고.
# 행 = 시점, 열 = 센서값을 가진 2차원의 표 형태임

# print(a.ndim()) # TypeError: 'int' object is not callable 발생

# ==================================================

# .shape
# 배열의 행열을 출력
# 출력 형태 : (행, 열)
# (5,)와 같이 출력되었을 때는
# 1차원 배열을 의미하고, 값이 5개 있다는 의미

d2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(d2.shape)  # (4, 3)
# shape은 튜플을 전달함

rows_count, clos_count = d2.shape
print("d2 배열의 행 :", rows_count)
print("d2 배열의 열 :", clos_count)

# ===============================================================

# .size
# 배열의 크기를 확인
# 배열의 크기 = 행 * 열
print(d2.size)  # 12

# 배열의 shape을 알면 size도 알 수 있음
# size를 알면 shape을 알 수는 없음 (경우의 수가 너무 많기 때문에)

# 아래 두 가지는 같을까?
print(len(d2))  # 4
print(d2.size)  # 12
# len(d2)는 배열의 길이를 의미하고 배열 안의 값 갯수를 출력
# 행의 갯수를 출력함
# 하지만 d2.size는 2차원 배열의 모든 값 갯수를 출력

# ====================================================

type = np.array([1, 2, 3], dtype=float)  # 배열의 자료형을 "지정"

# 이미 float으로 구성된 배열의 자료형을 바꿀 때
# 전부 int로
# int(type) # TypeError 발생


arr1 = np.array([1.5, 2.5, 3.5], dtype=int)
# [1 2 3] -> 소수점 아래를 전부 버림

# 배열의 형변환인 astype도 동일하게 동작
# 소수점 아래 숫자를 전부 버림
arr2 = np.array([1.5, 2.5, 3.5])
# arr2는 float 값을 가진 배열
print(arr2.dtype)  # float64
arr3 = arr2.astype(int)  # [1 2 3]

print(arr2)  # [1.5 2.5 3.5]
# 원본 배열은 바뀌지 않음

# 실습 4. 두 센서 표의 구조 확인하기
dater = np.array([[30, 15.44], [30, 18.69], [30, 62.48], [30, 18.37]])
print(f"차원 : {dater.ndim} / 형태 {dater.shape} / 개수 {dater.size} 출력")

# 실습 5. 전류 자료형 확인하고 정수로 바꾸기
electric = np.array([15.44, 18.69, 62.48, 18.37])
electric_list = electric.astype(int)
print(f"자료형 {electric.dtype} 확인 / 소수점 날린 거 확인 : {electric_list}")

# =============================================================================

# 1차원 -> 2차원 배열로 바꾸기
# reshape(행, 열)

arr999 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# 1차원의 배열

# 아래와 같은 2차원 배열로 바꾸기
# [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]

arr9999 = arr999.reshape(2, 6)
print(arr9999)
print(arr9999.ndim)
print(arr9999.shape)

print(arr999.reshape(-1, 3))  # 열을 3열로 지정하고 행은 자동 계산
print(arr999.reshape(4, -1))  # 행을 4행으로 지정하고 열은 자동 계산
# print(arr999.reshape(-1, -1))
# 행과 열을 모두 -1로 전달할 경우
# 어떻게 해야할지 모르기 때문에 에러 발생

# =================================================================

# 2차원 배열을 1차원으로 평평하게 만들기
# flatten()

arr9 = arr9999.flatten()
print(arr9)

print("8월 5일 하루도 고생했다!!!")

# ==================================================

# 8월 5일에 남은 실습 8월 6일에 함!

# 실습 6. 사이클타임을 표 모양으로 정리하기
cycle_time = []
with open("data/10_mct_tool.csv", "r", encoding="utf-8") as f:
    rows = list(csv.reader(f))
    for row in rows[-1:0:-1]:
        cycle_time.append(int(row[1]))
        if len(cycle_time) == 12:
            break
cycle_time_np = np.array(cycle_time)
cycle_time_2 = cycle_time_np.reshape(-1, 4)
print(cycle_time_np.reshape(-1, 4))
# [[ 2223 15603 15631 15558]
#  [15634 15607 15600 15610]
#  [15605 15605  2154 15557]]
print(cycle_time_2.flatten())
# [[ 2223 15603 15631 15558 15634 15607 15600 15610 15605 15605  2154 15557]]

# ==========================================================================

# 8월 5일 진도 덜 나간 추가 내용들

# 1차원 인덱싱
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d[3])  # 4
list_2d = [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] -> 0번 인덱스
# [4, 5, 6] -> 1번 인덱스
# 4 -> 0번 인덱스
# 5 -> 1번 인덱스
# 6 -> 2번 인덱스
print(list_2d[1])  # [4, 5, 6]
print(list_2d[1][1])  # 5

# 2차원 배열에서 인덱스로 값 뽑기
arr_2d = np.array(body)
print(arr_2d[4, 3])

# print(np.array(body[4,3])) # Error
print(np.array(body)[4, 3])  # 정상 작동
# 괄호 위치가 다름
# Error 발생 코드는 np.array에
# 변환하고자 하는 리스트를 넘기는 위치에서 인덱싱
# 그러면 결국 np.array는 "18.67"만 받게 됨
# "18.67"는 str이기 때문에 list를 받지 못해서
# np.array가 에러를 발생하는 것

print(np.array(body)[4, 3])  # 정상 작동
# np.array가 전달받은 값이 2차원의 리스트
# np.array를 통해서 정상적으로 배열을 변환
# 배열로 변환한 뒤에 [4, 3]이라는 인덱스로 접근해
# 값을 뽑아오는 것

# 2차원 리스트에서 인덱스로 접근하는 방법
# 대괄호를 중첩 body[4][3]
# 2차원 배열에서 인덱스로 접근하는 방법
# 대괄호에 행, 열을 전달 arr_2d[4, 3]

# 추가) 배열의 값 수정 가능
print(cycle_time_np)
# [ 2223 15603 15631 15558 15634 15607 15600 15610 15605 15605  2154 15557]
# 0번 인덱스의 값인 2223을 0으로 변경
cycle_time_change = cycle_time_np.copy()
# .copy()는 현재 변수에 담긴 값을 그대로 복제하는 것
cycle_time_change[0] = 0
print(cycle_time_change)
# [    0 15603 15631 15558 15634 15607 15600 15610 15605 15605  2154 15557]
# 배열도 값 수정 가능
# ==========================================================
# 배열의 슬라이싱
temp = np.array([27, 30, 33, 27, 28])
print(temp[1:4])  # [30 33 27]
print(temp[:2])  # [27 30]
print(temp[1:4].size)  # 3

print("===")

# 음수도 가능
print(temp[::-1].size)  # [28 27 33 30 27]
# 인덱싱은 값 하나를 뽑아오는 것
# 슬라이싱은 구역을 추출해서 리스트면 리스트, 배열이면 배열로 돌려줌

# 2차원 슬라이싱
temp_2d = np.array(
    [
        [27, 30, 33, 27, 28],
        [87, 76, 92, 81, 85],
        [27, 30, 33, 27, 28],
        [87, 76, 92, 81, 85],
    ]
)

print(temp_2d[0:3])
# [[27 30 33 27 28]
#  [87 76 92 81 85]
#  [27 30 33 27 28]]

print("===")
print(temp_2d[0:3, 0])  # [27 87 27]
# 3행까지의 1열 값들을 가져옴

print("===")
print(temp_2d[0:2, 1:4])
# 행 기준으로 2번째 행까지 뽑아옴
# [27, 30, 33, 27, 28], [87, 76, 92, 81, 85]
# 열 기준으로 2열부터 4열까지 뽑음
# [[30, 33, 27]
# [76, 92, 81]]

# 실습 1. 특정 구간 꺼내기
test = np.array([4603, 212, 33, 42346, 258, 6123, 7458, 8908, 9921, 4603])
print(test[0])
print(test[-1])
print(test[1:4])
print(test[5:])

# 리더님 답
# 방법 1. 리스트에서 구간 슬라이싱
rpm1 = np.array([int(row[4]) for row in body[-10:]])

# 방법 2. 배열에서 구간 슬라이싱
rpm2 = np.array(body)[-10:, 4]  # 결과가 문자열의 배열
rpm2 = rpm2.astype(int)
# rpm2 = np.array(body)[-10:, 4].astype(int) -> 이것도 됨!
print(rpm1)
print(rpm2)
print("===")

# 맨 앞, 맨 뒤 값 꺼내기
print(rpm1[0], rpm1[-1])

# 두 번째 에서 4번째 값 꺼내기
print(rpm1[1:4])

# 하나씩 걸러서 값 꺼내기
print(rpm1[::2])

# ========================================

print(
    [
        1,
        2,
        3,
    ]
    + [4, 5, 6]
)  # [1, 2, 3, 4, 5, 6]
# 하나의 리스트로 연결

# 배열의 연산
arr_a = np.array([1, 2, 3])
arr_b = np.array([100, 200, 300])
print(arr_a + arr_b)  # [101 202 303]
print(arr_a - arr_b)  # [ -99 -198 -297]
print(arr_a * arr_b)  # [100 400 900]
print(arr_a / arr_b)  # [0.01 0.01 0.01]
print(arr_a % arr_b)  # [1 2 3]
print(arr_a // arr_b)  # [0 0 0]
print(arr_a**arr_b)  # [                  1                   0 4157753088978724465]

arr_c = np.array([1, 2, 3])
arr_d = np.array([100, 200, 300, 400])
# print(arr_c + arr_d)
# ValueError: operands could not be broadcast together with shapes (3,) (4,)
# 배열 연산은 값의 개수가 동일해야 함

arr_e = np.array([[1, 2, 3], [4, 5, 6]])
arr_f = np.array([100, 200, 300])

print(arr_e + arr_f)
# [[101 202 303]
#  [104 205 306]]
# arr_f = np.array([100, 200, 300])를
# arr_f = np.array([[100, 200, 300], [100, 200, 300]])로 바꿔 연산

# arr_g = np.array([[1, 2], [4, 5, 6]])
# arr_h = np.array([[100, 200, 300], [400, 500, 600]])

# print(arr_g + arr_h) # ValueError

# arr_g = np.array([[1, 2], [4, 5, 6]])
# arr_h = np.array([[100, 200], [400, 500, 600]])
# print(arr_g + arr_h)  # ValueError

print("===")
# 실습 3. 회전수를 0과 1사이로 맞추기
rpm = np.array([int(row[4]) for row in body[-10:]])
min_num = min(rpm)  # 1241
max_num = max(rpm)  # 4987
avg_rpm = max_num - min_num
rpm_min_list = rpm - min_num
rpm_list = rpm_min_list / avg_rpm
print(rpm_list.round(2))
# [0.9  0.9  0.   0.9  0.9  0.51 0.9  0.99 0.9  1.  ]

print("=== 정규화 ===")
# 정규화 "norm" 이라고 많이 씀
# 값의 범위를 0~1 사이로 정리하는 것
# 나머지를 그 사이 비율로 표현
# 단위와 크기 각기 다른 값들을 0~1 사이라는 같은 기준으로
# 공평하게 계산하기 위해 사용

# ==================================================================

arr_score = np.array([61, 78, 59, 20, 83])
print(arr_score >= 60)
# [ True  True False False  True]

# NumPy 안쓰고 동일하게 출력하기
score = [61, 78, 59, 20, 83]
score_result = []
for i in score:
    if i >= 60:
        score_result.append(True)
    else:
        score_result.append(False)
print(score_result)

print((arr_score >= 60).dtype)  # bool
print((arr_score >= 60).astype(int))  # [1 1 0 0 1]

# 불리언 인덱싱
print(arr_score[arr_score >= 60])
# [61 78 83]
# 조건에 만족하는 값만 남김
# 60을 넘는 값은 어떤 값인지 알 수 있음
# 조건을 만족하지 못한다면 버려버림
# 블리언 인덱싱 결과는 기존 크기와 같거나 작아짐

# np.where
# 조건을 기준으로 True와 False일 때 치환할 값을 설정할 수 있음
# np.where(조건, True일_때_치환할_값, False일_때_치환할_값)
print(np.where(arr_score >= 60, 1, 0))
print(np.where(arr_score >= 60, "합격", "불합격 ㅋ"))
print(np.where(arr_score >= 60, arr_score, 0))  # 기준 이하를 0으로

print(np.where(arr_score >= 60))  # (array([0, 1, 4]),)
# np.where에 조건만 넘기면 True인 인덱스만 출력
print(np.where(arr_score >= 60)[0])  # [0 1 4]

# 다중조건 사용 가능!
# 18~25도가 쾌적할 때
arr_temps = np.array([18, 15, 24, 30, 33, 21, 15])

# 쾌적 온도 구간만 출력
print(arr_temps[(arr_temps >= 18) & (arr_temps <= 25)])  # [18 24 21]
# print(np.where((arr_temps[(arr_temps >= 18) and (arr_temps <= 25)]))) # Error
# and 연산자는 값 하나에 대한 연산을 한 (배열에서 사용 불가)

print("===")
# 결과 뒤집기
print(arr_temps[~(arr_temps > 30)])  # [18 15 24 30 21 15]
# ~은 부정 연산자로 not과 동일하게 적용

# 실습4. 저회전 이상 시점 걸러내기
# 단계
# ① 회전수와 토크 묶음을 각각 준비
# ② 회전수가 2000 미만 시점마다 판단해 참거짓 묶음 만들어 출력하기
# ③ 회전수가 2000 미만이거나 전류가 25을 초과 시점을 참거짓 묶음으로 만들어 출력하기
# ④ 조건을 만족하는 시점이 각자 몇 개인지 출력하기
# ⑤ 회전수 2000 미만은 전체의 몇 퍼센트인지, 회전수가 2000 미만이거나 전류가 25초과 시점은 전체의 몇 퍼센트인지 구하기
# 예상 결과
# 저회전 횟수와 비율, 저회전이면서 고전류 횟수와 비율

electric_rpm_1 = np.array([(row[3:5]) for row in body])
electric_rpm = electric_rpm_1.astype(float)
True_False_rpm = electric_rpm[:, 1] < 2000
print("2단계")
print(True_False_rpm)  # 회전수가 2000미만 판단 결과 출력
# [False False False False False False False False False False False False
#  False False False False False False False False  True False False  True
#  False False  True False False False False False  True False False False
#  False False False False]
print("3단계")
True_False_electric_rpm = []
for row in electric_rpm:
    if row[1] < 2000 or row[0] > 25:
        True_False_electric_rpm.append(True)
    else:
        True_False_electric_rpm.append(False)
print(np.array(True_False_electric_rpm))
# [False False  True False False False False  True False  True False False
#  False False False False False False False False  True False False  True
#  False False  True False False False False False  True False False  True
#  False  True False False]
print("4단계")
print(len(True_False_rpm))  # 40
total = 0
for i in True_False_rpm:
    if i == True:
        total += 1
print(total)
# 회전수가 2000미만인 True의 갯수 # 4개
count = 0
for i in True_False_electric_rpm:
    if i == True:
        count += 1
print(count)
print("5단계")
print(
    f"회전수 2000미만 전체 몇 퍼센트인지 : {(total/ len(True_False_rpm))*100}%\n회전수가 2000미만이고 전류가 25 초과인 것이 몇 퍼센트인지 : {count/len(True_False_electric_rpm)*100}%"
)

# 리더님 답
# with open("data/10_mct_tool.csv", "r", encoding="utf-8") as f:
#     rows = list(csv.reader(f))
# header = rows[0]
# body = rows[1:0]

# # 회전수
# prac_rpm = np.array([int(row[4]) for row in body])
# # 전류 1차원 배열
# prac_elect = np.array(float(row[3]) for row in body)

# # 회전수 2000 미만 검사 -> bool 배열
# prac_rpm_bool = prac_rpm < 2000  # 블리언 배열 출력
# print("저회전 여부 :", prac_rpm_bool)

# # 회전수 2000 미만 "이거나" 전류 25 초과 검사 -> bool 배열
# prac_rpm_elec_arr = (prac_rpm < 2000) or (prac_elect > 25)
# print("저회전이거나 고전류 여부:", prac_rpm_elec_arr)

# # 각각 True 갯수 구하기
# prac_rpm_count = prac_rpm_bool.sum()
# prac_rpm_elec_count = prac_rpm_elec_arr.sum()
# print("저회전 개수: ", prac_rpm_count)
# print("저회전이거나 고전류 개수: ", prac_rpm_elec_count)

# # 전체 대비 비율 구하기
# prac_rpm_per = prac_rpm_count / len(prac_rpm)
# prac_rpm_elec_per = prac_rpm_elec_count / len(prac_rpm)
# print("저회전 비율: ", prac_rpm_per * 100, "%")
# print("저회전이거나 고전류 비율: ", prac_rpm_elec_per * 100, "%")

# =================================================================
tall = np.array([153, 169, 173, 163, 169, 187, 198, 167])

# 합계
print(tall.sum())  # 1379

# 평균
print(tall.mean())  # 172,375

# 중앙값
print(np.median(tall))  # 169.0
print(sorted(tall))
# [np.int64(153), np.int64(163), np.int64(167), np.int64(169), np.int64(169), np.int64(173), np.int64(187), np.int64(198)]

# 평균 직접 계산하기
print(tall.sum() / len(tall))  # 172,375 len->말고 .size 가능

# 최대값
print(max(tall))  # 198

# 최솟값
print(min(tall))  # 153

# var
# 분산
# 왜 분산을 구해야해?
# 값이 퍼진 정도를 알 수 있음
# 분산 값이 작으면 값들이 모여있고,
# 분산 값이 크면 값들이 커져있다고 이해

print(round(tall.var(), (2)))  # 173.23

# std
# 표준편차
# 분산의 제곱근
# 실데이터와 동일한 기준으로 값들이 평균에서 얼만큼 떨어져있는지
print(round(tall.std(), (2)))  # 13.16

# 실습. 회전수의 평균, 중앙값, 분산, 표준편차 구하기 (소수점 한 자리 까지)
rpm_arr = np.array([(row[4]) for row in body])
rpm_array = rpm_arr.astype(int)
print("회전수 평균 : ", round(rpm_array.mean(), (1)))
print("회전수 중앙값 : ", round(np.median(rpm_array), (1)))
print("회전수 분산 : ", round(rpm_array.var(), (1)))
print("회전수 표준편차 : ", round(rpm_array.std(), (1)))
print(rpm_array.min(), rpm_array.max())  # 최솟값 : 58, 최댓값 : 4987

print("8월 6일도 고생했다!!!")
