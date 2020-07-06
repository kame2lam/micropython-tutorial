# 準備工作

1. 打開 "uPyCraft_V1.1.exe"

2. 打開 Tools->Serial->COM3
![img](.\img\1.png)

3. 選擇 board: esp8266, Firemware Choose:Users
![img](\img\2.png)

4. 選擇 "firmware_esp8266-v1.3.5.bin"
![img](\img\3.png)

5. 按"OK"刷新
![img](\img\4.png)

6. 等待100% 更完成刷新
![img](\img\5.png)

7. 將 mpfs.exe 與 boot.py 放在一起，按以下命令操作。
```
mpfs [/]> open
looking for all port...
Connected to esp8266
mpfs [/]> put boot.py
mpfs [/]> repl
>
*** Exit REPL with Ctrl+Q ***

MicroPython v1.12 on 2020-02-23; ESP module with ESP8266
Type "help()" for more information.
>>>import webrepl_setup
```
出現是否要啟動 webrepl 功能的詢問選單, 選擇 Enable 的話還要設定連線密碼並重啟系統才會生效. 

8. 透過wifi 連接webrepl,
````
mpfs [/]> open ws:192.168.10.114
````


