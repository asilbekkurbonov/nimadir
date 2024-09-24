def split_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

lst = ["A", "B", "C", "D", "E", "F", "G", "L", "Q", "U"]

n = int(input("Ro'yxatni nechta elementdan iborat bo'laklarga bo'lamiz? "))

print(split_list(lst, n))