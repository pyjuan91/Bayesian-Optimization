class Params:
    PARAM1_RANGE = (-10, 10)
    PARAM2_RANGE = (-10, 10)
    PARAM3_RANGE = (-10, 10)

    def __init__(self, param1, param2, param3):
        if not (Params.PARAM1_RANGE[0] <= param1 <= Params.PARAM1_RANGE[1]):
            raise ValueError(f"param1 must be in the range {Params.PARAM1_RANGE}")
        self.param1 = param1
        if not (Params.PARAM2_RANGE[0] <= param2 <= Params.PARAM2_RANGE[1]):
            raise ValueError(f"param2 must be in the range {Params.PARAM2_RANGE}")
        self.param2 = param2
        if not (Params.PARAM3_RANGE[0] <= param3 <= Params.PARAM3_RANGE[1]):
            raise ValueError(f"param3 must be in the range {Params.PARAM3_RANGE}")
        self.param3 = param3
    


class Experiment:
    def __init__(self, params: Params):
        self.params = params

    def run(self):
        # Selfdefined function
        # TODO: Implement the function
        x1 = self.params.param1
        x2 = self.params.param2
        x3 = self.params.param3
        return -(x1**2 + x2**2 + x3**2) + 10  # Example: maximized when x1=x2=x3=0
