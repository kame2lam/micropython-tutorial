## OTTO

| ESP32 | 設備     | 
|---    |---       |
| 4     | 蜂鳴器(+)|
|GND    | 蜂鳴器(-)|
|13|舵機右下 |
|15|舵機右上 |
|2 |舵機左下 |
|0 |舵機左上 |
|16|超聲波傳感器(Echo) |
|17|超聲波傳感器(Trig) |

``` python 
from otto import buzzer
bu=buzzer(4)
bu.tone()
bu.play('C D E D E -',1000)
```

舵機
``` python 
from otto import servo
ser=servo(13)
ser.write_angle(90)
```