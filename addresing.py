class Addressing:
    data_length = 0

    @classmethod
    def get_instruction_length(cls):
        return cls.data_length + 1

    @classmethod
    def get_offset(cls, cpu):
        return 0


class ImplicitAddressing(Addressing):
    """
    instructions that have data passed
    example: CLD, LDA
    """
    data_length = 0