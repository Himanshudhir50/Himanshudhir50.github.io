class Length:
    """ {} use dictories for _metric
    """
    __metric = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000,
               "in": 0.0254, "ft": 0.3048, "yd": 0.9144,
               "mi": 1609.344}

    def __init__(self, value, unit = "m"):
        self.value = value
        self.unit = unit

     """ entered value will multiply with each and every metric value"""
    def Converse2Metres(self):
        return self.value * Length.__metric[self.unit]

    def __add__(self,other):
