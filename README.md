# contralateral-py
v1.0.0

Code Availability (for Reviewers)
This repository contains the full simulation code used for all analyses in:
“Geometric and Evolutionary Constraints Explain the Origin of Contralateral Sensorimotor Wiring”
All three analytical components—Stage 1 (Geometric Model), Stage 2 (Evolutionary Optimization), and Stage 3 (Empirical Latency Scaling)—are implemented in a single consolidated Python file:
model.py

This file contains:
Stage 1: 1-D nondimensional geometric model and latency converter
Stage 2: Unbiased evolutionary search across 2×2 sensorimotor mappings
Stage 3: Empirical latency-scaling analysis and predictor band generation

Main controller (run_all()) to reproduce all numerical results
Empirical Data (Stage 3)

The empirical dataset used for the comparative analysis of escape latencies is included as:
stage3_empirical/empirical_dataset.csv
This CSV contains:
species	length_cm	latency_ms
All values were extracted from published mechanical fast-start measurements.

 Reproducibility
To reproduce all analyses:
python model.py
This will run:
Stage 1 geometric latency predictions
Stage 2 evolutionary search and convergence test
Stage 3 empirical comparison and predicted latency band

Upon manuscript acceptance, the full repository (including model.py and the empirical CSV) will be archived on Zenodo and receive a permanent DOI.

