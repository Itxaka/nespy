from addresing import ImplicitAddressing

instructions = {}


def register(cls):
    instructions[cls.identifier_byte] = cls
    return cls


class Instruction:
    def execute(self):
        raise NotImplementedError()


@register
class Lda(ImplicitAddressing, Instruction):
    identifier_byte = bytes([0xA9])

    def execute(self):
        pass


@register
class Cld(ImplicitAddressing, Instruction):
    identifier_byte = bytes([0xD8])

    def execute(self):
        pass
