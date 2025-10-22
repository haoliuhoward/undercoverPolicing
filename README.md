# Covert Assignments
## Undercover Infiltration and the Repression of Protests

Authors
---
- Howard Liu
- Benjamin J. Radford


Replication Instructions
---
This folder contains all materials needed to replicate our results. You can find the replication codes in the *R* folder. Results can be replicated by either the *.R* code or the *.qmd* code. *.R* code will show all results in R while *.qmd* code will produce the results in a clean pdf. We recommend opening the *undercoverPolicing.Rproj* and run the code because doing so you won't be needing to set working directories. 

Figure Replication Instructions
---
The replication data and code necessary to recreate Figures 2, 3, 4 A9, and A11 are contained within the `figures/` directory. These figures were created with Python. A full environment file `figures/environment.yml` is provided, but may be difficult to recreate. The minimum required packages are given below. Version numbers are given for reference, though other versions of many of these packages are likely to work as well. The figures were created with Python 3.8.2. 

- pandas (1.2.3)
- geopandas (0.10.2)
- numpy (1.19.2)
- contextily (1.1.0)
- seaborn (0.11.1)
- pillow (8.1.2)
- matplotlib (3.3.3)  
  - mpl_toolkits (should be provided with matplotlib)
- datetime
- shapely (1.7.0)
- alphashape (1.3.1)

To build the necessary python environment, please see the following steps:

1. Clone this repository (`git clone https://github.com/haoliuhoward/undercoverPolicing.git`).
2. Install [Anaconda](https://www.anaconda.com/download) or [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main).
3. Within a terminal, navigate to the cloned repository's root directory.
4. Within the terminal, navigate to the `figures/` subdirectory.
5. Run `conda env create -f undercover.yml` to create the necessary python environment.
6. Activate the python environment by running `conda activate undercover`.
7. Navigate your terminal into the folder with the code you wish to run (e.g., `cd fig2/`).
8. Run the code with `python fig2.py`.


Citations
---

Please cite this paper as follows:

Liu, Howard and Benjamin J. Radford. 2025. "Covert Assignments: Undercover Infiltration and the Repression of Protests." _International Studies Quarterly_.

```
@article{liu:radford:2025,
    author={Howard Liu and Benjamin J. Radford},
    title={{Covert Assignments: Undercover Infiltration and the Repression of Protests}},
    journal={{International Studies Quarterly}},
    year={2025},
    volume={},
    number={},
    pages={},
    DOI={}}
```
