# Программ проверят истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

countTrue = 0
countFalse = 0
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not(x or y or z) == (not x and not y and not z)):
                countTrue += 1
            else:
                countFalse += 1
if countFalse == 0:
    print ("Утверждение истенно для всех значений")
else:
    print ("Утверждение истенно не для всех значений")

