# def greet(a):
#     print("점검을 시작합니다")
#     print("장비를 착용하세요")

# def greet():
#     print("점검 시작")  # 함수 안
# print("프로그램 종료")  # 함수 밖

# 함수_실습1
# def greet(temp_check):
#     print("측정 온도 값:")
# greet()


# 함수_실습2
# def start_sensor():
#     print("점검을 시작합니다")
#     print("안전 장비를 확인하새요")
#     print("기록을 준비하세요")


# sensor = ("압축기A", "펌프1", "믹서B")
# for i in sensor:
#     print(i)
#     start_sensor()


# 함수_실습4
# def line():
#     print("=" * 20)


# def start_Sensor():
#     print("점검을 시작합니다")
#     print("기록을 준비하세요")


# line()
# start_Sensor()
# line()
# start_Sensor()


# 함수_기본_연습문제1
# def start_inspection():
#     print("[점검 시작]]")
#     print("보호 장비를 확인하세요.")
#     print("점검 기록지를 준비하세요.")


# start_inspection()

# 함수_기본_연습문제2
# [제어실] 점검 준비
# [제어실] 펌프 호출
# 펌프 1: 압력 확인
# 펌프 2: 기록 완료
# [제어실] 다음 설비로 이동


# 함수_기본_연습문제3
# def check_pump_safety():
#     print("펌프 안저 점검을 시작합니다.")


# check_pump_safety()

# 함수_기본_연습문제4
# def show_inspection_notice():
#     print("안전모와 장갑을 착용하세요")
#     print("점검 결과를 기록하세요")

# show_inspection_notice()
# show_inspection_notice()
# show_inspection_notice()


# 함수_기본_연습문제5
# def show_inspection_notice():
#     print("점검을 시작합니다")
#     print("보호 장비를 확인하세요")
#     print("기록지를 준비하세요")


# sensor_name = ("압축기A", "펌프 1", "보일러 2")
# for i in sensor_name:
#     print(i)
#     show_inspection_notice()

# 함수_기본_연습문제6
# def print_line():
#     print("=" * 20)


# def show_safety_notice():
#     print("안전모와 장갑을 착용하세요.")
#     print("점검 기록지를 준비하세요.")


# def inspect_compressor():
#     print_line()
#     print("압축기 A 점검시작")
#     show_safety_notice()


# def inspect_pump():
#     print_line()
#     print("펌프 1 점검시작")
#     show_safety_notice()


# inspect_compressor()
# inspect_pump()


# def check(name):
#     print(name + "점검을 시작합니다")


# check("펌프 1", "압축기 A")


# 실습1_매개변수 1개 함수 만들기
# def start_inspection(name):
#     print(name + " 점검 시작")


# start_inspection("압축기A")
# start_inspection("펌프1")

# 메모
# def report(name, temp):
#     print(name + ": " + str(temp))


# report(name="압축기A", temp=75.3)
# report(temp=73.3, name="압축기A")


# 실습 3. 키워드 인자로 함수 호출하기
# def report(name, temp):
#     print(name, temp)
# report(temp=78, name="모터")
# report("펌프", temp=92)

# 메모
# def calc_average(a, b):
#     return (a + b) / 2


# avg = calc_average(75.3, 88.0)
# print("평균 온도:", avg)


# 메모
# def check(temp):
#     return temp
#     print("실행 안 됨")


# print(check(75))


# 실습4_반환값으로 간단 계산기 만들기
# def average(a, b):
#     return (a + b) / 2


# avg = average(80, 90)
# print(avg)
# print(avg + 5)


# 메모
# def min_max(values):
#     return min(values), max(values)


# result = min_max([75.3, 88.0, 49.1])
# print(result)


# 실습5. 센서 통계 함수 만들기
# def min_max(values):
#     return min(values), max(values), sum(values) / len(values)


# low, high, avg = min_max([78, 92, 85])
# print(low, high, avg)


# 함수, 매개변수 연습문제 1
# def start_check(equipment):
#     print(equipment, "점검시작")


# start_check("압축기A")
# start_check("순환펌프B")

# 함수, 매개변수 연습문제 2
# 냉각기A 상태기록
# 냉각기B 상태기록
# 호출할 때 마다 equipment에 넣는 문자 + 상태기록
# 문제를 기준으로 처음에 eauipment에는 냉각기A 그 다음에는 냉각기B가 들어가서 호출되어 나옴


