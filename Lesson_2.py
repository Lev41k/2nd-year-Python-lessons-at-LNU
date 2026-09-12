# 1
# a = 456
# b = a%10
# a = a//10 + 100*b
# print(a)


# 2
# n = int(input("Enter n: "))
# print("Amount of full minutes in n seconds is", n//60)


# 3
# a = 356
# odyn = a%10
# desyatky = (a//10)%10
# sotni = a//100
# print(sotni*100 + odyn*10 + desyatky)


# 4
# h = 2
# m = 30
# t = 165

# hours_left = t//60
# minutes_left = t%60
# h += hours_left
# m += minutes_left
# if m >= 60:
#     h += 1
#     m -= 60
# print(h, ":",m)


# 5
# n = 46824
# print("Amount of full hours in n seconds is", n//3600)


# 6
# a = 123
# sothi = a//100
# desytky = (a//10)%10
# odyn = a%10

# print(100*desytky + 10*sothi + odyn)


# 7
# x = 3
# y = 4
# print(((max(x,y))**2) - ((2**x)*(min(x,y))))


# 8
# a = 1457984
# print((a%1000)//100)


# 9
# n = 5478
# print(n - (n//60)*60)


# 10
# a = 145984
# print((a%10000)//1000)


# 11
# x = 3
# y = 5
# z = min(x,y)
# x = max(x,y)
# y = z
# print("x =", x, "y =", y)


# 12
# a = 456
# a = (a - 100*(a//100))*10 + a//100
# print(a)


# 13
# n = 7350
# print(n - (n//3600)*3600)


# 14
# n = 1235
# sum = 0
# for i in range (4):
#     sum += n%10
#     n = n//10    
# print(sum)


# 15
# a = 123
# odyn = a%10
# sot = a//100
# des = (a-100*sot - odyn)//10
# print(100*odyn + 10*des + sot)


# 16
# n = 8
# print(n%7 + 1)


# 17
# n = 135
# sum = 0
# dob = 1
# for i in range (3):
#     dob = dob*(n%10)
#     sum += n%10
#     n = n//10    
# print("SUM:", sum, "DOB:", dob)


# 18
# a = 1289
# first = a//100
# last = a%100
# print(last*100 + first)


# 19
# y = 180 # 1 gradus = 2 hvylyny
# h = y * 2
# print(h//60, ":", h%60)


# 20
# a = 1256
# first = a//100
# second = a%100
# first_1 = first//10
# first_2 = first%10
# second_1 = second//10
# second_2 = second%10
# print(1000*first_2 + 100*first_1 + 10*second_2 + second_1)


# 21
# a = 3
# b = 4
# c = 7
# print (((a+b+c)/3)%1)


# 22
# a = 7
# a = a%(1.5)
# print(a**3 - 2.25*a)


# 23
# a = 3
# b = 4
# c = (a**2 + b**2)**(1/2)
# print("Perymetr:", a+b+c, "Plosha:", a*b/2)