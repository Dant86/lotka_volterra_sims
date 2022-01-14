from matplotlib.pyplot import plot, xlabel, ylabel, title, legend, \
                              savefig, rcParams
from argparse import ArgumentParser
from numpy import array, arange
from numpy.random import rand
from tqdm import tqdm

rcParams['text.usetex'] = True

def update(x, y, alpha, beta, gamma, delta, dt=1e-5):
    '''
    One update step of the Lotka-Volterra system.
    '''
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    dx, dy = dxdt * dt, dydt * dt
    return x + dx, y + dy


def run_simulation(x0, y0, alpha, beta, gamma, delta):
    '''
    Runs 10^7 update steps of the Lotka-Volterra system.
    '''
    xys = [[x0, y0]]
    for _ in range(int(1e7)):
        x_curr, y_curr = xys[-1]
        x, y = update(x_curr, y_curr, alpha, beta, gamma, delta)
        xys.append([x, y])
    return array(xys)

def plot_simulation_results(sims, labels, plot_title, fname):
    '''
    Plots the results of multiple Lotka-Volterra system
    simulations. Saves the resulting plot to the specified
    filename.
    '''
    for sim, label in zip(sims, labels):
        plot(sim[:,0], sim[:,1], label=label)
    xlabel('$x$')
    ylabel('$y$')
    title(plot_title)
    legend()
    savefig(fname)


if __name__ == '__main__':
    alpha, beta, gamma, delta = rand(4,)
    # Fix alpha, beta, gamma, and vary delta
    print('Varying delta...')
    title = 'Lotka-Volterra Simulations Where' + \
            f'$\\alpha={alpha:.2f}, \\beta={beta:.2f},' + \
            f'\\gamma={gamma:.2f}$, and $\\delta$ Varies'
    fname = 'LotkaVolterra_VaryDelta.png'
    vary_delta_sims = []
    deltas = arange(0, 1.1, .2)
    labels = [f'$\\delta={x:.2f}$' for x in deltas]
    for d in tqdm(deltas):
        sim = run_simulation(.5, .5, alpha, beta, gamma, d)
        vary_delta_sims.append(sim)
    plot_simulation_results(vary_delta_sims, labels, title, fname)
    
    # Fix alpha, beta, delta, and vary gamma
    print('Varying gamma...')
    title = 'Lotka-Volterra Simulations Where' + \
            f'$\\alpha={alpha:.2f}, \\beta={beta:.2f},' + \
            f'\\delta={delta:.2f}$, and $\\gamma$ Varies'
    fname = 'LotkaVolterra_VaryGamma.png'
    vary_gamma_sims = []
    gammas = arange(0, 1.1, .2)
    labels = [f'$\\gamma={x:.2f}$' for x in gammas]
    for g in tqdm(gammas):
        sim = run_simulation(.5, .5, alpha, beta, g, delta)
        vary_gamma_sims.append(sim)
    plot_simulation_results(vary_gamma_sims, labels, title, fname)

    # Fix alpha, gamma, delta, and vary beta
    print('Varying beta...')
    title = 'Lotka-Volterra Simulations Where' + \
            f'$\\alpha={alpha:.2f}, \\gamma={gamma:.2f},' + \
            f'\\delta={gamma:.2f}$, and $\\beta$ Varies'
    fname = 'LotkaVolterra_VaryBeta.png'
    vary_beta_sims = []
    betas = arange(0, 1.1, .2)
    labels = [f'$\\beta={x:.2f}$' for x in betas]
    for d in tqdm(betas):
        sim = run_simulation(.5, .5, alpha, b, gamma, delta)
        vary_beta_sims.append(sim)
    plot_simulation_results(vary_beta_sims, labels, title, fname)

    # Fix alpha, beta, gamma, and vary delta
    print('Varying alpha...')
    title = 'Lotka-Volterra Simulations Where' + \
            f'$\\beta={beta:.2f}, \\gamma={gamma:.2f},' + \
            f'\\delta={delta:.2f}$, and $\\alpha$ Varies'
    fname = 'LotkaVolterra_VaryAlpha.png'
    vary_alpha_sims = []
    alphas = arange(0, 1.1, .2)
    labels = [f'$\\alpha={x:.2f}$' for x in deltas]
    for a in tqdm(alphas):
        sim = run_simulation(.5, .5, a, beta, gamma, delta)
        vary_alpha_sims.append(sim)
    plot_simulation_results(vary_alpha_sims, labels, title, fname)

    # Fix all parameters and vary trajectory
    print('Varying trajectory...')
    title = 'Lotka-Volterra Simulations Where' + \
            f'$\\alpha={alpha:.2f}, \\beta={beta:.2f},' + \
            f'\\gamma={gamma:.2f}$, \\delta={delta:.2f}$,' + \
            'and Trajectory Varies'
    xys = [(.5, .5), (.75, .5), (.5, .75), (.75, .75)]
    vary_traj_sims = []
    labels = [f'$x_0={x}, y_0={y}$' for x, y in xys]
    for x, y in tqdm(xys):
        sim = run_simulation(x, y, alpha, beta, gamma, delta)
        vary_traj_sims.append(sim)
    plot_simulation_results(vary_traj_sims, labels, title, fname)