# 함수, 매개변수 연습문제 3
# def report_temperature(equipment, temperature):
#     print(equipment, temperature, "도")


# report_temperature("모터", 78)
# report_temperature("펌프", 92)


# 함수, 매개변수 연습문제 4
# def report_vibration(equipment, vibration):
#     print(equipment, "진동", vibration)


# report_vibration(vibration=4.2, equipment="송풍기")
# report_vibration(equipment="펌프", vibration=3.8)


# 함수, 매개변수 연습문제 5
# def calc_average(num_1, num_2):
#     return (num_1 + num_2) / 2


# average = calc_average(80, 90)
# print(average)
# print(average + 5)


# 함수, 매개변수 연습문제 6
# def sensor_summary(lo, hi):
#     return lo, hi, (lo + hi) / 2


# low, high, avg = sensor_summary(78, 92)
# print("최저", low)
# print("최고", high)
# print("평균", avg)

# 메모
# def report(name, value, unit="도"):
#     print(name + ":", str(value) + unit)


# report("압축기", 75.3)
# report("펌프", 7.2, "bar")


# 메모
# def grade(temp, limit=80):
#     if temp > limit:
#         return "점검필요"
#     elif temp < limit:
#         return "정상"


# grade(95, limit=90)

# =======================================================
# 실습1 기본값 인자 함수 만들기
# def status(temp, limit=90):
#     if temp > limit:
#         print("경고")
#     if temp < limit:
#         print("정상")


# status(78)
# status(95)
# status(50, limit=40)

# 메모
# x = 50


# def change():
#     x = 20 #함수 안 x(별개)


# change() #출력 안 됨
# print(x) #출력 10


# 실습2 지역변수 관찰하기
# def temp():
#     result = 10 + 20
#     print(result)


# temp()


# 실습3 처리 흐름 만들기
# def average(a, b):
#     return (a + b) / 2


# def judge(value):
#     if value > 90:
#         print("경고")
#     else:
#         print("정상")


# avg = average(80, 90)
# judge(avg)


# 실습4 센서 분석 함수 세트 만들기
# def average(values):
#     return sum(values) / len(values)


# def status(avg, limit=90):
#     if avg > limit:
#         print(avg, "경고")
#     else:
#         print(avg, "정상")


# avg = average([78, 92, 85])
# status(avg)


# 함수 설계와 활용 연습문제1
# def report_temperature(equipment, value, unit="도"):
#     print(equipment, value, unit)


# report_temperature("압축기A", 75)
# report_temperature("펌프1", 7.2, "bar")


# 함수 설계와 활용 연습문제2
# unit="도"라는 매게변수가 제일 앞에오면 오류가 납니다
# 항상 매개변수는 값이 바뀌지않는 것이 맨 앞에 와야함.
# def record_Sensor(equipment,value,unit="도",):
#     print(equipment, value, unit)


# record_Sensor("모터A", 82)
# record_Sensor("펌프2", 8.1, "bar")


# 함수 설계와 활용 연습문제3
# def show_limit(equipment, limit=90):
#     print(equipment, "기준", limit)


# show_limit("압축기A")
# show_limit(equipment="펌프1", limit=70)


# 함수 설계와 활용 연습문제4
# def make_message(equipment):
#     result = equipment + " 점검완료"
#     return result


# result = make_message("모터A")
# print(result)


# 함수 설계와 활용 연습문제5
# def judge_temperature(value, limit=90):
#     if value > limit:
#         result = "경고"
#     else:
#         result = "정상"
#     return result


# def report_result(equipment, result):
#     print(equipment, result)


# result = judge_temperature(95)
# report_result("압축기A", result)


# 함수 설계와 활용 연습문제6
# def judge_temperature(value, limit=90):
#     if value > limit:
#         result = "경고"
#     else:
#         result = "정상"
#     return result


# def print_report(equipment, value, result):
#     print(equipment, value, "도", result)


# def run_inspection(equipment, value, limit=90):
#     result = judge_temperature(value, limit)
#     print_report(equipment, value, result)


# run_inspection("압축기A", 85)
# run_inspection("펌프1", 95, limit=100)
