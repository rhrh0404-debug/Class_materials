# sensor = ("모터온도", 78, "c")
# print(sensor[0])
# print(sensor[-1])
# sensor = ("모터온도", 78, "apple")
# name, value, word = sensor
# print(name)
# print(value)
# print(word)
# sensor = ("모터온도", 78, (3, 5))
# print(sensor[2][0])

# sensor = (("모터온도", 78), ("진동", 0.5))
# for i, s in enumerate(sensor, 1):
#     print(i, s[0])

# sensor = ((78, "모터온도"), (95, "베어링진동"), (32, "펌프압력"))
# hot = sorted(sensor, reverse=)

# name = ("모터온도", 78)
# print(name[0])
# print(name[1])
# s1, s2 = name
# print(s1, s2)

# names = [("펌프A", 75), ("회전속도", 100), ("펌프압력", 90), ("유량", 110)]
# for a, b in names:
#     print(a, b)
# limit = 90
# for a, b in names:
#     if b > limit:
#         print(a, "경고")

# names = [
#     ("펌프A", 75, (3, 5)),
#     ("회전속도", 100, (5, 7)),
#     ("펌프압력", 90, (7, 9)),
# ]
# for a, b, c in names:
#     x, y = c
#     print(a, "위치:", x, y)
# for a, b, c in names:
#     x, y = c
#     if x <= 5:
#         print(a, "1구역")

# ids = {"301", "302", "303", "301"}
# idss = sorted(set(ids))
# print(idss)

# alerts = {"S01", "S02"}
# alerts.add("S03")
# print(alerts)
# alerts.add("S01")
# print(alerts)

# line_a = {"S01", "S02", "S03"}
# line_b = {"S03", "S04"}
# all_s = line_a.union(line_b)
# print(all_s)

# line_a = {"S01", "S02", "S03"}
# line_b = {"S03", "S04"}
# print(line_a.difference(line_b))
# print(line_b.difference(line_a))

# room_num = [301, 302, 303, 301, 304, 303, 305, 302]
# room_num_list = set(room_num)
# print(f"방 번호 : {sorted(room_num_list)} / 방 개수 : {len(room_num_list)}개")

# a_room = {"301", "302", "303", "304", "305", "401", "402"}
# b_room = {"401", "402", "403", "404", "405", "301", "303"}
# print(
#     f"203동 방 번호 : {sorted(a_room.union(b_room))} 중복 방 번호: {a_room.intersection(b_room)} / a층만 방 번호 {a_room.difference(b_room)} / b층만 방 번호 : {b_room.difference(a_room)}"
# )

# yesterday = {"301", "302", "303", "306"}
# today = {"301", "303", "304"}
# print("신규", today.difference(yesterday))
# print("지속", today.intersection(yesterday))

# 연습문제1
# yesterday = [("S01", "정상"), ("S02", "경고"), ("S03", "경고")]
# today = [("S01", "정상"), ("S02", "경고"), ("S03", "정상"), ("S04", "경고")]
# warning = {"경고"}
# yesterday_1 = set(yesterday)
# today_1 = set(today)
# for a, b in yesterday_1:
#     if today_1.difference(yesterday_1):
#         b == warning
#         print("신규 경고:", a)
#     if today_1.intersection(yesterday_1):
#         b == warning
#         print("지속 경고:", a)

# 연습문제2
# list = [
#     ("A01", "연필"),
#     ("A02", "공책"),
#     ("A03", "연필"),
#     ("A04", "지우개"),
#     ("A05", "공책"),
# ]
# shop = {"연필", "공책", "지우개"}
# list_1 = set()
# shop_1 = set()
# for a, b in list:
#     if b in shop_1:
#         list_1.add(b)
#     shop_1.add(b)
# c = list_1 - shop_1
# print("전체 상품:", sorted(list_1.union(shop_1)))
# print("중복 상품:", sorted(list_1.intersection(shop_1)))
# print("미등록상품:", c)

# sensors = {"모터온도": 78}
# sensors["펌프압력"] = 95
# sensors["유량"] = 42
# print(sensors)

# sensors = {"모터온도": 78, "펌프압력": 95}
# sensors["모터온도"]: 80
# del sensors["펌프압력"]
# print(sensors)

# sensors = {"모터온도": 78}
# print(sensors.get("모터온도"))
# print(sensors.get("유량"))

# sensors = {"모터온도": 78, "펌프압력": 95}
# print("모터온도" in sensors)
# print(78 in sensors)
# if "유량" in sensors:
#     print(sensors.get("유량"))

# 딕셔너리 실습1
# sensors = {"모터온도": 78}
# print(sensors["모터온도"])
# sensors["유량"] = 90
# sensors["모터온도"] = 100
# print(sensors)
# print(sensors.get("유량", 0))
# print("유량" in sensors)

# sensors = {"모터온도": 78, "압력": 95}
# print(list(sensors.keys()))
# print(list(sensors.values()))
# avg = sum(sensors.values()) / len(sensors)
# print(avg)

# sensors = {"모터온도": 78, "진동": 0.5}
# for name, value in sensors.items():
#     print(name, "측정값:", value)

# sensors = {"모터온도": 78, "진동": 0.5, "압력": 95}
# print(len(sensors))
# if len(sensors) < 5:
#     print("센서 데이터 누락 확인 필요")

# values = {"모터온도": 95, "압력": 88}
# limits = {"모터온도": 90, "압력": 90}
# for name, value in values.items():
#     if value > limits[name]:
#         print(name, "경고")

# sensors = {"모터온도": 78, "진동": 0.5}
# new_data = {"모터온도": 80, "유량": 42}
# sensors.update(new_data)
# print(sensors)

# names = ["모터온도", "진동", "압력"]
# values = [78, 0.5, 95]
# sensors = dict(zip(names, values))
# print(sensors)

# sensors = {"모터온도": [78, 79, 80]}
# temps = sensors["모터온도"]
# print(sum(temps) / len(temps))
# print(max(temps))
# print(min(temps))

# plant = {
#     "1번모터": {"온도": 78, "상태": "정상"},
#     "2번펌프": {"압력": 95, "상태": "경고"},
# }

# 실습 2
# sensor = {"모터온도": 70, "진동": 30}
# new_date = {"모터온도": 77, "압력": 760}
# sensor.update(new_date)
# print(sensor)
# del sensor["진동"]
# print(f"센서수: {len(sensor)}개")

# 실습3
# sensor = {"모터온도": 73, "진동": 32}
# avg = sum(sensor.values()) / len(sensor)
# print(f"평균: {round(avg,1)}")
# top = ""
# hi = 0
# for name, v in sensor.items():
#     if v > hi:
#         hi = v
#         top = name
# print(f"최대값 센서: {top} {hi}")

# 실습4
# names = ["모터온도", "압력", "진동"]
# values = [94, 124, 35]
# sensors = dict(zip(names, values))
# print(sensors)
# for name, value in sensors.items():
#     print(f"{name} : {value} / ", end="")

# 실습5
# values = {"모터온도": 73, "진동": 69, "압력": 88}
# limits = {"모터온도": 70, "진동": 75, "압력": 80}
# warning = []
# for name, value in values.items():
#     if value > limits[name]:
#         warning.append(name)
# print(f"경고 센서 : {warning}")

# 실습6
# plant = {
#     "설비명 1": {"온도": 78, "상태": "정상"},
#     "설비명 2": {"온도": 95, "상태": "경고"},
# }
# print(plant["설비명 1"]["상태"])
# for name, info in plant.items():
#     if info["상태"] == "경고":
#         print(name, "점검필요")
