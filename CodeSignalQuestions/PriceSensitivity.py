
def solution(prices, notes, x):
    global price_sensitivity
    price_sensitivity = False
    price_diff = 0

    for price, note in zip(prices, notes):
        # note = notes[i]
        insta_price = price
        if "lower" in note or "higher" in note:
            prcnt = float(note.split("%")[0])
            if "higher" in note:
                in_store_price = (price / (1 + prcnt * 0.01))
            else:
                in_store_price = (price / (1 - prcnt * 0.01))

            price_diff += (insta_price - in_store_price)

    price_sensitivity = price_diff <= x
    return price_sensitivity

def solution_optimal(prices, notes, x):
    *a, b = eval(dir()[0])
    for c, d in zip(*a):
        e = ('g' in d or -1) * float(d[:-22] or 0)
        b -= e * c / (e + 100)
    return b >= 0

# codesignal is dead, but you're alive
# join https://discord.gg/TxjF52A3qh


prices = [110, 95, 70]
notes = ["10.0% higher than in-store",
 "5.0% lower than in-store",
 "Same as in-store"]
x = 5

prices = [40, 40, 40, 40]
notes = ["0.001% higher than in-store",
 "0.0% lower than in-store",
 "0.0% higher than in-store",
 "0.0% lower than in-store"]
x = 0

prices = [220]
notes = ["120.0000% higher than in-store"]
x = 120

print(solution(prices, notes, x))
