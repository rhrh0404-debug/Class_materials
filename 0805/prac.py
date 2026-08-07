electric_rpm_1 = np.array([(row[3:5]) for row in body])
electric_rpm = electric_rpm_1.astype(float)
True_False_rpm = electric_rpm[:, 1] < 2000
print("2단계")
print(True_False_rpm)  # 회전수가 2000미만 판단 결과 출력

print("3단계")
True_False_electric_rpm = []
for row in electric_rpm:
    if row[1] < 2000 or row[0] > 25:
        True_False_electric_rpm.append(True)
    else:
        True_False_electric_rpm.append(False)
print(np.array(True_False_electric_rpm))

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
