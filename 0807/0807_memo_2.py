import numpy as np

F = "data/11_diecasting_series.csv"

data = np.genfromtxt(F, delimiter=",", skip_header=1, usecols=1, encoding="utf-8")

print(data.shape, data.dtype)  # 행 : (50,) 자료형 : float64

# fancy indexing
vals = np.array([1, 2, 3, 4, 5])
pick = np.array([0, 4])
print(vals[pick])  # vals 배열에서 pick 배열에 담긴 인덱스를 추출
# [1 5]
# 뽑고싶은 인덱스 번호를 알고 있으면
# 해당 인덱스에 값을 뽑아낼 수 있음

# =================================================================================

vib = np.array([2.1, 2.3, 2.0, 5.8])
print(np.sort(vib))  # [2.  2.1 2.3 5.8]
print(np.argsort(vib))  # [2 0 1 3]
# argsort는 오름차순 정렬을 한 뒤
# 원본 배열 기준 해당 값의 인덱스를 배열로 반환

# 실제 데이터에서 사이클타임 상위 세 샷의 인덱스 추출
print(np.argsort(data)[-3:])  # [42 47 49]
# 최신 데이터에서 사이클타임이 길어졌다는 것을 추측할 수 있고
# 사이클타임이 길어진 것이 모여있음도 확인 가능
# 곧 고장이 나거나 더 한 번의 샷이 더 오래걸릴 수 있음을
# 예측 가능
# 현재 데이터셋 기준으로는 사이클타임이 긴 샷이
# 점점 잦은 빈도로 더 긴 사이클타임을 가지는 것이라고 해석

# 사이클타임 정령을 내림차순으로 하고싶은 경우
print(np.argsort(data)[::-1][:3])  # [49 47 42]
# [::-1] -> 내림차순으로 정렬
# [:3] -> 처음부터 2번 인덱스까지 출력

# 최댓값, 최솟값의 인덱스 추출

print(data.max())  # 사이클타임이 가장 큰 위치의 값 출력
print(data.argmax())  # 사이클타임이 가장 큰 위치(인덱스) 출력
print(data[np.argmax(data)])  # 사이클타임이 가장 큰 위치(인덱스)로 가장 큰 값 출력
# argmax를 사용하여 사이클타임이 가장 긴 샷의 실린더 압력값도 추출 가능

# argmin은 argmaax와 동일하게 사용하되, 메서드 이름 유의

print("=== 실습 1. 최대 실린더 압력 시점 찾기 ===")
# 실습 1. 최대 실린더 압력 시점 찾기
point__list = np.genfromtxt(
    F, delimiter=",", skip_header=1, usecols=0, encoding="utf-8", dtype=int
)
cylinder_list = np.genfromtxt(
    F, delimiter=",", skip_header=1, usecols=2, encoding="utf-8"
)
print(
    f"중앙값 : {np.median(cylinder_list)}인데, {point__list[cylinder_list.argmax()]}번째 사이클에서 {cylinder_list.max()}값이 나옴"
)

# ===================================================================================

# 변수정리
print("=" * 70)

cycletime_list = np.genfromtxt(
    F, delimiter=",", skip_header=1, usecols=1, encoding="utf-8"
)
print("사이클타임")
print(f"사이클타임 평균 : {cycletime_list.mean()}")
print(f"사이클타임 중앙값 : {np.median(cycletime_list)}")
print(f"사이클타임 최댓값 : {cycletime_list.max()}")
print(f"사이클타임 최솟값 : {cycletime_list.min()}")
print(f"사이클타임 표준편차 : {round(cycletime_list.std(), (1))}")
print(f"사이클타임 최댓값 인덱스 : {cycletime_list.argmax()}번")
print(f"사이클타임이 제일 긴 시점 : {point__list[cycletime_list.argmax()]}")

print("=" * 70)

print("실린더압력")
print(f"실린더압력 평균 : {cylinder_list.mean()}")
print(f"실린더압력 중앙값 : {np.median(cylinder_list)}")
print(f"실린더압력 최댓값 : {cylinder_list.max()}")
print(f"실린더압력 최솟값 : {cylinder_list.min()}")
print(f"실린더압력 표준편차 : {round(cylinder_list.std(), (1))}")
print(f"실린더압력 최댓값 인덱스 : {cylinder_list.argmax()}번")
print(f"실린더압력이 제일 긴 시점 : {point__list[cylinder_list.argmax()]}")

