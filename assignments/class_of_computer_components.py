class RAM():
    def __init__(self, name, capacity, type):
        self.name = name
        self.capacity = capacity
        self.type = type

    def ram_properties(self):
        print(f"\tManufacturing Company : {self.name},\n\tRam Capacity : {self.capacity},\n\tType : {self.type}")


class CPU():
    def __init__(self, name, model, speed, core):
        self.name = name
        self.model = model
        self.speed = speed
        self.core = core

    def cpu_properties(self):
        print(f"\tManufacturing Company : {self.name}\n\tModel : {self.model}\n\tSpeed in GHz : {self.speed}\n\tCores : {self.core}")


class HardDrive():
    def __init__(self, name, capacity, type):
        self.name = name
        self.capacity = capacity
        self.type = type

    def HardDrive_properties(self):
        print(f"\tManufacturing Company : {self.name},\n\tHard Drive Capacity : {self.capacity},\n\tType : {self.type}")


class Computer():
    def __init__(self, cpu, ram, hardDrive):
        self.cpu = cpu
        self.ram = ram
        self.hardDrive = hardDrive

    def properties(self):
        print("Computer Properties : \nCPU Properties : ")
        self.cpu.cpu_properties()
        print("RAM Properties : ")
        self.ram.ram_properties()
        print("Hard Drive Properties : ")
        self.hardDrive.HardDrive_properties()


ram = RAM('Intel', '8 GB', 'DDR4')
cpu = CPU('Intel', 'i7-10700K', '3.8 GHz', '8')
hardDrive = HardDrive('Seagate', '1 TB', 'SSD')
ob = Computer(cpu, ram, hardDrive)
ob.properties()
