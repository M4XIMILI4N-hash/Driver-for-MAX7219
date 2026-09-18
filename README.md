# Driver-for-MAX7219

**Hardware setup:**
* ESP32
* 056LED4D7S display
* MAX7219
* 74AHCT125PW-Q100118 - Logic level shifter (LLS) (due to the fact that esp operates on 3.3V and Max operates on 5V)

**Pinout:**
`ESP32` =========== `LLS` ========================== `MAX7219`
* `P18 CLK` === `IN pin 2A` / `OUT pin 2Y` === `pin 13 CLK`
* `P5 CS` ===== `IN pin 3A` / `OUT pin 3Y` === `pin 12 LOAD(CS)`
* `P23 DIN` === `IN pin 1A` / `OUT pin 1Y` === `pin 1 DIN`

*All of the GND pins must be connected*

## Quick setup:

```python
import machine
from machine import SPI, Pin
from max_driver import Max_Driver

# 1. Initializing SPI (use your pins)
spi = SPI(1, baudrate=10000000, polarity=0, phase=0, bits=8, sck=Pin(18), mosi=Pin(23))

# 2. creating object
display = Max_Driver(spi, cs_pin_id=5, num_digits=4)

# 3. display data
display.send("H", 1) # Sends letter 'H' on 1 position
display.send(5, 2)   # Sends number '5' on 2 position
