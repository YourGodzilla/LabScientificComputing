# Condition
# if
# else
# else if => elif
# else

# && => and
# || => or
# ! => not

x = 70
# indentation
if x < 50 :
    print("lebih kecil dari 50")
    if x < 20 or x > 30:
    print("Lebih dari 20 atau lebih besar dari 30")
elif x > 50 :
    print("Lebih besar dari 50")
    if x > 60 and x < 80:
    print("Lebih besar dari 60 dan kurang dari 50")

if x != 50:
    print("Bukan 50")

udaMandi = False
if not udaMandi:
    print("ih bau")
else:
    print("udh wangi")


for i in range(10):
    print(i)

print(" ")

# start, end , step
for j in range(5, 10, 1):
    print(j)

print(" ")

# reverse
for k in range(10, 0, -2):
    print(k)