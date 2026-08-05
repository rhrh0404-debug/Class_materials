print("8월 4일 시작!!!")
# temp = int("삼십")


# ValueError: invalid literal for int() with base 10: '삼십'
# ValueError
#  - 오류의 종류
#  - 값에 문제가 있다는 의미

# invalid literal for int() with base 10: '삼십'
# - 오류에 대한 설명
# - "삼십"은 10진수의 숫자가 아니다 라는 설명

# [그 위 에러 발생 위치]
# File "c:\Users\coco\Desktop\Class_materials\0802\0802memo.py", line 2, in <module>
#   temp = int("삼십")
#         ~~~^^^^^^^^
# 파일의 이름(위치 경로 포함) 정보와
# 해당 파일 내 몇 번째 줄에서 에러가 발생하는지
# 에러가 발생한 코드 자체도 출력
# 여기서 알려주는 코드 줄은 정확하지 않기 때문에
# 위 아래 3줄까지는 같이 확인

# =======================================================================================
# 이 전체 내용을 트레이스백 이라 함!
# File "c:\Users\coco\Desktop\Class_materials\0802\0802memo.py", line 2, in <module>
#     temp = int("삼십")
#            ~~~^^^^^^^^
# ValueError: invalid literal for int() with base 10: '삼십'

# 실습 1. 트레이스백으로 에러 읽기
# age = "3짤"
# int(age)
# line 33, in <module> 33번째 줄에서 에러 발생!
# ValueError: invalid literal for int() with base 10: '3짤'
# "3짤"은 10진수의 숫자가 아니다 라는 설명
# age = 3 으로 한 후 print할 때 "살"을 추가할 것

# temp = 5 / 0
# line 39, in <module> 39번째 줄에서 에러 발생!!!
# ZeroDivisionError: division by zero
# 0으로 나누기 오류!!
# 0으로 나누는게 아니라 0을 제외한 수로 나눌 것

# word = adc
# line 45, in <module> 45번째 줄에서 에러 발생!!!
# NameError: name 'adc' is not defined
# 이름 'adc'는 정의되어 있지 않다
# word = "adc" 로 하여 정의하거나
# abc = "어떤 불라불라한 내용"으로 정의할 것!

# ===========================================================

# try -except문
# try : 에러가 발생할 수 있는 위험한 코드 작성
# except : 에러가 발생했을 때 이에 대응하는 코드

# num = input("숫자를 입력하세요")
# try:
#     temp = int(num)
#     print(f"입력하신 숫자는 {temp}입니다.")
# except:
#     print("입력하신 값은 숫자가 아닙니다")

# print(f"입력하신 숫자는 {temp}입니다.")
# num에 저장된 사용자 입력값은 숫자로 변환할 수 없는 경우
# except문으로 넘어가기 때문에 temp라는 변수가 존재하지 않아서
# 에러가 발생

# 특정 에러에 대해서 대응 코드를 작성하고 싶은 경우
# num2 = input("숫자를 입력하세요")

# try:
#     temp2 = int(num2)
#     print(f"입력하신 숫자는 {temp2}입니다.")
# except NameError:
#     print("NameError 발생")
# except:
#     print("모르는 에러 발생")

# ===============================================================
# 실습 2. try-except로 오류 넘기기
# 조건
# 온도를 입력값으로 받기
# 입력받은 온도는 숫자(float, int 마음대로)로 변환
# 숫자로 변환을 성공했다면 온도 출력
# 만약 숫자로 변환이 불가능하다면 경고문 출력
# 빈 값이 들어왔다면 값을 입력하라는 경고문 출력
# 정상적인 값을 입력받을 때 까지 계속 입력 받아야 함
# 정상적인 값을 입력받아 온도를 출력했다면 "프로그램 종료"라고 출력
# while True:
#     try:
#         temp = input("측정한 온도를 입력하세요")
#         if temp.strip() == "":
#             print("빈 값을 입력했습니다. 다시 입력하세요")
#             continue
#         print(f"측정한 온도는 {float(temp)}입니다.")
#         print("프로그램 종료")
#         break
#     except ValueError:
#         if not temp == "":
#             print(f"\n측정한 값{temp}이(가) 잘못되었습니다. 다시 입력하세요")
#             continue

# =================================================================================
# finally 실습
# 조건
# 09_ict_inspection.csv with open을 사용하지 않고 열기
# 측정값이 0이거나 값이 없는 행만 새로운 csv 파일에 삽입
# finally 사용해서 파일 안전하게 닫기

# import csv

