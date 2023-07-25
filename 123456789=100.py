from time import time


def isCorrect(string):
    return eval(string) == 100


def tryOparation(oparation):
    temp = ""
    for i in range(len(numbers)):
        try:
            temp += numbers[i]
            if oparation[i] != " ":
                temp += oparation[i]
        except:
            pass
    resolt = eval(temp)
    if resolt == 100:
        print(f"{temp} = {resolt}")
        ans.append(temp)


numbers = "123456789"
oparators = ["+", "-", "*", "/", " "]
ans = []

time0 = time()

oparations = []
for opar1 in oparators:
    for opar2 in oparators:
        for opar3 in oparators:
            for opar4 in oparators:
                for opar5 in oparators:
                    for opar6 in oparators:
                        for opar7 in oparators:
                            for opar8 in oparators:
                                numOf_ = 0
                                for i in [opar1, opar2, opar3, opar4, opar5, opar6, opar7, opar8]:
                                    if i == " ":
                                        numOf_ += 1
                                if numOf_ == 5:
                                    oparations.append(
                                        opar1 + opar2 + opar3 + opar4 
                                        + opar5 + opar6 + opar7 + opar8
                                    )
for i in oparations:
    tryOparation(i)
time1 = time()

print(
    f"\nnumber of ans working: {len(ans)}\nnumber of difrent operation: {len(oparations)}\nprobability of random ans working: {len(ans)*100/len(oparations)}%\n\nit took: {time1 - time0} seconds\n\n"
)
