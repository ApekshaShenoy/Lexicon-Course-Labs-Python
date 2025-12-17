"""
4. Predict and Verify MRO  
Create a diamond-shaped inheritance structure with four classes.  
Before running the program, write down what you believe the MRO will be.  
Then print the actual MRO and compare it with your prediction. 

"""
class Device:
    def identify(self):
        print("Device")

class Mobile(Device):
    def identify(self):
        super().identify()
        print("Mobile")

class Laptop(Device):
    def identify(self):
        super().identify()
        print("Laptop")

class SmartDevice(Mobile, Laptop):
    def identify(self):

        super().identify()
        print("SmartDevice")

sd = SmartDevice()

# my prediction :[SmartDevice, Mobile, Laptop, Device, object]

sd.identify()
print(SmartDevice.mro())



