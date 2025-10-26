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
The replication data and code necessary to recreate Figures 2, 3, 4 A9, and A11 are contained within the `figures/` directory. These figures were created with Python. A full environment file `figures/environment.yml` is provided, but may be difficult to recreate. The minimum required packages are given below. Version numbers are given for reference, though other versions of many of these packages are likely to work as well. The figures were created with Python 3.8.12. 

- pandas (1.2.3)
- geopandas (0.12.2)
- numpy (1.22.4)
- contextily (1.1.0)
- seaborn (0.11.1)
- pillow (8.1.2)
- matplotlib (3.3.3)  
- shapely (1.7.0) -- install with pip
- alphashape (1.3.1)

### Replication Method 1

1. Download and install [Docker Desktop](https://www.docker.com/get-started/).
2. Open your terminal (a.k.a. command prompt) and verify that docker is working properly by running: `docker --version`.
3. Clone this repository: `git clone https://github.com/haoliuhoward/undercoverPolicing.git`.
4. Within your terminal, navigate to the cloned repository's root directory (e.g., `cd undercoverPolicing/`).
5. Run the following command in your terminal: `docker run -v "./:/home" -i -t continuumio/miniconda3  /bin/bash`.
6. Verify that your terminal now reads `root@xxx:/#` where xxx is a series of alphanumeric characters.
7. In your terminal, run `cd /home`.
8. In your terminal, run `conda env create -n undercover -f environment.yml`.
9. In your terminal, run `conda activate undercover`. Verify that your terminal now reads `(undercover)`.
10. Navigate to the directory of the figure you'd like to replicate: `cd figures/fig2`.
11. Run the replication code: `python fig2.py`.

### Replication Method 2

1. Clone this repository: `git clone https://github.com/haoliuhoward/undercoverPolicing.git`.
2. Install [Anaconda](https://www.anaconda.com/download) or [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main). Restart your terminal after it is installed.
3. Within a terminal, navigate to the cloned repository's root directory.
4. In your terminal, run `conda env create -n undercover -f environment.yml`.
5. In your terminal, run `conda activate undercover`. Verify that your terminal now reads `(undercover)`.
6. Navigate to the directory of the figure you'd like to replicate: `cd figures/fig2`.
7. Run the replication code: `python fig2.py`.


### Replication Method 3

To build the necessary python environment, please see the following steps:

1. Clone this repository: `git clone https://github.com/haoliuhoward/undercoverPolicing.git`.
2. Install [Anaconda](https://www.anaconda.com/download) or [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main). Restart your terminal after it is installed.
3. Within a terminal, navigate to the cloned repository's root directory.
4. Within the terminal, navigate to the `figures/` subdirectory.
5. Within the terminal, run the following command:  
  ```
  conda create -n undercover -c conda-forge python=3.8.12 pandas=1.2.3 geopandas=0.12.2 numpy=1.22.4 contextily=1.1.0 pillow=8.1.2 seaborn=0.11.1 matplotlib=3.3.3 alphashape=1.3.1
  ```
6. Activate the python environment by running `conda activate undercover`.
7. Run `pip install shapely==1.7.0`
8. Navigate your terminal into the folder with the code you wish to run (e.g., `cd fig2/`).
9. Run the code with `python fig2.py`.

*Note*: Some figures rely on third party APIs (like contextily). You may find it difficult to perfectly replicate Figure 2 if the map tile servers change which tile themes are available. Some users, upon trying to replicate Figure 2, have reported different (but geographically accurate) background tiles from those in the manuscript. 


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
