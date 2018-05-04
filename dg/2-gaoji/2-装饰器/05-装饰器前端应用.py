def makeBold(fn):
	def wrapped():
		return "<b>" + fn() + "</b>"

	return wrapped

def makeItalic(fn):
	def wrapped():
		return "<i>" + fn() + "</i>"

	return wrapped


@makeBold
def test1():
	return "----makebold----"
	
@makeItalic
def test2():
	return "----makeitalic----"


@makeBold
@makeItalic
def test3():
	return "----bold+italic----"


print(test1())
print(test2())
print(test3())
