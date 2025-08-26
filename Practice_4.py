employees = [
    {"name": "Taro",   "age": 25, "dept": "Sales"},
    {"name": "Hanako", "age": 32, "dept": "HR"},
    {"name": "Ken",    "age": 41, "dept": "IT"},
    {"name": "Mika",   "age": 29, "dept": "Sales"},
]

over_30 = [e for e in employees if e["age"] >= 30]

all = [f'{e["name"]}({e["dept"]} / {e["age"]}歳)' for e in employees]

labels = [f'{e["name"]}({e["dept"]} / {e["age"]}歳)' for e in over_30]

dept_counts = {}
for e in employees:
    dept = e["dept"]
    dept_counts[dept] = dept_counts.get(dept,0) + 1

print("30歳以上:", labels)
print("部署ごとの人数:", dept_counts)
print("全員:", all)