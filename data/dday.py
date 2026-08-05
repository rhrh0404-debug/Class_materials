from datetime import datetime


def calculate_dday(year, month, day):
    """
    특정 연도, 월, 일을 입력받아 오늘까지의 디데이(사귄 날을 1일로 계산)를 반환합니다.
    """
    start_date = datetime(year, month, day)
    today = datetime.now()
    delta = today - start_date
    dday = delta.days + 1

    return dday


year = 2025
month = 12
day = 20
days = calculate_dday(year, month, day)
if days > 0:
    print(f"재히랑 사귄 지 💖{days}일째💖 입니다!")
