#/usr/bin/python3

import sys, paramiko,os
import subprocess


host=<host>
username=<username>
password=<password>
dirFolder=<directory>

def pull():
    datacommit =sys.argv[1]
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.WarningPolicy)
    ssh.connect(hostname=host, username=username, password=password)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("screen -dmS killnode killall node && cd + dirFolder + && git pull && screen -dmS node npm run dev")
    print(ssh_stdout.read())
    ssh.close()

def main():
    try:
        subprocess.check_call(["git add ."], shell=True)
        subprocess.check_call("git commit -m update", shell=True)
        subprocess.check_call("git push origin "+datacommit, shell=True)
        pull()
    except subprocess.CalledProcessError as e:
        raise RuntimeError("nothing change")

if __name__ == '__main__':
    main()
