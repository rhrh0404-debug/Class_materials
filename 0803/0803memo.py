print("8월 3일 학습 시작!")
# 연습
# f = open("data/08_press.csv", "r", encoding="utf-8")  # f = 파일 객체(연결 통로)
# print(type(f).__name__)  # TextIOWrapper
# f.close()

# ============================================================================================
# 연습
import os
import csv

FILE = "data/08_press.csv"  # 불러오고자 하는 파일 경로 지정
# open 함수 사용해보기
f = open(FILE, "r", encoding="utf-8")  # f에는 파일 객체 (연결통로)가 할당됨

print(
    f
)  # <_io.TextIOWrapper name='data/08_press.csv' mode='r' encoding='utf-8'> 가 출력됨
# io.TextIOWrapper: : f라는 파일 객체의 타입
# name='data/08_press.csv' : 지금 연 파일의 경로
# mode='r' : 열기 모드(read 전용 모드)
# encoding='utf-8' : 파일의 글자를 해석할 때 쓰는 문자 인코딩 방식
# f라는 변수에는 파일 안의 내용물이 아닌
# 해당 파일과 연결된 통로 그 자체여서
# 내용 대신 연결 상태 정보가 보임

print("=" * 50)

# 파일 안에 내용을 가져오기
# print(f.read())  # 전체를 한 문자열로 가져옴
# 설비ID,시각,진동X,진동Y,전류,상태
# PRESS-01,2022-07-12 00:00:00.019,0.117,-0.1764,192.3387,0
# PRESS-02,2022-07-12 00:08:27.624,0.242,0.1,-51.347,0
# PRESS-03,2022-07-12 00:17:19.247,-0.0446,0.0103,109.3448,0
# PRESS-04,2022-07-12 00:27:42.343,-0.0462,-0.0126,-89.1011,0
# PRESS-05,2022-07-12 00:37:19.526,0.0612,0.2451,215.0735,0
# PRESS-06,2022-07-12 00:46:49.858,0.0433,0.2131,-208.6758,0
# PRESS-07,2022-07-12 00:57:07.847,0.0282,-0.022,-101.7107,0
# PRESS-08,2022-07-12 01:06:58.151,-0.0423,-0.0366,-7.2041,0
# PRESS-09,2022-07-12 01:16:55.828,0.0773,0.0883,108.258,0
# PRESS-10,2022-07-17 10:51:07.943,0.2937,-0.5406,21.4577,1
# PRESS-11,2022-07-17 10:52:40.072,0.1102,-0.1504,-85.8307,1
# PRESS-12,2022-07-17 10:53:53.540,-0.0489,-0.0071,195.5033,1

print("=" * 50)

print(type(f.read()))  # <class 'str'> # 문자열 확인

print("=" * 50)

# 한 줄 출력
# print(f.readline) # readline 내장함수에 ()가 없어서 error 발생
print(f.readline())  # 아무것도 출력하지 않음
# 이유는 : f라는 파일 객체에는 "현재 어디까지 읽었는지"를 알려주는
# "위치 포인터"가 있음
# "이미 위에서 read()라는 내장메서드로 끝까지 읽었다면"
# 현재 위치 포인터 위치는 가장 마짐작이고,
# readline으로 읽을 값은 더이상 없어서
# 빈 문자열을 출력함.

# 위치 포인터를 옮기는 방법
f.seek(0)  # 포인터를 파일 맨 앞으로 이동
print(f.readline())  # 설비ID,시각,진동X,진동Y,전류,상태

# .seek() 이라는 내장메서드는 파일을 처음부터 몇 바이트(글자)
# 건너뛴 지점으로 갈 지를 인자로 전달받음

f.seek(3)
print(f.readline())  # 비ID,시각,진동X,진동Y,전류,상태
# 첫 번째 줄의 바이트를 알기 번거로우니 두 번째 줄을 출력하고 싶은 경우는
# readlines()를 사용해서 리스트로 전달받고,
# 인덱스로 접근하는 것이 더 쉬움.

