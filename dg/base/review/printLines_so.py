def print_line(char, times):
    """打印单条分隔线
    char:分隔线符号
    times:分隔线符号重复次数"""
    print(char*times)

def print_lines(char, times):
    """打印多条分隔线
    char:分隔线的符号
    times:分隔线符号重复次数"""

    i = 0
    while i < 5:
        print_line(char, times)
        i += 1

name = "laowang"
