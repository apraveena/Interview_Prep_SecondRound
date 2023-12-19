def convert_n_to_base_x(n, x):
    res = []
    while n >= x:
        rem = n % x
        res.append(str(rem))
        n = n // x
    res.append(str(n))
    res.reverse()
    return "".join(res)


print(convert_n_to_base_x(23, 2) == "10111")
print(convert_n_to_base_x(23, 5) == "43")
print(convert_n_to_base_x(23, 7) == "32")
print(convert_n_to_base_x(23, 10) == "23")
print(convert_n_to_base_x(23, 15) == "18")
