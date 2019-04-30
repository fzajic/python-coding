N = int(input())
counter = 1
numbers_seen = []
a_sleep = False
if N == 0:
  print("INSOMNIA")
while not a_sleep:
  if N == 0:
    break

  if len(numbers_seen) >= 10:
    #a_sleep = True
    break

  number = counter * N
  for i in str(number):
    if i not in numbers_seen:
      numbers_seen.append(i)

  counter = counter + 1

print(number)
