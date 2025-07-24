from abc import ABC, abstractmethod
class absClass(ABC):
    @abstractmethod
    def absMethod(self):
        pass


class childClass(absClass):
    def absMethod(self):
        print("child")

c = childClass()
c.absMethod()

# a=absClass()          will cause error as we cant instantiate abstract class
# a.absMethod()
