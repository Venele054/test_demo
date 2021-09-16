import os
import subprocess
import platform
win = platform.system() == "Windows"
encoding=("gbk" if win else "utf8")
file_path = r'/var/docker/checking.log'
MIDER = os.environ.get('MIDER')  # iotlab.midea.com.cn
TaskUuid = os.environ.get('task_uuid')
APPID = os.environ.get('app_id')
APPSECRET = os.environ.get('app_secret')

print('MIDER',MIDER)
print('TaskUuid',TaskUuid)
print('APPID',APPID)
print('APPSECRET',APPSECRET)
all = [f"nslookup {MIDER} 120.77.42.90",f"nslookup {MIDER} 47.97.62.62"]
def run_shell(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    re = p.stdout.readlines()

    with open(file_path, "a") as f:
        f.write(MIDER)
        f.write(TaskUuid)
        f.write(APPID)
        f.write(APPSECRET)
        for i in re:
            output = i.decode(encoding=encoding)
            print(output)
            f.write(output)


with open(file_path, "w") as f:
    f.truncate()
for i in all:
    run_shell(i)

