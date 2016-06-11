import logging
import argparse
from nes import NES
from rom import ROM

log = logging.getLogger('nespy')

logger = logging.StreamHandler()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.setFormatter(formatter)

log.addHandler(logger)
log.setLevel(logging.DEBUG)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('rom_file')
    args = parser.parse_args()
    rom = ROM(args.rom_file)
    nes = NES()
    nes.load_rom(rom)
    nes.start()

if __name__ == "__main__":
    main()
