import subprocess
import sys
import time
import shlex

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


def popen_test1():
    process = subprocess.Popen(['echo', 'working'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               universal_newlines=True)
    stdout, stderr = process.communicate()
    print(stdout, stderr)


def popen_test2():
    with open('popen_test2.txt', 'w') as f:
        process = subprocess.Popen(['date', '+%s'], stdout=f)


def popen_test3():
    process = subprocess.Popen(['ping', '-c 4', 'python.org'], stdout=subprocess.PIPE, universal_newlines=True)
    while True:
        output = process.stdout.readline()
        print(output.strip())
        ret_code = process.poll()
        if ret_code is not None:
            print("RETURN CODE:", ret_code)
            break


def popen_test4():
    ssh = subprocess.Popen(['ssh', 'mack14'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           universal_newlines=True, bufsize=0)
    ssh.stdin.write("uname -a\n")
    ssh.stdin.write("uptime\n")
    ssh.stdin.close()
    for line in ssh.stdout.readlines():
        print(line.strip())


def run_test1():
    process = subprocess.run(['echo', 'more work'], stdout=subprocess.PIPE, universal_newlines=True)
    print(process.returncode, process.stdout)


def read_write_test1():
    check_file_name = "status_check"
    now = str(int(time.time()))
    write_cmd = "echo {}".format(now)
    write_cmd = shlex.split(write_cmd)
    with open(check_file_name, "w") as f:
        proc = subprocess.run(write_cmd, stdout=f)
    if proc.returncode == 0:
        read_cmd = "cat {}".format(check_file_name)
        read_cmd = shlex.split(read_cmd)
        proc = subprocess.run(read_cmd, stdout=subprocess.PIPE, universal_newlines=True)
        if proc.returncode == 0 and proc.stdout.strip() == now:
            sys.exit(0)
    sys.exit(1)


def read_write_test2():
    now = str(int(time.time()))
    check_file_name = "status_check"
    client_host_name = "mack14"
    beegfs_mount_point = "tmp/"
    check_file_path = beegfs_mount_point + check_file_name
    ssh = subprocess.Popen(['ssh', client_host_name], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           universal_newlines=True, bufsize=0)
    ssh.stdin.write("echo {} > {}\n".format(now, check_file_path))
    ssh.stdin.write("cat {}\n".format(check_file_path))
    ssh.stdin.close()
    if ssh.stdout.readline().strip() == now:
        sys.exit(0)
    sys.exit(1)


if __name__ == '__main__':
    # check_output_test()
    # call_test1()
    # call_test2()
    # getstatusoutput_test()
    # popen_test1()
    # popen_test2()
    # popen_test3()
    # popen_test4()
    # run_test1()
    # read_write_test1()
    # read_write_test2()
    pass
