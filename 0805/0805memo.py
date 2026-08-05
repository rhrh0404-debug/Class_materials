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
