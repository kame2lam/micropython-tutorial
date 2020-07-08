# 一款 Shell 型 MicroPython 文件資源管理器

特點:體積迷你，功能齊全的 MicroPython 管理工具，如：put\get\cat\rm\execfile 等等。

### 1.教學
* 連接webrepl的方法:
打開 mpfs.exe,按以下命令操作。

```
mpfs [/]> open ws:192.168.10.114,1234
```
192.168.10.114是esp8266 IP,
1234是webrepl密碼.

* 運行代碼文件
在 桌面 準備一個 Python 代碼文件（hello.py）

```python 
print('hello world!')
```
將 exe 與 .py 放在一起，按以下命令操作。
```
mpfs [/]> open
looking for all port...
Connected to esp8266
mpfs [/]> runfile hello.py
hello world!
```

### 2. 所有命令的用法

命令中的括弧為簡寫，方便使用。

| 命令類型     | 使用方法                                                     | 運行結果                                             | 註意事項                                                     |
| ------------ | ------------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------------------ |
| open (o)      | 打開當前設備。格式有：有線串口 `open com3`，無線有 `ws:192.168.10.114,1234` | 連接成功後返回 `Connected to esp32`                  | 控制板子前，需要先打開連接。括弧為簡寫。                     |
| close        | 關閉當前設備。                                               |                                                      |                                                              |
| quit (q)         | 輸入                                                             | 退出程式                                                   |                                                              |
| EOF          | 輸入                                                         | 退出程式                                             | 無                                                           |
| cat (c)          | 輸入 檔案名，例如 `cat boot.py`                              | 將板子的指定檔內容列印出來，以便快速查看。                   | 無                                                           |
| put          | 把目前的目錄下的檔推送到板子，例如`put boot.py`              | 無                                                   | 失敗會返回錯誤資訊                                           |
| get          | 獲取板子目前的目錄下的檔，例如`get boot.py`                  | 在程式運行的目錄（lpwd）下多了一個 boot.py 文件              |                                                              |
| mput         | 與 put 相對，以板子為主，對程式的目錄操作。                  |                                                      |                                                              |
| mget         | 與 get 相對，以板子為主，對程式的目錄操作。                  |                                                      |                                                              |
| repl (e)      | 進入 python 的 repl 控制介面                                 | 可以直接執行python代碼。                             |                                                              |
| exec (e)     | 輸入 Python 代碼，例如`exec print('hello')`                  | 返回print('hello')的運行結果 hello                   | 隻能執行一行 python 代碼。括弧為簡寫。                        |
| execfile (ef) | 執行板子中存在的python檔，例如`execfile main.py`           | 執行 main.py 的效果                                  | 括弧為簡寫。                                              |
| lexecfile (lef) | 執行程式下存在的python檔，例如`lexecfile main.py`           | 執行 main.py 的效果                                  | 括弧為簡寫，與 runfile 不同的是會進入repl模式，所以支援input操作。                                              |
| runfile (rf)  | 結合了 put 和 execfile 命令                                  |                                                      | 括弧為簡寫。                                                 |
| cd           | 輸入 指定板子裡的目錄，例如 `cd /` 或  `cd D:/Users`                           | 修改程式訪問板子的所處目錄                           | 以 `/` 分隔的linux路徑。 |
| md           | 輸入 目錄名稱                                                | 在板子上新建一個目錄                                 | 無                                                           |
| lcd          | 輸入 指定現在程式裡的目錄，例如 `cd /`                       | 修改程式訪問板子的所處目錄                           | 以 `/` 分隔的linux路徑。 |
| pwd          | 輸入`pwd`                                                    | 返回當前板子所處的目錄                               | 無                                                           |
| lpwd         | 輸入 `lpwd`                                                  | 返回當前程式所處的目錄                               | 無                                                           |
| mpyc         | 輸入 目前的目錄下的 python 檔，例如 `mpyc main.py`           | 把 python 代碼 pyc 化靜態編譯代碼處理，生成 main.pyc | 需要係統裡有 mpy-cross 命令                                                            |
| mrm          | 輸入指定的目錄或檔案名 `rm 目錄或檔案名`                                     | 移除係統裡的該目錄或檔案名                                           |                                                              |
| rm           | 輸入指定的目錄或檔案名 `rm 目錄或檔案名`                                     | 移除板子裡的該目錄或檔案名                                           |                                                              |
| ls           | 輸入` ls /`                                                  | 查看 板子 目前的目錄下的所有檔                       |                                                              |
| lls          | 輸入 `lls /`                                                 | 查看 程式 目前的目錄下的所有檔                       |                                                              |
| view          | 輸入 `view`                                                 | 查看 本機 可能的串口，和當前的 open 配置                       |                                                              |
| help         | 查看命令的幫助，例如：`help lls`                             |                                                      |

引用: https://github.com/junhuanchen/mpfshell-lite