f.seek(0)
print(f.readlines())  # 전체 내용을 줄별로 리시트에 담아 출력
# ['설비ID,시각,진동X,진동Y,전류,상태\n',
# 'PRESS-01,2022-07-12 00:00:00.019,0.117,-0.1764,192.3387,0\n',
# 'PRESS-02,2022-07-12 00:08:27.624,0.242,0.1,-51.347,0\n',
# 'PRESS-03,2022-07-12 00:17:19.247,-0.0446,0.0103,109.3448,0\n',
# 'PRESS-04,2022-07-12 00:27:42.343,-0.0462,-0.0126,-89.1011,0\n',
# 'PRESS-05,2022-07-12 00:37:19.526,0.0612,0.2451,215.0735,0\n',
# 'PRESS-06,2022-07-12 00:46:49.858,0.0433,0.2131,-208.6758,0\n',
# 'PRESS-07,2022-07-12 00:57:07.847,0.0282,-0.022,-101.7107,0\n',
# 'PRESS-08,2022-07-12 01:06:58.151,-0.0423,-0.0366,-7.2041,0\n',
# 'PRESS-09,2022-07-12 01:16:55.828,0.0773,0.0883,108.258,0\n',
# 'PRESS-10,2022-07-17 10:51:07.943,0.2937,-0.5406,21.4577,1\n',
# 'PRESS-11,2022-07-17 10:52:40.072,0.1102,-0.1504,-85.8307,1\n',
# 'PRESS-12,2022-07-17 10:53:53.540,-0.0489,-0.0071,195.5033,1\n']

print("=" * 50)

# PRESS-0 행만 출력하고 싶은 경우 인덱스로 접근
f.seek(0)
print(f.readlines()[3])  # PRESS-03,2022-07-12 00:17:19.247,-0.0446,0.0103,109.3448,0

# 변수에 담아서 사용하기
f.seek(0)
lines = f.readlines()[3]
# 변수에 담아두면 해당 변수를 사용하면 되기 떄문에
# f,seek(0)으로 포인터를 옮길 필요가 거의 없음

print(len(lines))  # 59

# csv 파일의 전체 길이 : 출력
print(len(f.readlines()))  # 13

print("=" * 50)

# __name__ : 자료형에 이름을 문자열로 담고 있는 속성을 의미한다.
# f의 자료형은 "_io.TextIOWrapper"
print(type(f))  # <class '_io.TextIOWrapper'>
print(type(f).__name__)  # TextIOWrapper

print(type("aaa"))  # <class 'str'>
print(type("aaa").__name__)  # str
# __name__을 사용하면 <class>를 안보이게 할 수 있음!

print("=== 실습1 ===")
f = open("data/08_press.csv", "r", encoding="utf-8")
print(f.read())
f.close()
print("=" * 50)
f_1 = open("data/08_press.csv", "r", encoding="utf-8")
print(f_1.readlines())
f_1.close()
print("=" * 50)
f_text = open("data/text.txt", "r", encoding="utf-8")
print(f_text.readlines())
f_text.close()
print("=" * 50)
f_text = open("data/text.txt", "r", encoding="utf-8")
print(f_text.readline())
f_text.close()

# ====================연습====================
# with open 사용
# 블록이 끝나면 자동으로 닫힘(자동 close())

print("=== with open 사용 ===")

with open("data/08_press.csv", "r", encoding="utf-8") as f:
    # with eopn으로 연 파일의 내부 값을
    # 알아서 readlines()를 한 것처럼
    # 리스트로 만들어서 for문을 동작함
    for line in f:

        # 앞뒤 불필요한 공백 제거
        print(line.strip())

        # 독립적인 각자의 값을
        # 각기 문자열로 나누어 리스트로 저장
        print(line.split(","))
        # ['PRESS-12', '2022-07-17 10:53:53.540', '-0.0489', '-0.0071', '195.5033', '1\n']

# 설비명만 셋으로 만들어서 출력하기
print("=== 설비명만 셋으로 만들어서 출력하기 ===")

