import receiver
import command

if __name__ == "__main__":

    receiver = receiver.Receiver("data")  # Employees data filename
    cmd = command.CalculateTotalAmoungCommandHandler(receiver)
    invoker = command.Invoker()
    invoker.command(cmd)
    invoker.execute()