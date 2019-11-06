import subprocess

CMD_DATE = "date"
CMD_LS = "ls"

CMDL_LS = ["ls", "-l"]


def check_output_test():
    res = subprocess.check_output(CMD_DATE)
    print(res.decode('utf-8'))


def call_test1():
    res = subprocess.call(CMD_DATE)
    print(res)


def call_test2():
    res = subprocess.call(CMDL_LS)
    print(res)


def getstatusoutput_test():
    res1 = subprocess.getstatusoutput(CMD_DATE)
    print(res1)
    res2 = subprocess.getstatusoutput(CMD_LS)
    print(res2)


if __name__ == '__main__':
    check_output_test()
    call_test1()
    call_test2()
    getstatusoutput_test()
    pass
