def test(name, title="", gender=True):
    gender_txt = "男生"

    if not gender:
        gender_txt = "女生"

    print("[%s]%s 是 %s" % (title, name, gender_txt))


test("小明","班长")
test("小美", gender=False)
