import numpy as np
import pandas as pd

np.random.seed(42)

# ---------- Helper Functions ----------

def clipped_normal(mean, std, low, high, size):
    values = np.random.normal(mean, std, size)
    return np.clip(values, low, high)


# ---------- Persona Definitions ----------

PERSONAS = {
    "casual": {
        "count": 360,
        "avg_session_time": (22, 5, 10, 40),
        "sessions_per_week": (3, 1, 1, 5),
        "levels_completed": (10, 4, 2, 20),
        "time_to_complete_level": (16, 4, 10, 25),
        "death_rate": (3, 1, 1, 5),
        "retry_rate": (0.5, 0.5, 0, 2),
        "accuracy": (55, 8, 40, 70),
        "exploration_score": (0.4, 0.1, 0.2, 0.6),
        "aggression_score": (0.4, 0.1, 0.2, 0.6),
        "completion_rate": (60, 10, 40, 75),
    },

    "hardcore": {
        "count": 180,
        "avg_session_time": (90, 15, 60, 130),
        "sessions_per_week": (6, 1, 4, 7),
        "levels_completed": (45, 10, 25, 65),
        "time_to_complete_level": (6, 1, 4, 9),
        "death_rate": (0.5, 0.5, 0, 2),
        "retry_rate": (0.5, 0.5, 0, 2),
        "accuracy": (90, 3, 80, 98),
        "exploration_score": (0.3, 0.1, 0.1, 0.5),
        "aggression_score": (0.7, 0.1, 0.5, 0.9),
        "completion_rate": (95, 3, 85, 99),
    },

    "explorer": {
        "count": 240,
        "avg_session_time": (70, 15, 40, 110),
        "sessions_per_week": (4, 1, 2, 6),
        "levels_completed": (22, 6, 10, 35),
        "time_to_complete_level": (22, 6, 12, 35),
        "death_rate": (2, 1, 0, 4),
        "retry_rate": (1.5, 0.5, 0, 3),
        "accuracy": (68, 6, 55, 80),
        "exploration_score": (0.9, 0.05, 0.7, 1.0),
        "aggression_score": (0.3, 0.1, 0.1, 0.5),
        "completion_rate": (78, 7, 65, 90),
    },

    "speedrunner": {
        "count": 120,
        "avg_session_time": (35, 8, 15, 55),
        "sessions_per_week": (5, 1, 3, 7),
        "levels_completed": (40, 8, 25, 55),
        "time_to_complete_level": (4.5, 1, 2.5, 7),
        "death_rate": (2, 1, 0, 4),
        "retry_rate": (3, 1, 1, 6),
        "accuracy": (85, 5, 75, 95),
        "exploration_score": (0.1, 0.05, 0, 0.3),
        "aggression_score": (0.6, 0.1, 0.4, 0.8),
        "completion_rate": (90, 4, 80, 97),
    },

    "risk_taker": {
        "count": 180,
        "avg_session_time": (45, 10, 25, 70),
        "sessions_per_week": (4, 1, 2, 6),
        "levels_completed": (18, 6, 8, 30),
        "time_to_complete_level": (12, 3, 7, 20),
        "death_rate": (5, 1.5, 3, 8),
        "retry_rate": (2, 1, 0, 4),
        "accuracy": (62, 6, 50, 75),
        "exploration_score": (0.3, 0.1, 0.1, 0.5),
        "aggression_score": (0.9, 0.05, 0.7, 1.0),
        "completion_rate": (60, 10, 45, 75),
    },

    "persistent_learner": {
        "count": 120,
        "avg_session_time": (85, 15, 55, 130),
        "sessions_per_week": (5, 1, 3, 7),
        "levels_completed": (22, 6, 10, 35),
        "time_to_complete_level": (16, 4, 10, 25),
        "death_rate": (4, 1, 2, 6),
        "retry_rate": (4, 1, 2, 7),
        "accuracy": (60, 6, 45, 75),
        "exploration_score": (0.5, 0.1, 0.3, 0.7),
        "aggression_score": (0.5, 0.1, 0.3, 0.7),
        "completion_rate": (75, 7, 60, 88),
    }
}


# ---------- Data Generation ----------

def generate_player_data():
    all_players = []

    for persona, config in PERSONAS.items():
        n = config["count"]
        persona_data = {}

        for feature, params in config.items():
            if feature == "count":
                continue
            mean, std, low, high = params
            persona_data[feature] = clipped_normal(mean, std, low, high, n)

        df = pd.DataFrame(persona_data)
        all_players.append(df)

    final_df = pd.concat(all_players, ignore_index=True)
    return final_df
