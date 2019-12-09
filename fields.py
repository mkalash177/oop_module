#from abc import ABC, abstractmethod
from validators import *

class AbstractField(ABC):
    @abstractmethod
    def __init__(self, validators=None):
        pass

    @abstractmethod
    def is_valid(self, value):
        pass

class CharField(AbstractField):
    def __init__(self, validators=None):
        self.default = [TextValidator(min_length=0, max_length=999)]
        self.all_validators = self.default
        if isinstance(validators, list) and validators:
            self.all_validators += validators

    def is_valid(self, value):
        list_v = [i.is_valid(value) for i in self.all_validators]
        for i in list_v:
            if i is False:
                return False
            return True


class TextField(AbstractField):
    def __init__(self, validators=None):
        self.default = [TextValidator(min_length=1001, max_length=3000)]
        self.all_validators = self.default
        if isinstance(validators, list) and validators:
            self.all_validators += validators

    def is_valid(self, value):
        list_v = [i.is_valid(value) for i in self.all_validators]
        for i in list_v:
            if i is False:
                return False
            return True

class IntegerField(AbstractField):
    def __init__(self, validators=None):
        self.default = [IntegerValidator(min_value=128, max_value=1024)]
        self.all_validators = self.default
        if isinstance(validators, list) and validators:
            self.all_validators += validators

    def is_valid(self, value):
        list_v = [i.is_valid(value) for i in self.all_validators]
        for i in list_v:
            if i is False:
                return False
            return True
