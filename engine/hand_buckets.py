import random
'''
Dictionary of different hands and their corresponding bet + check strength value ranges.
Left value is the bet strength range, right value is the check strength range.
These values are arbitrary and can and SHOULD be adjusted by a more experienced player/modeler.
'''

# Utility ranges: [ (min_bet, max_bet), (min_check, max_check) ]
hand_buckets = {
    "Nuts": [(0.95, 1.0), (0.6, 0.7)],                 # Strongest hand, high value
    "Strong Made": [(0.85, 0.95), (0.5, 0.6)],         # Strong made hand, good value
    "Medium Made": [(0.6, 0.75), (0.55, 0.65)],        # Medium strength made hand, decent value
    "Weak Made": [(0.3, 0.5), (0.55, 0.7)],            # Weak made hand, low value
    "Draws Strong": [(0.5, 0.7), (0.45, 0.6)],         # Strong draws, potential to improve
    "Draws Weak": [(0.2, 0.5), (0.5, 0.7)],            # Weak draws, less potential
    "Air Blockers": [(0.4, 0.6), (0.2, 0.4)],          # Air hands with blockers, low value
    "Air No Blockers": [(0.1, 0.3), (0.4, 0.6)],       # Air hands without blockers, very low value
    "Marginal Bluff": [(0.5, 0.7), (0.4, 0.6)],        # Marginal bluff hands, low value
    "Trapping": [(0.7, 0.9), (0.7, 0.9)]               # Trapping hands, high value
}