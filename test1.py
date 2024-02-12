def add(*numbers):
  total = 0
  for n in numbers:
    total += n

  return total

add1 = add(1,2,3,4,5,6,7,8)
print(add1)