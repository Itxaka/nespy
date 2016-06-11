import logging
from instructions import instructions

log = logging.getLogger('nespy.cpu')


class CPU:
    def __init__(self):
        self.a_reg = None  # accumulator
        self.x_reg = None  # index
        self.y_reg = None  # index

        self.pc_reg = None  # pc: program counter, 65536 locations
        self.stack_reg = None  # s: stack pointer
        self.status_reg = None  # p: status

        self.ram = None

    def __str__(self):
        return "<Cpu 6502>"

    def power_up(self):
        """
        set internal registers to default values
        P = $34 (IRQ disabled)
        A, X, Y = 0
        S = $FD
        $4017 = $00 (frame irq enabled)
        $4015 = $00 (all channels disabled)
        $4000-$400F = $00 (not sure about $4010-$4013)
        Internal memory ($0000-$07FF) has unreliable startup state. Some machines may have consistent RAM contents at power-on, but others do not.
        """
        self.status_reg = bytes.fromhex('34')
        self.a_reg = self.x_reg = self.y_reg = bytes.fromhex('00')
        self.status_reg = bytes.fromhex('FD')
        self.pc_reg = 0

    def proccess(self, instruction):
        """
        receives an instruction and executes it
        """
        log.debug('Instruction received: {}'.format(instruction))
        print(type(instruction))
        print(bytes.fromhex(instruction))

    def start(self, rom):
        on = True
        while on:
            identifier = rom.get(self.pc_reg)
            instruction = instructions.get(identifier)
            if instruction is None:
                raise Exception("No instruction for identifier {}".format(identifier))
            log.debug('Got instruction type: {}'.format(instruction))
            data = rom.get(self.pc_reg + 1, instruction.data_length)
            instruction.execute(data)
            self.pc_reg += instruction.get_instruction_length()
        log.debug("Finished executing.")