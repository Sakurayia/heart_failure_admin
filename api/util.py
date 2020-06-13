import datetime


def minNums(startTime, endTime):
    seconds = (endTime - startTime).seconds
    # 来获取时间差中的秒数。注意，seconds获得的秒只是时间差中的小时、分钟和秒部分的和，并没有包含时间差的天数（既是两个时间点不是同一天，失效）
    total_seconds = (endTime - startTime).total_seconds()
    # 来获取准确的时间差，并将时间差转换为秒
    mins = total_seconds / 60 + (endTime - startTime).days * 24 * 60
    return int(mins)


def strToDatetime(str):
    return datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S") #+ datetime.timedelta(hours=8)

