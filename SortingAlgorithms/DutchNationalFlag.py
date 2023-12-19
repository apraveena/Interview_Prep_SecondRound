def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def dutch_national_flag(a):
    red, green, blue = 0, 0, len(a)-1
    while green <= blue:
        if a[green] == "R":
            swap(a, green, red)
            green += 1
            red += 1
        elif a[green] == "G":
            green += 1
        else:
            swap(a, blue, green)
            blue -= 1
    return a

data = ["G", "B", "G", "G", "R", "B", "R", "G"]
data = ["G", "R", "G", "G", "R", "R", "R", "G"]
data = ["G", "G", "G", "G", "G", "G", "G", "G"]
data = ["G", "R", "R", "G", "G", "R", "G", "G"]
print(dutch_national_flag(data))