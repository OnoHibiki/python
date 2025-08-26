def safe_divide(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return "Error: 0では割れません"
    except ValueError:
        return "Error: 数値に変換できません"
    except Exception as e:
        return f"Unexpected: {type(e).__name__}: {e}"
    

tests = [("10", "2"),("5","0"),("abc" , "3"),(8,2)]
for x,y in tests:
    print(f"{x} / {y} = {safe_divide(x,y)}")