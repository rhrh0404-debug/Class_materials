items = [
    ("A01", "연필"),
    ("A02", "공책"),
    ("A03", "연필"),
    ("A04", "지우개"),
    ("A05", "공책"),
]
shop = {"연필", "공책", "지우개"}

# 1. 전체 상품 (리스트에 등장한 모든 상품 종류, 중복 제거 및 정렬)
all_items = sorted(list({item[1] for item in items}))

# 2. 중복된 상품 (리스트에 2번 이상 등장한 상품)
# 등장 횟수 카운트
counts = {}
for _, name in items:
    counts[name] = counts.get(name, 0) + 1

# 2번 이상 등장한 상품만 추출
duplicate_items = sorted([name for name, count in counts.items() if count > 1])

# 3. 미등록 상품 (shop에는 있지만 items 리스트에는 없는 상품)
registered_items = {item[1] for item in items}
unregistered_items = sorted(list(shop - registered_items))

# 결과 출력
print(f"전체 상품 : {', '.join(all_items)}")
print(f"중복된 상품 : {' '.join(duplicate_items)}")
print(f"미등록 상품 : {', '.join(unregistered_items)}")
