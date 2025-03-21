# Multiple Sequence Alignment Analysis

**Primary Stack:** Python • BioPython • Jupyter

## Description

This project implements comprehensive multiple sequence alignment (MSA) analysis workflows, including consensus sequence calculation, position-specific scoring matrices (PSSM), sequence profile visualization, and Markov chain simulation for biological sequence analysis.

## Problem

Analyzing biological sequences requires computing consensus sequences from multiple alignments, generating position-specific scoring matrices (PSSMs), and creating sequence logo visualizations. Additionally, understanding stochastic processes like Markov chains helps model biological phenomena such as state transitions.

## Approach

The project implements three main components:

1. **Consensus Sequence Calculation**: Processes multiple sequence alignments (MSA) from FASTA files to derive consensus sequences using BioPython's `AlignInfo` module.

2. **Sequence Profile Analysis**: Generates position-specific scoring matrices (PSSMs) and converts them to probability-based profiles, then visualizes them as sequence logos using logomaker.

3. **Markov Chain Simulation**: Implements a discrete-time Markov chain simulator for modeling state transitions with custom transition matrices.

## Tech Stack

- **Python 3.x**: Core programming language
- **BioPython**: Sequence alignment and analysis
- **logomaker**: Sequence logo visualization
- **numpy**: Numerical computations
- **Jupyter Notebook**: Interactive analysis (markov_simulation.ipynb)

## Project Structure

```
msa-consensus-pssm-and-markov/
├── consensus_sequence.py           # Consensus sequence calculation from MSA
├── sequence_profile.py             # PSSM generation and sequence logo creation
├── markov_simulation.py            # Markov chain simulator
├── markov_simulation.ipynb         # Interactive Markov chain analysis
├── msa_output.fasta                # Multiple sequence alignment results
├── raw_sequences.fasta             # Input raw sequence data
├── requirements.txt                # Python dependencies
└── README.md                        # This file
```

## Setup / Installation

1. Ensure you have Python 3.7+ installed:
```bash
python --version
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

The requirements include:
- `biopython>=1.79` - Sequence alignment and analysis
- `logomaker` - Sequence logo visualization  
- `numpy>=1.21.0` - Numerical operations
- `matplotlib>=3.3.0` - Plotting support
- `jupyter>=1.0.0` - Interactive notebook

## Usage

### 1. Consensus Sequence Calculation

Calculate a consensus sequence from a multiple sequence alignment:

```bash
python consensus_sequence.py msa_output.fasta
```

**Output**: Prints the consensus sequence to stdout.

### 2. Sequence Profile Analysis

Generate PSSM, create probability-based profiles, and produce sequence logos:

```bash
python sequence_profile.py msa_output.fasta
```

**Outputs**:
- `sequence_analysis_sequence_profile.csv` - Position-specific probability matrix
- `sequence_analysis_sequence_logo.png` - Visual sequence logo (50x5 inches)

**Custom Output Prefix**: Set the `MSA_OUTPUT_PREFIX` environment variable to customize output filenames:
```bash
# Linux/Mac
export MSA_OUTPUT_PREFIX="my_analysis"
python sequence_profile.py msa_output.fasta

# Windows (Command Prompt)
set MSA_OUTPUT_PREFIX=my_analysis
python sequence_profile.py msa_output.fasta

# Windows (PowerShell)
$env:MSA_OUTPUT_PREFIX="my_analysis"
python sequence_profile.py msa_output.fasta
```

### 3. Markov Chain Simulation

#### Command-line version:
```bash
python markov_simulation.py
```

#### Interactive Jupyter notebook:
```bash
jupyter notebook markov_simulation.ipynb
```

The simulation models state transitions (e.g., city visits) using a transition matrix and tracks the frequency of each state over 100 steps.

## Data Files

### Input Files

- **raw_sequences.fasta**: Raw biological sequences in FASTA format
  - Contains unaligned sequences for initial processing
  
### Output Files

- **msa_output.fasta**: Multiple sequence alignment results
  - Generated from MSA tool (e.g., Clustal Omega, MUSCLE)
  - Used as input for consensus and profile analysis

## Key Features

### Consensus Sequence Module
- Reads MSA files in FASTA format
- Uses BioPython's `AlignInfo.SummaryInfo`
- Applies `dumb_consensus` with threshold=0 for conservative consensus
- Handles single alignment files (typical for Clustal Omega output)

### Sequence Profile Module
- Generates position-specific scoring matrices (PSSM)
- Converts raw counts to probability distributions
- Exports as CSV with sorted amino acid headers
- Creates high-resolution sequence logos (chemistry color scheme)
- Configurable for different sequence types

### Markov Chain Simulator
- Discrete-time Markov chain implementation
- Customizable transition matrices
- Simulates N steps starting from any state
- Tracks and reports state frequencies
- Example: Models traveler movement between cities

## Expected Outputs

### consensus_sequence.py
```
Consensus sequence printed to stdout
Example: MSFKILVACGLLL...
```

### sequence_profile.py
```
Files created:
- sequence_analysis_sequence_profile.csv (CSV with probability matrix)
- sequence_analysis_sequence_logo.png (Sequence logo visualization)
```

### markov_simulation.py / .ipynb
```
total number of cities visited: 100
Time in each city visited:
Berlin: 32
Munich: 38
Hamburg: 30
```
