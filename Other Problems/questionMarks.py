'''
"arrrb6???4xxbl5???eee5" -- True
"acc?7??sss?3rr1??????5" -- True
"5??aaaaaaaaaaaaaaaa?5?5" -- True
"9???1???9???1???9" -- True
"aa679" -- False
"8???2???9" -- False
"10???0???10" -- False
"aa3??oiuqwer?7???2" -- False
'''


def all_good(s):
    first_digit = ""
    second_digit = ""
    qm_count = 0
    if "?" not in s:
        return False
    for ltr in s:
        if ltr.isdigit():
            if first_digit == "":
                first_digit = ltr
            else:
                second_digit = ltr
                if qm_count == 3:
                    if int(first_digit) + int(second_digit) == 10:
                        # all good reset values and continue testing
                        first_digit = second_digit
                        second_digit = ""
                        qm_count = 0
                    else:
                        return False
                else:
                    first_digit = second_digit
                    second_digit = ""
                    qm_count = 0

        elif ltr == "?" and first_digit != "":
            qm_count += 1
            if qm_count > 3:
                #reset
                first_digit = ""
                second_digit = ""
                qm_count = 0



    return True

if __name__ == "__main__":
    print(all_good("arrrb6???4xxbl5???eee5") == True)
    print(all_good("aa3??oiuqwer?7???2") == False)
    print(all_good("acc?7??sss?3rr1??????5") == True)
    print(all_good("5??aaaaaaaaaaaaaaaa?5?5") == True)
    print(all_good("9???1???9???1???9") == True)
    print(all_good("aa679") == False)
    print(all_good("8???2???9") == False)
    print(all_good("10???0???10") == False)
    print(all_good("aa3??oiuqwer?7???2") == False)




