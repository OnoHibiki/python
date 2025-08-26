ages = [25 , 32 , 41 , 29 , 38 , 22 , 30]

# 平均を出す関数
def average(numbers):
    return sum(numbers) / len(numbers)

# 30歳以上を抽出する関数
def filter_over_30(numbers):
    return [age for age in numbers if age >= 30]

# 20代だけを抽出する関数
def filter_age_20(numbers):
    return [age for age in numbers if 20 <= age <= 29]


print("社員データ：", ages)
print("平均年齢", average(ages))
print("30歳以上:", filter_over_30(ages))

print("20代:", filter_age_20(ages))
