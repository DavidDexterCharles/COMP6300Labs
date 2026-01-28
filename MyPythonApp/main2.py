import numpy as np
import matplotlib.pyplot as plt


def main():
    # Simple NumPy example
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Simple Matplotlib example
    plt.plot(x, y)
    plt.title("Sine Wave Example")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.show()


if __name__ == "__main__":
    main()