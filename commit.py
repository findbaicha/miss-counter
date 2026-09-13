import subprocess
import time
from pathlib import Path

REPO = Path.cwd()
FILE = REPO / "count.txt"
BRANCH = "main"
GIT_INTERVAL = 10
def git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO,
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE
    )

# 初始化文件
if not FILE.exists():
    with open(FILE, "w") as f:
        f.write("0")

print("写给嘟嘟的代码")
print("启动思念程序")
print("距离下次见面的期待，一直在增加")
print("只要程序不停，思念就不会中断")

with open(FILE, 'r') as f:
    count = int(f.read())

last_sync = time.time()

while True:
    count += 1
    print("此刻累计想你的次数：", count)
    with open(FILE, "w") as f:
        f.write(str(count))

    now = time.time()
    if now - last_sync >= GIT_INTERVAL:
        try:
            git("add", "count.txt")
            try:
                git("commit", "--amend", "--no-edit")
            except subprocess.CalledProcessError:
                git("commit", "-m", "update count")
            git("push", "--force", "origin", BRANCH)
            print("✅ synced to github", flush=True)
            last_sync = now
        except subprocess.CalledProcessError as e:
            err_msg = e.stderr.decode()[:250]
            print(f"❌ sync failed: {err_msg}", flush=True)

    time.sleep(1)