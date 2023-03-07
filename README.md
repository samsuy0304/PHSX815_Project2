# PHSX815_Project2

# Muon Ratio
This repository contains Python scripts that simulate the decay of muons in a material and calculate the ratio of positive and negative muons.

## Contents
The repository contains the following files:

Generator.py: This script creates an instance of the Muon class and simulates the decay time of muons. It uses a while loop to keep updating the probability distribution until the estimated rate parameter exceeds a certain threshold value. It then calculates the ratio of positive and negative muons.

Muon.py: This script contains the Muon class that simulates the decay of muons in a material. The class takes several parameters such as the number of events, the probability distribution of the muons, and the decay time for both positively and negatively charged muons. The class also contains methods to update the probability distribution and simulate the decay time of the muons.

## Usage
To run the simulation and calculate the muon ratio, simply run the Generator.py script. The script will generate a plot showing the histogram of the decay time distribution and display the estimated rate parameter and the ratio of positive and negative muons.

```
python Generator.py
```

## Dependencies
The Muon.py script requires the following libraries to be installed:

`numpy`
`matplotlib`
