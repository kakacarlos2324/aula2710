class Monitor:
    def __init__(self):
        self.marca = ""
        self.tamanho = 0

class Computador:
    def __init__(self):
        self.nome = ""
        self.monitor = None

# Example usage:
# Creating a monitor separately
monitor1 = Monitor()
monitor1.marca = "Monitor A"
monitor1.tamanho = 24

# Creating a computer with a monitor
computador1 = Computador()
computador1.nome = "PC 1"
computador1.monitor = monitor1

# Creating a computer without a monitor
computador2 = Computador()
computador2.nome = "PC 2"

# Accessing information
print(computador1.nome)  # Output: PC 1
print(computador1.monitor.marca)  # Output: Monitor A
print(computador2.nome)  # Output: PC 2
print(computador2.monitor)  # Output: None