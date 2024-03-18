import random
import scipy.integrate as spi


def f(x):
    return x ** 2


def monte_carlo_integration(num_points, lower_bound, upper_bound):
    x_values = [random.uniform(lower_bound, upper_bound) for _ in range(num_points)]
    y_values = [random.uniform(0, f(upper_bound)) for _ in range(num_points)]

    inside_points = sum(1 for x, y in zip(x_values, y_values) if y <= f(x))
    rectangle_area = (upper_bound - lower_bound) * f(upper_bound)
    integral_value = rectangle_area * inside_points / num_points
    return integral_value


if __name__ == '__main__':
    num_points = 100_000
    a = 0
    b = 2
    print(f"""Monte Carlo integration result: {monte_carlo_integration(num_points, a, b)}""")

    result, error = spi.quad(f, a, b)
    print(f"""SciPy integration result: {result}""")
