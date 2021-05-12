import machine, time, math

class servo:
    """
    A simple class for controlling hobby servos.

    Args:
        pin (machine.Pin): The pin where servo is connected. Must support PWM.
        freq (int): The frequency of the signal, in hertz.
        min_us (int): The minimum signal length supported by the servo.
        max_us (int): The maximum signal length supported by the servo.
        angle (int): The angle between the minimum and maximum positions.

    """
    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.pwm = machine.PWM(machine.Pin(pin), freq=freq, duty=0)

    def write_us(self, us):
        """Set the signal to be ``us`` microseconds long. Zero disables it."""
        if us == 0:
            self.pwm.duty(0)
            return
        us = min(self.max_us, max(self.min_us, us))
        duty = us * 1024 * self.freq // 1000000
        self.pwm.duty(duty)

    def write_angle(self, degrees=None, radians=None):
        """Move to the specified angle in ``degrees`` or ``radians``."""
        if degrees is None:
            degrees = math.degrees(radians)
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)

class buzzer:
    def __init__(self, num):
        self._B={'C':262,'CSharp':277,'D':294,'Eb':311,'E':330,'F':349,'FSharp':370,'G':392,
'GSharp':415,'A':440,'Bb':466,'B':494,'C3':131,'CSharp3':139,'D3':147,'Eb3':156,'E3':165,'F3':175,
'FSharp3':185,'G3':196,'GSharp3':208,'A3':220,'Bb3':233,'B3':247,'C4':262,'CSharp4':277,
'D4':294,'Eb4':311,'E4':330,'F4':349,'GSharp3':208,'A3':220,'Bb3':233,'B3':247,'C4':262,
'CSharp4':277,'D4':294,'Eb4':311,'E4':330,'F4':349,'FSharp4':370,'G4':392,'GSharp4':415,
'A4':440,'Bb4':466,'B4':494,'C5':523,'CSharp5':555,'D5':587,'Eb5':622,'E5':659,
'F5':698,'FSharp5':740,'G5':784,'GSharp5':831,'A5':880,'Bb5':932,'B5':988}
        buzzer_pin = machine.Pin(num, machine.Pin.OUT)
        self.pwm=machine.PWM(buzzer_pin)
        
    def tone(self, buz=[262, 1000]):
        self.pwm.duty(512)
        self.pwm.freq(buz[0])
        time.sleep_ms(buz[1])
        self.pwm.duty(0)
    
    def play(self, strA, timeB):
        notes=str(strA).split(' ')
        timeB=timeB
        for note in notes:
            if note=='-':
                self.pwm.duty(0)
                time.sleep_ms(timeB)
            else:
                self.tone([self._B[note],timeB])
    
    
class OTTO:
    def __init__(self,servoPin=[13,15,2,0]):
        self.S=[servo(servoPin[0]),servo(servoPin[1]),servo(servoPin[2]),servo(servoPin[3])]

    def servoAll(self,angle=[90,90,90,90]):
        self.S[0].write_angle(angle[0])
        self.S[1].write_angle(angle[1])
        self.S[2].write_angle(angle[2])
        self.S[3].write_angle(angle[3])