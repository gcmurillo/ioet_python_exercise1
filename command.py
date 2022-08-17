from abc import ABC

class CalculateTotalAmountCommand(ABC):
    """ Command interface class """
    def __init__(self, receiver):
        self.receiver = receiver

    def process(self):
        pass

 
class CalculateTotalAmoungCommandHandler(CalculateTotalAmountCommand):
    """ Implements command """
    def __init__(self, receiver):
        super().__init__(receiver)

    def process(self):
        self.receiver.execute()


class Invoker:

    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.process()


