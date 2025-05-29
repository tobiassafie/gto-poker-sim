# CFR - Counterfactual Regret Minimization (toy model for poker)
# Toy model - 1 street, 2 players, 10 hand types (see engine/hand_buckets.py for details)
import numpy as np
import random
from engine.hand_buckets import hand_buckets

class CFRSolver:
    def __init__(self, num_iterations=10000):
        # Initialize the CFR solver
        self.actions = ['Bet', 'Check']
        self.hands = list(hand_buckets.keys())
        self.num_actions = len(self.actions)
        self.num_hands = len(self.hands)
        self.iterations = num_iterations

        # Initialize regret and strategy arrays
        self.strategy = np.full((self.num_hands, self.num_actions), 0.5)
        self.regret_sum = np.zeros((self.num_hands, self.num_actions))
        self.strategy_sum = np.zeros((self.num_hands, self.num_actions))

    def get_strategy(self, hand_idx):
        # Calculate the strategy for a given hand index based on regret sums
        regrets = self.regret_sum[hand_idx]
        pos_regrets = np.maximum(regrets, 0)
        normalizing_sum = np.sum(pos_regrets)
        # Normalize the strategy
        # If all regrets are negative, use a uniform strategy
        if normalizing_sum > 0:
            strategy = pos_regrets / normalizing_sum
        else:
            strategy = np.full(self.num_actions, 1.0 / self.num_actions)
        self.strategy[hand_idx] = strategy
        return strategy

    def train(self):
        for _ in range(self.iterations):
            for h in range(self.num_hands):
                strategy = self.get_strategy(h)
                hand_name = self.hands[h]

                # Randomly sample utilities from defined ranges
                bet_min, bet_max = hand_buckets[hand_name][0]
                check_min, check_max = hand_buckets[hand_name][1]
                bet_utility = random.uniform(bet_min, bet_max)
                check_utility = random.uniform(check_min, check_max)

                action_utils = np.array([bet_utility, check_utility])
                node_utility = np.dot(strategy, action_utils)
                regrets = action_utils - node_utility

                self.regret_sum[h] += regrets
                self.strategy_sum[h] += strategy

    def get_average_strategy(self):
        # Calculate the average strategy across all iterations
        avg_strat = np.zeros((self.num_hands, self.num_actions))
        # Normalize the strategy sums to get the average strategy
        for h in range(self.num_hands):
            normalizing_sum = np.sum(self.strategy_sum[h])
            if normalizing_sum > 0:
                avg_strat[h] = self.strategy_sum[h] / normalizing_sum
            else:
                avg_strat[h] = np.full(self.num_actions, 1.0 / self.num_actions)
        return avg_strat
