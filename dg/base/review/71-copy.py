f_r = open("README")
f_w = open("README[复件]", "w")

t = f_r.read()
f_w.write(t)

f_r.close()
f_w.close()
