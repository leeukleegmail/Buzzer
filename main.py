from machine import PWM, Pin
from time import sleep


tempo = 5
tones = {
    'c': 262,
    'd': 294,
    'e': 330,
    'f': 349,
    'g': 392,
    'a': 440,
    'b': 494,
    'C': 523,
    ' ': 0,
}
beeper = PWM(Pin(14, Pin.OUT), freq=440, duty=512)
melody = 'cdefgabC'
rhythm = [8, 8, 8, 8, 8, 8, 8, 8]


for tone, length in zip(melody, rhythm):
    beeper.freq(tones[tone])
    sleep(tempo/length)
beeper.deinit()
