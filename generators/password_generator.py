# generate a password with length "passlen" with no duplicate characters in the password
<<<<<<< HEAD

=======
>>>>>>> aef0e5d23c1d0274d86ceaa9c1c0a06007377a10
import random, os
os.chdir("generators")
fout = open("hesla.txt", "w")
for i in range(20):
  s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
  passlen = 20
  p =  "".join(random.sample(s,passlen ))
  fout.write(str(p) + "\n")
fout.close()
