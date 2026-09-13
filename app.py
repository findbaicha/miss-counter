import time
print("写给嘟嘟的代码")
print("启动思念程序")
print("距离下次见面的期待，一直在增加")
print("只要程序不停，思念就不会中断")
with open('/../../../count.txt' , 'r') as f:
        a = int(f.read())
while True:
        a+=1
        print("此刻累计想你的次数：",a)
        time.sleep(1)
        with open("/../../../count.txt", "w") as f:
                f.write(str(a))