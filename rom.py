import logging

log = logging.getLogger('nespy.rom')


class ROM:
    def __init__(self, rom):
        self.path = rom
        with open(rom, 'rb') as file_read:
            self.data = file_read.read()
            log.debug('Rom loaded from {}'.format(rom))

        # header info from http://wiki.nesdev.com/w/index.php/INES
        self.header = self.data[0:16]
        self.pgr_size = self.header[4] * 16384
        self.chr_size = self.header[5] * 8192

        self.pgr_data = self.data[17:self.pgr_size]

        log.debug('PGR Size: {}'.format(self.pgr_size))
        log.debug('CHR Size: {}'.format(self.chr_size))

    def __str__(self):
        return "<Rom {}>".format(self.path)

    def get(self, position, size=1):
        return self.pgr_data[position:position+size]
