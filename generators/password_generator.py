# generate a password with length "passlen" with no duplicate characters in the password

import random
fout = open("hesla.txt", "w")
for i in range(20):
  s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
  passlen = 3
  p =  "".join(random.sample(s,passlen ))
  fout.write(str(p) + "\n")
fout.close()