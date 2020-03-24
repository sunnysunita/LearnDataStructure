user_input = input("enter string")
list0 = list(user_input)


def checkAB(list0, si, l=len(list0)):
    if list0[0] == "a":
        if si > l - 1:
            return True
        else:
            if list0[si] == "a":
                return checkAB(list0, si + 1)
            elif list0[si] == "b" and si+1<l and list0[si + 1] == "b":

                if si+2<l and list0[si + 2] == "a":
                    return checkAB(list0, si + 2)
                elif si+2==l:
                    return True
                else:
                   return False
            else:
                return False


    else:
        return False


print(checkAB(list0, 0))
