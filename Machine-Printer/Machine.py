class Machine:
    def __init__(self):
        self.powered_on = False

    def power_on(self):
        if not self.powered_on:
            print("Machine is powering on.")
            self.powered_on = True
        else:
            print("Machine is already powered on.")

    def power_off(self):
        if self.powered_on:
            print("Machine is powering off.")
            self.powered_on = False
        else:
            print("Machine is already powered off.")