# 1. 빈 셋 만들기
# 2. with open 사용해서 파일 열기
# 3. 반복문으로 csv의 리스트 안 문자열 접근
# 4. "," 기준으로 나눠서 설비ID가 들어간 인덱스 찾기
# 5. 설비 ID 인덱스의 값을 빈 셋에 추가
# 설비ID 는 리스트에서 빼기
# 셋으로 만드는 이유는 중복을 자동 제거 해주기 때문
system_id = set()
with open("data/08_press.csv", "r", encoding="utf-8") as f:
    for line in f:
        system_id.add(line.split(",")[0])
print(sorted(system_id)[0:-1])

# ==========================================
# "w" 사용해 파일 재작성하기
# "w" 모드는 write의 약자로, 기존 저장된 값들을 모두 삭제하고
# 새로운 값을 작성
TXT = "data/text.txt"
with open(TXT, "r", encoding="utf-8") as f:
    print(f.read())
    # 김재욱 찢!!!!

# 모드 "w"로 새로 작성한다고 한 뒤 해당 파일의 전체 내용 출력
with open(TXT, "w", encoding="utf-8") as f:
    # 여기서 기존 파일에 있던 내용이 모두 삭제
    # print(f.read())
    # 그 뒤에 내용을 출력하라고 하니 읽을 수 없다는 Error 발생
    # io.UnsupportedOperation: not readable
    f.write(
        "새로 작성하는 내용 추가! \n이렇게 하면 줄바꿈도 가능하지롱 ㅋ \n아 자고 싶다"
    )
    # print(f.read())
    # 모드 "w"에서는 읽기 불가능
    # "w" 모드로 해놨기 때문에!
    # io.UnsupportedOperation: not readable
# 수정한 뒤에 수정된 값을 읽어오고 싶다면
# "r" 모드로 다시 코드 작성해야 함
print("=== w모드로 수정후 읽기 ===")
with open(TXT, "r", encoding="utf-8") as f:
    print(f.read())

# csv 파일 다시 작성해보기
FILE_UPDATE = "data/08_press_update.csv"
with open(FILE_UPDATE, "w", encoding="utf-8") as f:
    # 방법 1. 삼중따옴표 사용
    f.write("""date,is_study
260721,True
260722,True
260723,True
206724,True""")  # """"""을 사용할 경우 줄바꿈과 들여쓰기 주의

    # 방법 2. \n 사용
    f.write("\n260725,False\n260726,False\n260727,True\n206728,True")

    # 해당 코드블록 안에 여러번의 write()를 사용해 계속 추가하는 경유
    # 아래에 값이 계속 쌓임
with open(FILE_UPDATE, "r", encoding="utf-8") as f:
    print(f.read())

# "a" 모드
# 기존에 있던 값을 유지한 상태에서 아래에 계속 데이터 삽입

# 실습. "a" 모드로 08_press_update.csv 파일에 오늘 날짜까지 데이터 삽입
print("=== 실습. a 모드로 08_press_update.csv 파일에 오늘 날짜까지 데이터 삽입 ===")
FILE_ADD = "data/08_press_update.csv"
with open(FILE_ADD, "a", encoding="utf-8") as f:
    f.write("\n260729, True\n260730,True\n260731,True")
    f.write("""\n260801,False
260802,False
260803,True""")
with open(FILE_ADD, "r", encoding="utf-8") as f:
    print(f.read())

# print("=== 없는 파일을 작성한 경우 새로운 파일도 자동 생성됨! ===")
# 없는 파일을 작성한 경우
# 현재 data 폴더 안에는 08_press_update.csv
FILE_UPDATE = "data/08_press_update_new.csv"

with open(FILE_UPDATE, "w", encoding="utf-8") as f:
    f.write("이거 될까요?")
# 새로운 파일도 자동 생성됨

# ==============================
# csv.reader
# 한 행씩 리스트로 읽기
# csv.reader는 콤마로 나눈 결과를 자동으로 리스트로 변환해 준다
# 직접 split 하는 것보다 안전하고 편함

print("===csv.reader 연습해보기!")

import csv

FILE = "data/08_press.csv"  # 불러오고자 하는 파일 경로 지정

