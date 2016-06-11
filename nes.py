import logging

from cpu import CPU
from rom import ROM
from exceptions import NoRomLoaded


log = logging.getLogger('nespy.nes')


class NES:
    def __init__(self):
        self.cpu = CPU()
        self.input = None
        self.rom = None

    def load_rom(self, rom: ROM):
        log.debug('Loading rom into NES: {}'.format(rom))
        self.rom = rom

    def start(self):
        if self.rom is None:
            raise NoRomLoaded('Could not find a rom loaded into NES')
        log.debug('Starting NES!')
        self.cpu.power_up()
        self.cpu.start(self.rom)
