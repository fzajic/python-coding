def evaluate_attack(attack):
  charge = 1
  damage = 0
  for f in attack:
    if f == "C":
      charge = charge * 2
    else:
      damage = damage + charge
  return damage

def make_list(program):
  script = []
  for i in program:
    script.append(i)
  return script

def swap(attack):
  for i in range (len(attack)):
    if attack[-i] == "S" and attack[-i-1] == "C":
      attack[-i] = "C"
      attack[-i-1] = "S"
  return attack


D = int(input("enter max damage "))
program =  "CSCSS" # str(input("input aliens program like this (CSSCS) "))

attack = make_list(program)

if attack.count("S") <= D:
  counter = 0
  if evaluate_attack(attack) > D:
    while evaluate_attack(attack) > D:
      counter = counter + 1
      attack = swap(attack)
      print(attack)
  print(counter)

else:
  print("#case0 impossible")