# try:
#     file = open("data/09_ict_inspection.csv", "r", encoding="utf-8")
#     new_file = open(
#         "data/09_ict_inspection_new_file.csv", "w", encoding="utf-8", newline=""
#     )
#     reader = csv.reader(file)
#     header = next(reader)
#     writer = csv.writer(new_file)
#     writer.writerow(header)
#     for row in reader:
#         if row[2] != "" and float(row[2]) != 0:
#             writer.writerow(row)
# finally:
#     file.close()
#     new_file.close()

# =================================================================================
# pass와 continue

# try:
#     for i in range(5):
#         print(i)
# finally:
#     pass

# try:
#     print(float("pass"))
# except:
#     pass
# print("나는 에러나도 그냥 어떤 처리도 없이 계속 코드가 실행됐으면 좋겠어")

# 아래 for문은 에러가 절대 발생하지 않음
# 그럼에도 try에 감싸져있기 때문에
# 무조건!! except 혹은 finally를 사용해야하고
# finally에도 실행할 코드가 없기 때문에 pass를 작성한 것.
# try:
#     for i in range(5):
#         if i % 2 == 0:
#             continue  # 반복문 안에서만 사용할 수 있음
#         print(i)  # 홀수만 출력
# finally:
#     pass
# # try를 언제나 항상 써야 하는 것은 아님을 보여주는 예시

# with open(
#     "data/09_ict_inspection.csv", "r", encoding="utf-8"
# ) as f:  # data/09_ict_inspection.csv
#     rows = f.readlines()  #
#     total = 0
#     skip_count = 0
#     for line in rows[1:]:  # 헤더 제외
#         # 해당 행의 값들을 문자열 리스트로 저장
#         # ex) "2197,E2,0.0,5000.0,2310.0,-3750.0,OK" -> ['2197', 'E2', '0.0', '5000.0', '2310.0', '-3750.0', 'OK']
#         cols = line.split(",")  # 해당 행의 값들을 문자열 리스트로 저장
#         try:
#             total += float(cols[2])
#         except (ValueError, IndexError):
#             skip_count += 1  # 건너뛴 횟수 카운팅
#             continue  # 불량 줄은 건너뜀
#     print(f"총 합계 : {total, 1}, 건너뛴 줄 수 : {skip_count}")

# as e 활용
# print("=== as e 활용 ===")
# try:
#     int("as e로 에러 정보 확인해보기")
# except ValueError as error:
#     print(error)

# ======================================================================
# print("=== raise로 직접 에러 발생시키기 ===")

# raise ValueError("내가 직접 만든 ValueError")

# raise 아래에 작성한 코드는 절대 실행되지 않음
# 그래서 비활성화 된 것처럼 옅은 색으로 작성됨
# 해결 방법은 try-except문으로 감싸기

# num = int(input("0~10 사이의 숫자를 입력하세요 : "))

# if num < 11 and num > 0:
#     print(f"입력한 값은 {num}입니다.")
# else:
#     raise ValueError("0~10 사이의 숫자가 아님")
# 원한다면 TypeError 등 무관한 Error를 발생시킬 수 있음
# 근데 그러면 안됨 뒤지게 욕 먹는거야!

# 실습 1. 부품별로 csv 파일 만들기
# 부품 종류 : E2, F2, B2, A2, D2
# 결과 : 새로운 csv 파일 5개
# print("=== 실습 1 ===")
# import csv
# try:
#     base_file = open("data/09_ict_inspection.csv", "r", encoding="utf-8")
#     E2_file = open("data/E2.csv", "w", encoding="utf-8", newline="")
#     F2_file = open("data/F2.csv", "w", encoding="utf-8", newline="")
#     B2_file = open("data/B2.csv", "w", encoding="utf-8", newline="")
#     A2_file = open("data/A2.csv", "w", encoding="utf-8", newline="")
#     D2_file = open("data/D2.csv", "w", encoding="utf-8", newline="")
#     reader = csv.reader(base_file)
#     header = next(reader)
#     E2_writer = csv.writer(E2_file)
#     F2_writer = csv.writer(F2_file)
#     B2_writer = csv.writer(B2_file)
#     A2_writer = csv.writer(A2_file)
#     D2_writer = csv.writer(D2_file)
#     E2_writer.writerow(header)
#     F2_writer.writerow(header)
#     B2_writer.writerow(header)
#     A2_writer.writerow(header)
#     D2_writer.writerow(header)
#     for row in reader:
#         if row[1] == "E2":
#             E2_writer.writerow(row)
#         elif row[1] == "F2":
#             F2_writer.writerow(row)
#         elif row[1] == "B2":
#             B2_writer.writerow(row)
#         elif row[1] == "A2":
#             A2_writer.writerow(row)
#         elif row[1] == "D2":
#             D2_writer.writerow(row)
# finally:
#     base_file.close()
#     E2_file.close()
#     F2_file.close()
#     B2_file.close()
#     A2_file.close()
#     D2_file.close()

