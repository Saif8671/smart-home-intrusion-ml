import pandas as pd
import numpy as np

np.random.seed(42)

rows = 2000
data = []

for _ in range(rows):
    hour = np.random.randint(0, 24)
    motion = np.random.uniform(0, 10)
    sound = np.random.uniform(0, 10)
    movement_count = np.random.randint(0, 20)

    door_open = np.random.choice([0, 1], p=[0.8, 0.2])
    window_open = np.random.choice([0, 1], p=[0.85, 0.15])

    # Intrusion logic
    intrusion = 0
    if (motion > 6 and sound > 6) or \
       (hour >= 0 and hour <= 5 and motion > 4) or \
       (door_open == 1 and hour >= 22):
        intrusion = 1

    data.append([
        motion,
        sound,
        movement_count,
        hour,
        door_open,
        window_open,
        intrusion
    ])

columns = [
    "motion_level",
    "sound_level",
    "movement_count",
    "hour_of_day",
    "door_open",
    "window_open",
    "label"
]

df = pd.DataFrame(data, columns=columns)
df.to_csv("data/events.csv", index=False)

print("Dataset generated successfully.")
