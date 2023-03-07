# PHSX815_Project2

# Muon Ratio
This repository contains Python scripts that simulate the decay of muons in a material and calculate the ratio of positive and negative muons.

## Contents
The repository contains the following files:

Muon.py: Simulates the decay time of muons. It uses a while loop to keep updating the probability distribution until the estimated rate parameter reaches the literature value of average muon lifetime. It then calculates the ratio of positive and negative muons.

Generator.py: This script contains the Muon class that simulates the decay of muons using exponential sampling for decay time. The class takes several parameters such as the number of events, the probability distribution of the muons, and the decay time for both positively and negatively charged muons. The class also contains methods to update the probability distribution and simulate the decay time of the muons.
## Required Improvements
* Edit the Muon.py file so that the parameters can be changed from the command line. 
* Add analysis file.
## Required Feedback
I would appreciate feedback on:
* Whether the project matches the required project description.
* I know I am using the posterior probability distribution. (If not please let me know). I am confused about what to do in the analysis part. My idea is that my Hypothesis will be --> H0 => # Negative Muons/ # Postive Muons == 1 and H1 => # Negative Muons/ # Postive Muons /= 1 

## Usage
To run the simulation and calculate the muon ratio, simply run the Generator.py script. The script will generate a plot showing the histogram of the decay time distribution and display the estimated rate parameter and the ratio of positive and negative muons.

```
python Generator.py
```

## Dependencies
The Muon.py script requires the following libraries to be installed:

`numpy`
`matplotlib`
