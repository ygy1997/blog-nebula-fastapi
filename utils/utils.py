#删除逗号
def delLastChar(str):
    str_list=list(str)
    str_list.pop()
    return "".join(str_list)
