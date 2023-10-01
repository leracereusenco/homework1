temp = []
list_lenght = 7

temp1 = float(input('Care este temperatura luni?\n'))
temp.append(temp1)
temp2 = float(input('Care este temperatura marti?\n'))
temp.append(temp2)
temp3 = float(input('Care este temperatura miercuri?\n'))
temp.append(temp3)
temp4 = float(input('Care este temperatura joi?\n'))
temp.append(temp4)
temp5 = float(input('Care este temperatura vineri?\n'))
temp.append(temp5)
temp6 = float(input('Care este temperatura sambata?\n'))
temp.append(temp6)
temp7 = float(input('Care este temperatura duminica?\n'))
temp.append(temp7)

tempMed = float(temp1 + temp2 + temp3 + temp4 + temp5 + temp6 + temp7)/7

final_list = [temp1 - tempMed], [temp2 - tempMed], [temp3 - tempMed], [temp4 - tempMed], [temp5 - tempMed], [temp6 - tempMed], [temp7 - tempMed]


print(final_list)
print(sorted(final_list))