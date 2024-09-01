'''

# chmery version

import random
import statistics as s
import matplotlib.pyplot as plt

def generate_rule_signals (signals_num):
    return [-1 if random.randint(0,1) == 0 else 1 for _ in range(signals_num)]

def generate_daily_returns (returns_num):
    return [random.uniform(-5,5) for _ in range(returns_num)]

def draw_daily_return (daily_returns):
    drawed_return = random.choice(daily_returns)
    daily_returns.remove(drawed_return)
    return drawed_return;

rule_signals = generate_rule_signals(1000)
daily_returns = generate_daily_returns(1000)

# perform monte carlo permutation to obtain one mean
def calc_mean (daily_returns, rule_signals):
    daily_returns_copy = daily_returns.copy()
    random.shuffle(daily_returns_copy)
    rule_returns = []

    for signal in rule_signals:
        daily_return = draw_daily_return(daily_returns_copy)
        rule_returns.append(daily_return * signal)

    return s.mean(rule_returns)

def calc_means (means_amount):
    return [calc_mean(daily_returns, rule_signals) for _ in range(means_amount)]



# plot sampling distribution
means = calc_means(5000)
plt.title(f"Mean: {s.mean(means)}")
plt.hist(means , bins=50)
plt.show()

'''

import random
import matplotlib.pyplot    as      plt
from   time                 import  time
import numpy                as      np


if __name__ == "__main__":

    t0              = time()
    K               = 1_000
    N               = 10_000
    signal          = np.array(random.choices([-1, 1], k = K))
    daily_returns   = np.random.uniform(-5, 5, size = K)
    means           = []

    for _ in range(N):

        np.random.shuffle(daily_returns)

        means.append(np.mean(daily_returns * signal))

    print(f"{time() - t0:0.1f}s")

    plt.title(f"Mean: {np.mean(means)}")
    plt.hist(means , bins=50)
    plt.show()