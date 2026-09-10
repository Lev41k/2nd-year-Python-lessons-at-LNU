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
a = 123
sothi = a//100
desytky = (a//10)%10
odyn = a%10

print(100*desytky + 10*sothi + odyn)