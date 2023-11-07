from rest_framework.serializers import ValidationError
import re

class habitsValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        myString = dict(value).get(self.field, '')
        # myString = 'fdg hfd https://www.youtube.com/ hgjhdfjks https://colab.research.google.com'
        print(myString)