with open(FILE, "r", encoding="utf-8") as f:
    # csv 파일을 코드로 작업하기 편한 상태로 변환
    reader = csv.reader(f)
    # 이제부터는 코드 작업하기 편한 reader를 사용
    # 위 코드는 헤더까지 출력
    # 헤더를 자동 넘김하는 코드
    next(reader)  # 헤더를 건너뛰기

    for row in reader:
        print(row)
        # ['설비ID', '시각', '진동X', '진동Y', '전류', '상태']
        # ['PRESS-01', '2022-07-12 00:00:00.019', '0.117', '-0.1764', '192.3387', '0']
        # ...
        # 리스트로 반환해주기 때문에 바로 인덱스 사용 가능
        print(row[0])  # 설비 ID에 바로 접근

# 실습 4 설비명만 셋으로 만들어서 출력하기 (csv 사용 ver으로 개선하기)
print("=== 실습 4 설비명만 셋으로 만들어서 출력하기 (csv 사용 ver으로 개선하기) ===")
# 1. 빈 셋 만들기
# 2. with open 사용해서 파일 열기
# 3. 반복문으로 csv의 리스트 안 문자열 접근
# 4. 설비 ID 인덱스의 값을 빈 셋에 추가
# 5. 정렬하여 리스트로 출력
equipment = set()
import csv

FILE = "data/08_press.csv"
with open(FILE, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        equipment.add(row[0])
print(sorted(equipment))

# ====================================
# csv 사용해서 행 추가하기
print("=== csv 사용해서 행 추가하기 ===")
FILE_UPDATE = "data/08_press_update.csv"
import csv

# with open의 모드를 "w"로 하면 기존 데이터 모두 날아감
# with open의 모드를 "a"로 하면 기존 데이터 아래에 새로운 행 추가
with open(FILE_UPDATE, "a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(
        [
            "\n" "PRESS-12",
            "2022-07-17 10:53:53.540",
            "-0.0489",
            "-0.0071",
            "195.5033",
            "1",
        ]
    )  # 인자로 넘긴 리스트를 행으로 추가하는 동작
    # reader를 사용할 때 한 행을 문자열의 리스트로 받음
    # 그래서 writer를 쓸 때도 문자열의 리스트로 전달한다고
    # 생각하면 쉬움
    # 행을 추가할 때 열 갯수만큼 추가해야 문제 없이 동작함.
with open(FILE_UPDATE, "r", encoding="utf-8") as f:
    print(f.read())

# "=== 실습 5. csv.writer로 csv 쓰기 ==="
print("=== 실습 5. csv.writer로 csv 쓰기 ===")
NEW_STUDY_FILE = "data/2026_new_study.csv"
import csv

with open(NEW_STUDY_FILE, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["공부날짜", "순공시간", "메모"])
with open(NEW_STUDY_FILE, "a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["2026년08월01일", "00:00", "휴식"])
    writer.writerow(["2026년08월02일", "00:00", "휴식"])
    writer.writerow(["2026년08월03일", "02:17", "당일 학습 내용 복습"])
    writer.writerow(["2026년08월04알", "00:00", "미정"])
    writer.writerow(["2026년08월05일", "00:00", "미정"])
    writer.writerow(["2026년08월06일", "00:00", "미정"])
    writer.writerow(["2026년08월07일", "00:00", "미정"])
    writer.writerow(["2026년08월08일", "00:00", "미정"])
    writer.writerow(["2026년08월09일", "00:00", "미정"])
    writer.writerow(["2026년08월10일", "00:00", "미정"])

# csv.DictReader
# with open 으로 열고 reader 로 읽어 형변환 — writer 로 리스트를 행으로 저장

# 실습 6. csv읽어 조건 저장하기
print("=== 실습 6. csv읽어 조건 저장하기 ===")
import csv

FILE = "data/08_press.csv"
files = []
with open(FILE, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        if float(row[4]) > 90:
            files.append(row)
with open("data/files.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in files:
        writer.writerow(row)
with open("data/files.csv", "r", encoding="utf-8") as f:
    print(f.read())

print("인서야 오늘하루 존나 고생했다")
