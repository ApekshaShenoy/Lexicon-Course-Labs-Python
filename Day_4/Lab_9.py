
"""
9. Class With a Calculation Method
Use a class with parents' heights and calculate predicted child height
for both boy and girl in centimeters.
"""

class ChildHeight:
    def __init__(self, dad_height, mom_height):
        self.dad_height = dad_height
        self.mom_height = mom_height

    def predict_height(self):
        boy_height = (self.dad_height + self.mom_height + 13) / 2
        girl_height = (self.dad_height + self.mom_height - 13) / 2

        print(f"Predicted boy height: {boy_height:.1f} cm")
        print(f"Predicted girl height: {girl_height:.1f} cm")

family1 = ChildHeight(181, 161)
family1.predict_height()


family2 = ChildHeight(180, 150)
family2.predict_height()
