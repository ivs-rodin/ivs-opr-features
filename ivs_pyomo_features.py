from pyomo.environ import ConcreteModel

__version__ = 'dev'

#TODO: Base class pyomo model
#TODO: Impvars

class PyomoSet(set):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def get_slice(self, mask):
        print(mask)
        for element in self:
            print(element)