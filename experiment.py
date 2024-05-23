import params


class Experiment:
    def __init__(self, params: params.Params):
        self.params = params

    def run(self):
        # Selfdefined function
        # TODO: Implement the function
        return self.params.param1 + self.params.param2 + self.params.param3
