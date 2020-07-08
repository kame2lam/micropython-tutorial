from machine import Pin,PWM
import time

def alarmBeep(pwm):
   pwm.freq(1000)     #設定頻率為 1KHz    
   pwm.duty(512)      #設定工作週期為 50%
   time.sleep(1)          #持續時間 1 秒
   pwm.deinit()          #停止發聲
   time.sleep(2)          #持續時間 2 秒

pwm=PWM(Pin(4))

while True:
    alarmBeep(pwm)