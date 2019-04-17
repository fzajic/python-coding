while True:
  seznam = []
  limit = int(input("zadej limit "))+1
  for i in range(limit):
    seznam.append(int(i))
  primes = []

  seznam.remove(0)
  seznam.remove(1)

  while seznam:
    prime = seznam[0]
    x = prime
    primes.append(seznam[0])
    seznam.remove(seznam[0])
    while x < limit:
      x = x + prime
      if x in seznam:
        seznam.remove(x)
  print("toto jsou nase prvocisla:")
  print(primes)
  x=0
  for i in primes:
    x=x+1
  print("")
  print("pocet prvocisel:")
  print(x)
  print("")