# 데이터에서 부품 종류 자동으로 추출
# import csv

# try:
#     with open("data/09_ict_inspection.csv", "r", encoding="utf-8") as f:
#         reader = csv.reader(f)
#         header = next(reader)
#         rows = list(reader)
# except FileNotFoundError:
#     print("파일이 존재하지 않습니다. 경로를 확인하세요.")

# parts = []  # 추출된 부품을 추가할 빈 리스트
# for row in rows:
#     part = row[1]  # 해당 행에 있는 부품명 저장
#     if part == "":
#         continue
#     if part not in parts:  # parts 리스트 안에 part(부품명)이 없는 경우 실행되는 코드
#         parts.append(part)  # 부품명만 parts 리스트에 추가

# print("자동 추출한 부품 종류: ", parts)

# # 부품 종류별로 csv 파일 생성
# for part in parts:  # parts 리스트의 부품명들만큼 csv 파일 생성
#     with open(
#         f"data/09_ict_inspection_{part}.csv", "w", encoding="utf-8", newline=""
#     ) as f:
#         writer = csv.writer(f)
#         writer.writerow(header)

#         for row in rows:  # 만들어질 csv 파일에 행을 추가하는 반복문
#             if row[1] == part:
#                 # 전체 데이터셋에서 현재 for문으로 돌고있는
#                 # 부품명이 같은 경우에만 현재 만들 csv 파일에
#                 # 행으로 추가하는 작업
#                 writer.writerow(row)  # 해당 행을 csv 파일에 추가
#     print(f"data/09_ict_inspection_{part}.csv 생성 완료")
# print("모든 파일 생성 완료")

# ==============================================================================
# 실습 2.
# 조건
# 각 행에서 정상범위 내에 있는 데이터셋 생성
# 측정값이 0이면 제외
# 층거밧이 하한치보다 작으면 제외
# 측정값이 상한치보다 높으면 제외
# 측정값이 빈 값이면 제외
# import csv

# try:
#     base_file = open("data/09_ict_inspection.csv", "r", encoding="utf-8")
#     test_file = open(
#         "data/09_ict_inspection_test2.csv", "w", encoding="utf-8", newline=""
#     )
#     reader = csv.reader(base_file)
#     header = next(reader)
#     writer = csv.writer(test_file)
#     writer.writerow(header)
#     for row in reader:
#         if row[2] == "" or float(row[2]) == 0:
#             continue
#         if float(row[2]) < float(row[5]):
#             continue
#         if float(row[2]) > float(row[4]):
#             continue
#         writer.writerow(row)
# finally:
#     base_file.close()
#     test_file.close()


# ======================================================================
# 실습 3.
# 측정값, 상한값, 하한값을 인자로 전달받아
# 0이 아니면서 정상범위인지 확인하는 함수 만들기
# 인자로 전달하는 값의 자료형은 flaot이라고 가정
# 반환값은 조건에 만족한다면 True, 아니라면 False
# is_nomal
def is_normal(measurement, upper_limit, lower_limit):
    if measurement == 0:
        return False
    if measurement < lower_limit:
        return False
    if measurement > upper_limit:
        return False
    return True


# 기존 코드 함수 활용하도록 수정하기
import csv

try:
    base_file = open("data/09_ict_inspection.csv", "r", encoding="utf-8")
    test_file = open(
        "data/09_ict_inspection_test2.csv", "w", encoding="utf-8", newline=""
    )
    reader = csv.reader(base_file)
    header = next(reader)
    writer = csv.writer(test_file)
    writer.writerow(header)
    for row in reader:
        if row[2] == "":
            continue
        measurement = float(row[2])
        upper_limit = float(row[4])
        lower_limit = float(row[5])
        if is_normal(measurement, upper_limit, lower_limit):
            writer.writerow(row)
finally:
    base_file.close()
    test_file.close()


# raise 활용해서 검증 함수 만들기
def check_value(measurement, upper_limit, lower_limit):
    val = float(measurement)
    if val == 0 or not (lower_limit <= measurement <= upper_limit):
        raise ValueError(f"부적절한 값 {val}")
    return val


# 빈값, 문자열, 측정값이 0, 정상범위가 아니면 ValueError 발생
# 문제가 있을 때 무조건 Error 발생시킴

for row in rows:
    try:
        check_value(row[2], float(row[4]), float((row[5])))
    except (ValueError, IndexError):
        continue
