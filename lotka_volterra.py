from matplotlib.pyplot import plot, xlabel, ylabel, title, legend, \
                              savefig, rcParams
from argparse import ArgumentParser
from numpy.random import rand
from numpy import array

rcParams['text.usetex'] = True

def update(x, y, alpha, beta, gamma, delta, dt=1e-5):
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    dx, dy = dxdt * dt, dydt * dt
    return x + dx, y + dy


def run_simulation(x0, y0, alpha, beta, gamma, delta):
    xys = [[x0, y0]]
    for _ in range(int(1e7)):
        x_curr, y_curr = xys[-1]
        x, y = update(x_curr, y_curr, alpha, beta, gamma, delta)
        xys.append([x, y])
    return array(xys)

if __name__ == '__main__':
    parser = ArgumentParser(description='Lotka-Volterra Simulations')
    parser.add_argument('-x0', type=float, help='initial x value',
                        default=1.)
    parser.add_argument('-y0', type=float, help='initial y value',
                        default=1.)
    parser.add_argument('-n_plots', type=int, help='number of sims',
                        default=5)
    arguments = parser.parse_args()

    x, y = arguments.x0, arguments.y0
    labels = ['\\alpha', '\\beta', '\\gamma', '\\delta']
    for _ in range(arguments.n_plots):
        d = dict(zip(labels, list(rand(4,))))
        alpha, beta, gamma, delta = list(d.values())
        label_str = ', '.join([f'${k}={v:.2f}$' for k, v in d.items()])
        sim = run_simulation(x, y, alpha, beta, gamma, delta)
        plot(sim[:,0], sim[:,1], label=label_str)
    xlabel('$x$')
    ylabel('$y$')
    title(f'Lotka-Volterra Simulations where $x_0={x}$ and $y_0={y}$')
    legend()
    savefig(f'lotka_volterra_x={x:.2f}_y={y:.2f}.png')

