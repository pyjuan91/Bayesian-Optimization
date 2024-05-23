import experiment
import numpy as np
from sklearn.neural_network import MLPRegressor
from scipy.optimize import minimize


def prepare_experiment(sample):
    param = experiment.Params(sample[0], sample[1], sample[2])
    experiment_instance = experiment.Experiment(param)
    return experiment_instance


def generate_initial_data(n_samples, param_ranges):
    data = []
    for _ in range(n_samples):
        sample = [np.random.uniform(low, high) for low, high in param_ranges]
        experiment_instance = prepare_experiment(sample)
        score = experiment_instance.run()
        data.append((*sample, score))
    return np.array(data)


def train_model(data):
    X = data[:, :-1]
    y = data[:, -1]
    model = MLPRegressor(hidden_layer_sizes=(50,), max_iter=1000)
    model.fit(X, y)
    return model


def surrogate_function(x, model):
    return -model.predict([x])[0]  # Negate for minimization


def optimize_parameters(model, param_ranges):
    bounds = param_ranges
    result = minimize(
        surrogate_function,
        x0=np.zeros(3),
        args=(model,),
        bounds=bounds,
        method="L-BFGS-B",
    )
    return result.x


def iterative_optimization(n_iterations, initial_data, param_ranges):
    data = initial_data
    for _ in range(n_iterations):
        model = train_model(data)
        optimal_params = optimize_parameters(model, param_ranges)
        experiment_instance = prepare_experiment(optimal_params)
        new_score = experiment_instance.run()
        new_data_point = (*optimal_params, new_score)
        data = np.vstack([data, new_data_point])
    return data


def main():
    param_ranges = [
        experiment.Params.PARAM1_RANGE,
        experiment.Params.PARAM2_RANGE,
        experiment.Params.PARAM3_RANGE,
    ]
    initial_data = generate_initial_data(20, param_ranges)
    final_data = iterative_optimization(100, initial_data, param_ranges)
    optimal_parameters = final_data[np.argmax(final_data[:, -1]), :-1]
    optimal_score = np.max(final_data[:, -1])
    print(f"Optimal Parameters: {optimal_parameters}")
    print(f"Optimal Score: {optimal_score}")


if __name__ == "__main__":
    main()
