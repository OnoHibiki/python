class Employee:
    def __init__(self, name:str , age:int , dept: str):
        self.name = name
        self.age = age
        self.dept = dept

    
    def age_group(self) -> str:
        if 20 <= self.age <= 29:
            return "20代"
        elif 30 <= self.age <= 39:
            return "30代"
        else:
            return "その他"
        
    def describe(self) -> str:
        return f"{self.name}({self.dept}): {self.age}歳 / {self.age_group()}"
    

members = [
    Employee("Taro", 25 , "Sales"),
    Employee("Hanako", 32, "HR"),
    Employee("ken" , 41 , "IT"),
]

for m in members:
    print(m.describe())