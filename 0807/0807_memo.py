print("8월 7일도 아자아자장! 화이팅!!!")

import numpy as np
import csv

with open("data/10_mct_tool.csv", "r", encoding="utf-8") as f:
    rows = list(csv.reader(f))
header = rows[0]
body = rows[1:]
# rpm = np.array([int(row[4]) for row in body[-10:]]) # 최근 10개 rpm
# rpm = np.array([(row[4]) for row in body]) # 전체 rpm

# ================================================

# 8월 6일 추가 내용들

# axis 개념( 행, 열 방향)
# axis = 0은 위에서 아래로
# 한 열의 값들을 모음 -> 열별 결과 출력 가능
# axis = 1은 왼쪽에서 오른쪽으로
# 한 행의 값들을 모음 > 행병 결과

# 영화

movies = np.array(
    [["Runtime", "Release Year", "Age Rating"], [130, 2016, 13], [156, 2026, 15]]
)

movies_body = movies[1:].astype(int)

print(movies_body.mean())
# 726.0
# 모든 값들에 대한 평균이 출력됨

# 월별 평균을 구하는 방법
print(movies_body.mean(axis=0))
# [ 143. 2021.   14.]
# mean 즉, 평균을 내기 위해 mean() 함수가 값을 더하고 나누는 동작을 함
# 결론적으로 평균 결과는 float 배열로 반환됨

# 행별 평균을 구하는 방법
print(movies_body.mean(axis=1))
# [719.66666667 732.33333333]
# 스파이더맨과 호프라는 영화에 대한 값들을 평균냄
# 사실 현재 데이터셋 기준으로는 행별 평균은 의미가 없음
# 단위가 다른 값들을 섞었기 때문
# 특히 설비 데이터는 열마다 단위가 다르기 때문에
# axis=0을 압도적으로 많이 씀

print("===")

# 회전수와 토크의 평균 구하기
rpm_tok_1 = np.array([(row[4:]) for row in body])
# print(f"회전수 평균 : {rpm_tok.mean(axis=0)}")
rpm_tok = rpm_tok_1.astype(int)
print(f"회전수 평균 과 토크 평균: {rpm_tok.mean(axis=0)}")
# 회전수 평균 과 토크 평균: [4212.625   10.7  ]

# 리더님 답
data = np.array([row[4:] for row in body], dtype=float)

# 행 40개, 열 2개 추출 확인
print(data.shape)

print("열별 평균(회전수, 토크) :", data.mean(axis=0))
# 열별 평균(회전수, 토크) : [4212.625   10.7  ]

print("열별 중앙값(회전수, 토크) :", np.median(data, axis=0))
print("열별 분산(회전수, 토크) :", data.var(axis=0))
print("열별 표준편차(회전수, 토크) :", data.std(axis=0))

datas = np.loadtxt(
    "data/10_mct_tool.csv",
    encoding="utf-8",
    delimiter=",",  # 값을 나누는 기호
    skiprows=1,  # 첫 줄(제목)은 건너뜀
    usecols=4,
)  # 5번째 열 = 회전수

print(datas.shape, datas.dtype)
# (40,) float64

# ==================================================================
print("=== 실습 9. 불러오기부터 통계까지 한 흐름으로 ===")
# 실습 9. 불러오기부터 통계까지 한 흐름으로
rpm_tok_list = np.loadtxt(
    "data/10_mct_tool.csv", encoding="utf-8", delimiter=",", skiprows=1, usecols=(4, 5)
)
rpm = np.array([row[0] for row in rpm_tok_list], dtype=float)
print(rpm)
count = 0
rpm_error = []
for i in rpm:
    if i < 2000:
        count += 1
        rpm_error.append(i)
np.array(rpm_error)
print("rpm과 토크가 몇 열 몇 행이냐 :", rpm_tok_list.shape)
print("rpm과 토크가 어떤 종류의 값이냐 :", rpm_tok_list.dtype)
print(f"이상시점 : {count}개")
print(f"이상 평균 : {sum(rpm_error)/len(rpm_error)}")
print(f"전체 평균 : {round(sum(rpm)/len(rpm), 1)}")

# ======================================================================================
