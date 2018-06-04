diem_xap__xep = []
new = input("Enter your sequence of number, separated by space: ")
diem = new.strip().split()

new = []
is_sorted = True

for item in diem:
    new.append(int(item))

for i in range(len(new) - 1):
    if new[i] > new[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("Your sequence is sorted")
    print(*new, sep= ", ")
else:
    print("Your sequence isn't sorted")
    print("Your sequence after sorted: ")
    for i in range(len(diem)):
        x = min(diem)
        diem.remove(x)
        diem_xap__xep.append(x)
    print(*diem_xap__xep, sep=", ")

