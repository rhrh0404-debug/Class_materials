# 메모
# import math

# result = math.sqrt(16)
# print(result)

# 메모
# from math import sqrt

# result = sqrt(16)
# print(result)

# 메모
# import datetime as dt

# now = dt.datetime.now()
# print(type(now))

# ==================================================================================

# 실습1 import 세 방식으로 모듈 가져오기
# import math

# result = math.sqrt(16)
# result_1 = math.ceil(4.2)
# print(result, result_1)

# from math import sqrt, ceil

# result_2 = sqrt(16)
# result_3 = ceil(4.2)
# print(result_2, result_3)

# import math as m

# print(m.sqrt(16), m.ceil(4.2))

# ==================================================================================
# 연습
# import math

# print(math.sqrt(9))
# print(math.ceil(4.2))
# print(2**3)

# import random

# print(random.randint(1, 10))
# print(random.choice(["정상", "경고", "위험"]))

# import datetime

# now = datetime.datetime.now()
# print(now)

# ===================================================================================
# 실습2
# import math, random

# value = random.randint(1, 100)
# print(value)
# print(math.sqrt(value))

# ===================================================================================
# import os

# cwd = os.getcwd()
# print(cwd)

# import os

# files = os.listdir("c:")
# for name in files:
#     print(name)

# ===================================================================================
# import os

# path = os.path.exists("data")
# print(path)
# ====================================================================================
# import os

# path = os.path.join("data", "08_press.csv")
# if os.path.exists(path):
#     print("파일 있음:", path)
# =====================================================================================
# 실습3
# import os

# print("=" * 20)
# print(os.getcwd())
# files = os.listdir("data")
# for i in files:
#     print(i)
# for a in files:
#     if a.endswith(".csv"):
#         print(a)

# 실습4
# import os

# path = os.path.join("data", "08_press.csv")
# print(os.path.exists(path))
# if os.path.exists(path):
#     print("파일있음")
# else:
#     print("파일없음")

# 실습5
# import os
# from datetime import datetime

# files = os.listdir()
# now = datetime.now()
# print(len(files))
# print(f"파일 {len(files)}개, 점검 시작 {now}")

# 파일6
# import os

# files = os.listdir("data")
# cvs = []
# for i in files:
#     if i.endswith(".csv"):
#         cvs.append(i)
# print(cvs, end="")
# for j in cvs:
#     path = os.path.join("data", j)
#     print(f" 목록 {path}")

# 메모
# f = open("data/08_press.csv", "r", encoding="utf-8")
# print(type(f).__name__)
# f.close()
# with open("data/08_press.csv", "r", encoding="utf-8") as f:
#     lines = f.readlines()
# print(type(lines).__name__, len(lines))

# 실습1 우리가 풀지않고 답지보고 연습만함
# f = open("data/08_press.csv", "r", encoding="utf-8")
# text = f.read()
# print(text)
# f.close()
# f = open("data/08_press.csv", "r", encoding="utf-8")
# lines = f.readlines()
# print(lines)
# f.close()
