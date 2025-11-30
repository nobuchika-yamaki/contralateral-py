# model.py
# Complete simulation framework for:
# "Geometric and Evolutionary Constraints Explain the Origin of Contralateral Sensorimotor Wiring"

import numpy as np
import pandas as pd

# ============================================================
# =======================  STAGE 1  ==========================
# ============================================================

def stage1_latency(L=1.0, v=1.0, syn=0.0, t_star=1.6):
    return (L / v) * t_star + syn

def compute_contralateral_delay(L=1.0, v=1.0):
    return L / v

def compute_ipsilateral_delay(L=1.0, v=1.0):
    return 0.0

def stage1_compare(L_list, v_list):
    records = []
    for L in L_list:
        for v in v_list:
            t_pred = stage1_latency(L=L, v=v)
            records.append([L, v, t_pred])
    return pd.DataFrame(records, columns=["Length_m", "Velocity_mps", "PredLatency_ms"])

# ============================================================
# =======================  STAGE 2  ==========================
# ============================================================

def evaluate_mapping(mapping):
    D = np.array([[0, 2],
                  [2, 0]])
    latency = np.sum(mapping * D)
    return latency

def evolutionary_search(pop_size=200, generations=200, mutation_rate=0.1):
    population = [np.random.randint(0,2,(2,2)) for _ in range(pop_size)]
    for gen in range(generations):
        scores = np.array([evaluate_mapping(m) for m in population])
        ranks = np.argsort(scores)
        population = [population[i] for i in ranks[:pop_size//2]]
        new_pop = []
        for m in population:
            child = m.copy()
            if np.random.rand() < mutation_rate:
                i,j = np.random.randint(0,2), np.random.randint(0,2)
                child[i,j] = 1 - child[i,j]
            new_pop.append(child)
        population += new_pop
    best = population[0]
    return best, evaluate_mapping(best)

# ============================================================
# =======================  STAGE 3  ==========================
# ============================================================

def load_empirical_csv(path="stage3_empirical/empirical_dataset.csv"):
    return pd.read_csv(path)

def stage3_prediction(df, v_min=5, v_max=30, t_star=1.6):
    L = df["length_cm"].values / 100.0
    df["pred_min"] = (L / v_max) * t_star * 1000
    df["pred_max"] = (L / v_min) * t_star * 1000
    df["inside_band"] = (df["latency_ms"] >= df["pred_min"]) & (df["latency_ms"] <= df["pred_max"])
    return df

# ============================================================
# ===================  MASTER CONTROLLER  =====================
# ============================================================

def run_all():
    print("Running Stage 1...")
    df1 = stage1_compare(
        L_list=np.linspace(0.01, 0.5, 10),
        v_list=[5,10,20,30]
    )
    print(df1.head())

    print("\nRunning Stage 2...")
    best, score = evolutionary_search()
    print("Best mapping:")
    print(best)
    print("Latency score:", score)

    print("\nRunning Stage 3...")
    try:
        df_emp = load_empirical_csv()
        df_out = stage3_prediction(df_emp)
        print(df_out)
    except FileNotFoundError:
        print("empirical_dataset.csv not found.")

if __name__ == "__main__":
    run_all()
