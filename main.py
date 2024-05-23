import experiment
import params
from skopt import gp_minimize
from skopt.space import Real, Integer


def test_package_1():
    noise_level = 0.1
    import numpy as np

    def f(params, noise_level=noise_level):
        x, y, z = params
        return np.sin(x) + y ** 2 + np.log(z) + np.random.randn(1)[0] * noise_level

    res = gp_minimize(
        f,  # the function to minimize
        [(-2.0, 2.0), (1.0, 10.0), (1.5, 100.5)],  # the bounds on each dimension of x
        acq_func="EI",  # the acquisition function
        n_calls=15,  # the number of evaluations of f
        n_random_starts=5,  # the number of random initialization points
        noise=0.1**2,  # the noise level (optional)
        random_state=1234,
    )  # the random seed
    print(f"Best parameters: {res.x}")
    print(f"Best score: {res.fun}")


def main():
    def objective_function(params):
        # Create an instance of the Params class
        p = params.Params(param1=params[0], param2=params[1], param3=params[2])
        exp = experiment.Experiment(p)
        return exp.run()

    # Define the search space
    param_space = [
        Integer(0, 10, name="param1"),
        Real(0.0, 10.5, name="param2"),
        Real(0.0, 10.0, name="param3"),
    ]

    # # Perform optimization
    result = gp_minimize(objective_function, param_space, n_calls=10, random_state=0)

    # # Retrieve the best parameters
    best_params = result.x
    best_score = -result.fun  # Negative if you are maximizing

    print(f"Best parameters: {best_params}")
    print(f"Best score: {best_score}")


if __name__ == "__main__":
    test_package_1()
    # main()
