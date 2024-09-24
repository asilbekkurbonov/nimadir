inp = input("String kiriting: ")

natija = ""
is_plus = True

for belgi in inp:
    if belgi == "*":
        if is_plus:
            natija += " + "
        else:
            natija += " - "
        is_plus = not is_plus
    else:
        natija += belgi

print(natija)