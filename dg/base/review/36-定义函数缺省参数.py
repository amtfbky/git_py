def test(name, gender):
    gender_txt = "男生"

    if not gender:
        gender_txt = "女生"

    print("%s 是 %s" % (name, gender_txt))


test("小明", gender=True)
test("小美", gender=False)
