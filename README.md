# We are preprocessing EEG DataSet Using Python (MNE)

### Team 🧑🏽‍💻
  - Baila 
  - Josiah
  - Sai

## EEG Preprocessing (CleaningEEG)

This repo is our group study for learning how to preprocess EEG data in Python using MNE.  
The goal is to take raw (in this case `.edf` format) recordings and turn them into cleaner, analysis-ready signals.

### What this project does

- Load EEG recordings from `.edf` files  
- Let the user choose which recording to work with  
- Apply basic preprocessing steps:
  - set channel montage and rename channels
  - mark and remove bad channels
  - apply high-pass / low-pass / notch filters
  - re-reference the data (e.g. average reference)
- Run ICA to separate artifacts (eye blinks, muscle noise, etc.)
- Save the cleaned EEG data for later analysis/experiments

### Purpose

This project is mainly for **learning and experimentation**:
- to understand each preprocessing step with simple, readable code  
- to build an end-to-end pipeline I can reuse in future EEG projects

> ⚠️ Disclaimer:  
> This code is **not** intended for clinical or medical use(yet). It’s a student project for research and education only.

## Future Goal for this Project
Get the most accurate cleaned data possible so we can reuse this project for further studies!

## Instructions
