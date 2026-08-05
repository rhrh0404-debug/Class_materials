def space():
    print("=" * 50)
    print()


# - 사용 범위: `import`, 별칭 import, `from ... import ...`, 사용자 모듈, `os.getcwd()`, `os.path.join()`, `os.path.basename()`, `pathlib.Path`
# - 사용하지 않는 범위: 반복문, 예외 처리, 파일 읽기/쓰기, 클래스
# - 경로 구분 문자는 직접 `"/"`로 붙이지 말고 경로 조합 기능을 사용합니다.

# ## 문제 1. 표준 모듈 가져오기 (5분)

# `math` 모듈을 가져와 `sqrt()`로 진동값 `81`의 제곱근을 계산해 출력하세요.

# 예시 출력

# ```text
# 9.0
# ```

# 제약: `import math`를 사용하고 `math.sqrt(81)` 형태로 호출합니다.
import math

print(math.sqrt(81))
space()
# ## 문제 2. 별칭으로 점검 시간 만들기 (6분)

# `datetime` 모듈을 `dt`라는 별칭으로 가져오고, `dt.date(2026, 7, 31)`을 만들어 출력하세요.

# 예시 출력

# ```text
# 2026-07-31
# ```

# 제약: `import datetime as dt`를 사용합니다.
import datetime as dt

print(dt.date(2026, 7, 31))
space()
# ## 문제 3. 필요한 기능만 선택해서 가져오기 (7분)

# `os.path`에서 `basename`만 가져와 아래 경로에서 파일명만 출력하세요.

# ```python
# report_path = "data/inspection/compressor_A.csv"
# ```

# 예시 출력

# ```text
# compressor_A.csv
# ```

# 제약: `from os.path import basename`을 사용합니다.
from os.path import basename

report_path = "data/inspection/compressor_A.csv"
print(basename(report_path))
space()
# ## 문제 4. 점검 결과 경로 안전하게 조합하기 (8분)

# `os.path.join()`으로 기준 폴더, 날짜 폴더, 파일명을 조합하세요.

# ```python
# base_dir = "inspection_data"
# date_dir = "2026-07-31"
# file_name = "pump_01.csv"
# ```

# 예시 출력

# ```text
# inspection_data/2026-07-31/pump_01.csv
# ```

# 제약: 문자열 덧셈과 직접 `"/"` 입력을 사용하지 않습니다. 운영체제에 따라 구분 문자는 달라질 수 있습니다.
base_dir = "inspection_data"
date_dir = "2026-07-31"
file_name = "pump_01.csv"
import os

files = os.path.join(base_dir, date_dir, file_name)
print(files)
space()
# ## 문제 5. 사용자 모듈로 점검 상태 재사용하기 (9분)

# 아래와 같이 `inspection_tools.py` 파일이 있다고 가정합니다.

# ```python
# def status(value, limit=90):
#     if value > limit:
#         return "경고"
#     return "정상"
# ```

# `inspection_tools` 모듈을 가져와 압축기 온도 `95`의 상태를 출력하세요.

# 예시 출력

# ```text
# 경고
# ```

# 제약: `import inspection_tools`를 사용하고 `inspection_tools.status(95)`로 호출합니다.
# import inspection_tools


# def status(value, limit=90):
#     if value > limit:
#         return "경고"
#     return "정상"


# inspection_tools.status(95)
# ## 문제 6. pathlib로 설비 보고서 위치 만들기 (10분)

# `Path`를 사용해 다음 보고서 경로를 만들고, 파일명과 전체 경로를 차례로 출력하세요.

# - 기준 폴더: `"reports"`
# - 날짜 폴더: `"2026-07-31"`
# - 파일명: `"motor_A.txt"`

# 예시 출력

# ```text
# motor_A.txt
# reports/2026-07-31/motor_A.txt
# ```

# 제약: `from pathlib import Path`를 사용하고 `/` 연산자로 Path 객체를 조합합니다.
from pathlib import Path

report_path = Path("reports") / "2026-07-31" / "motor_A.txt"
print(report_path.name)
print(report_path)
space()
# ## 제출 전 점검

# - 모듈 이름과 함수 이름 사이에 `.`을 정확히 썼는가?
# - 별칭을 썼다면 원래 모듈 이름 대신 별칭으로 호출했는가?
# - 필요한 이름만 가져왔을 때 모듈 이름을 붙이지 않았는가?
# - 경로를 직접 연결하지 않고 `join()` 또는 `Path`로 조합했는가?
# - 사용자 모듈 파일이 현재 파일과 같은 폴더 또는 import 가능한 경로에 있다고 가정했는가?
