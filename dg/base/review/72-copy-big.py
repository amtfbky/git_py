f_r = open("README")
f_w = open("README[复件]", "w")

while True:
    t = f_r.readline()
    if not t:
        break
    f_w.write(t)

f_r.close()
f_w.close()
