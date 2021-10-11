a=-1
# l=list()
# while a != 0:
#   a=int(input('Введите число :'))
#   l.append(a)

# positive=0
# negative=0
# for i in range(len(l)):
#   if l[i]>0:
#     positive = positive+1
#   elif l[i]<0:
#     negative= negative +1

# print("positive numbers: ",positive)
# print("negative numbers: ",negative)

pos=list()
neg=list()
for i in range(0,1000):
  a=int(input('Введите число :'))
  if a>0:
    pos.append(a)
  elif a<0:
    neg.append(a)
  else:
    break
print("positive numbers: ",len(pos))
print("negative numbers: ",len(neg))