print("=== 리더님이 정리 한 변수정리 ===")
cyc = data = np.genfromtxt(
    F, delimiter=",", skip_header=1, usecols=0, encoding="utf-8"
)  # 시점
cyt = data = np.genfromtxt(
    F, delimiter=",", skip_header=1, usecols=1, encoding="utf-8"
)  # 사이클타임
cyl = data = np.genfromtxt(
    F, delimiter=",", skip_header=1, usecols=2, encoding="utf-8"
)  # 실린더압력
# 사이클타임: 평균, 중앙값, 최댓값, 최솟값, 표준편차, 최댓값의 인덱스, 제일 높았던 시점
cyt_mean = cyt.mean()
cyt_median = np.median(cyt)
cyt_max = cyt.max()
cyt_min = cyt.min()
cyt_std = cyt.std()
cyt_argmax = cyt.argmax()
cyt_peak_cycle = int(cyc[cyt_argmax])
print("사이클타임 평균:", cyt_mean)
print("사이클타임 중앙값:", cyt_median)
print("사이클타임 최댓값:", cyt_max)
print("사이클타임 최솟값:", cyt_min)
print("사이클타임 표준편차:", cyt_std)
print("사이클타임 최댓값의 인덱스:", cyt_argmax)
print("사이클타임 제일 높았던 시점:", cyt_peak_cycle)
# 실린더압력: 평균, 중앙값, 최댓값, 최솟값, 표준편차, 최댓값의 인덱스, 제일 높았던 시점
cyl_mean = cyl.mean()
cyl_median = np.median(cyl)
cyl_max = cyl.max()
cyl_min = cyl.min()
cyl_std = cyl.std()
cyl_argmax = cyl.argmax()
cyl_peak_cycle = int(cyc[cyl_argmax])
print("실린더압력 평균:", cyl_mean)
print("실린더압력 중앙값:", cyl_median)
print("실린더압력 최댓값:", cyl_max)
print("실린더압력 최솟값:", cyl_min)
print("실린더압력 표준편차:", cyl_std)
print("실린더압력 최댓값의 인덱스:", cyl_argmax)
print("실린더압력 제일 높았던 시점:", cyl_peak_cycle)

# ===================================================================

# 소수점 정리
# diff
# 값 사이의 변화량을 계산해서 배열로 반환
# i번째 인덱스와 i+1번째 인덱스의 차이를 계산
# 항상 원본 배열보다 길이가 1짧음
arr1 = np.array([2.0, 2.1, 2.2, 7.0, 7.1])
change = np.diff(arr1)
print(change)  # [0.1 0.1 4.8 0.1]

# 변화량을 알 수 있으며, 이상 구간을 탐지하기 쉬움
print(change.argmax())  # 가장 큰 값의 인덱스
# 1을 더하면 이상인 발생한 시점도 알 수 있음

# 변화가 큰 이상치의 값을 추출할 수 있음
print(arr1[change.argmax() + 1])  # 7.0

# abs
# 절댓값으로 변환
# 변화량은 음수일 수도 있고, 양수일 수도 있음
# 하지만 음양수가 중요한게 아니라 얼만큼 변했는지가 중요하기 때문에
# 비교는 절대값으로 해야 함

arr2 = np.array([1, 1.1, -3.7, 1.1, 1])
change2 = np.diff(arr2)  # [ 0.1 -4.8  4.8 -0.1]
print(change2)
# 이상이 발생한 시점은 -3.7부터이고,
# 변화량 기준으로 4.8이 거진 1은 정상범위

# 절대값 기준으로 변화량을 추적하기 위해
print(np.abs(change))  # [0.1 0.1 4.8 0.1]

# ============================================================================
# # 실습 2. 사이클타임 급변 구간 찾기
print("=== 실습 2. 사이클타임 급변 구간 찾기 ===")
# 사이클타임 = cyt
# 시점 = cyc

cyt_diff = np.diff(cyt)
cyt_diff_abs = np.abs(cyt_diff)
cyt_diff_abs_maxnum = cyt_diff_abs.argmax()
# print(cyt_diff_abs_maxnum)  # 48
print(
    f"{int(cyc[cyt_diff_abs_maxnum])}번과 {int(cyc[cyt_diff_abs_maxnum + 1])}번 사이에서 {round(cyt_diff_abs[cyt_diff_abs_maxnum],(1))}초만큼 변한 것으로 출력"
)

# 실습 3. 측정 오류값 범위 안으로 보정하기
# print("=== 실습 3. 측정 오류값 범위 안으로 보정하기 ===")
# cyl[0] = 9999
# cyl_avg = np.clip(cyl, 100, 300)
# print(
#     f"보정 전 평균은 {round(cyl.mean(),(1))}, 보정 뒤에는 {round(cyl_avg.mean(), (1))}로 원래 수준 부근"
# )
