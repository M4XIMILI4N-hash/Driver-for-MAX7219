import machine
from machine import SPI, Pin

class Max_Driver:
    """MAX7219 driver, using SPI"""
    
    def __init__(self, spi_bus, cs_pin_id, num_digits):
        
        self.spi = spi_bus
        
        self.cs =  Pin(cs_pin_id, Pin.OUT, value=1)
        
        self.num_digits = num_digits
        
        self.dictionary = {"-": 0x0A,"blank": 0x0F, "E": 0x0B, "H": 0x0C, "L": 0x0D, "P": 0x0E}
        
        self.init_display()
        
    def init_display(self):
        
        #Normal mode
        self.cs.value(0)
        self.spi.write(bytearray([0x0C, 0x01]))
        self.cs.value(1)
        
        #Activation of decode mode b
        self.cs.value(0)
        self.spi.write(bytearray([0x09, 0xFF]))
        self.cs.value(1)
        
        
        #scan limit, how many digits do we have
        self.cs.value(0)
        self.spi.write(bytearray([0x0B, self.num_digits-1]))
        self.cs.value(1)
        
        #Screen cleaning
        for i in range(1,self.num_digits+1):
            self.cs.value(0)
            self.spi.write(bytearray([i, 0x0F]))
            self.cs.value(1)
        
        
    
    def send(self, num, dig):
        self.cs.value(0)
        if isinstance(num, int):
            self.spi.write(bytearray([dig, num]))
        else:
            self.spi.write(bytearray([dig, self.dictionary.get(num, 0x0F)]))
        self.cs.value(1)
        
        
        
       






