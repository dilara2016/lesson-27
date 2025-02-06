class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name =name
        self.max_speed=max_speed
        self.mileage = mileage
class bus (vehicle):
    pass

school_bus=bus("school volvo", 100, 122)
print("vehicle name:",school_bus.name, "speed:",school_bus.max_speed,
"mileage:", school_bus.mileage)
