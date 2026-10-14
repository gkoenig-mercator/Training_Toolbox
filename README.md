# Copernicus Marine Toolbox: Arctic Ocean training

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gkoenig-mercator/Training_Toolbox/main?urlpath=lab)

Hands-on training to find, download and analyse ocean data from the [Copernicus Marine Service](https://marine.copernicus.eu/) with the **Copernicus Marine Toolbox** in Python.

All examples focus on the **Arctic Ocean**: ocean physics, sea ice and in situ observations.

---

## What you will learn

By the end of the training, you will be able to:

- find a product in the **Copernicus Marine Data Store** and read its documentation
- **download original files** as delivered by the data producers (`get`)
- **extract only the data you need**, for a given area, period, depth and set of variables (`subset`)
- **work with data without downloading files**, for gridded data (`open_dataset`) and in situ observations (`read_dataframe`)
- open, map and analyse the data with **xarray** and **pandas**

No prior knowledge of the toolbox is needed. Basic Python (variables, loops, lists) is enough.

---

## Contents

Follow the notebooks in this order:

| # | Notebook | Topic | Duration |
|---|----------|-------|----------|
| 1 | [ARCTBX-01-get.ipynb](ARCTBX-01-get.ipynb) | The Data Store, downloading original files with `get`, surface temperature and sea ice | ~30 min |
| 2 | [ARCTBX-02-subset.ipynb](ARCTBX-02-subset.ipynb) | Extracting a subset with `subset`, Atlantic Water and a section across the Fram Strait | ~30 min |
| 3 | [ARCTBX-03-open-read.ipynb](ARCTBX-03-open-read.ipynb) | Remote access with `open_dataset` and `read_dataframe`, sea ice extent and in situ temperature | ~40 minutes |

Each notebook ends with exercises to go further.

---

## Before the session

### 1. Create a Copernicus Marine account

Accounts are free. Register at [data.marine.copernicus.eu/register](https://data.marine.copernicus.eu/register) and keep your **username and password** at hand: you will need them in the first notebook.

### 2. Choose where to run the notebooks

**Option A: Binder (nothing to install).**
Click the **launch binder** badge at the top of this page. JupyterLab opens in your browser with everything installed. The session is temporary: download anything you want to keep before closing it.

**Option B: on your own computer.**
Clone this repository:

```bash
git clone https://github.com/gkoenig-mercator/Training_Toolbox.git
cd Training_Toolbox
```

Then create the conda environment. Conda is recommended, especially on Windows and macOS, because `cartopy` and `netcdf4` rely on compiled libraries that conda installs for you.

```bash
conda env create -f environment.yml
conda activate copernicusmarine-training
python -m ipykernel install --user --name python_v1.1 --display-name "Copernicus Marine (Python)"
jupyter lab
```

The `ipykernel` line registers the **Copernicus Marine (Python)** kernel, which the notebooks open with automatically.

If you prefer pip, use a fresh virtual environment and run:

```bash
pip install -r requirements.txt jupyterlab
python -m ipykernel install --user --name python_v1.1 --display-name "Copernicus Marine (Python)"
jupyter lab
```

> The notebooks were written for version **2.5.0** of the toolbox. Other versions may behave slightly differently: see the toolbox's [versioning and end-of-life policy](https://toolbox-docs.marine.copernicus.eu/en/stable/end-of-life.html).

---

## How the notebooks work

- **Run the cells in order**, from top to bottom.
- **Log in once.** Your credentials are saved after the first login, so the next notebooks can skip this step.
- **Exercises** come with a **Hint**, which you can expand by clicking on it, and a **Solution** cell. Try on your own first! Running the solution cell loads the answer from the `_solved/` folder.
- **Long outputs:** right-click on a cell output and select **Enable Scrolling for Outputs** to make it easier to read.

---

## Repository layout

```
.
├── ARCTBX-0*.ipynb    # the training notebooks
├── _solved/           # solutions to the exercises
├── utils/             # plotting and analysis helpers used by the notebooks
├── img/               # screenshots shown in the notebooks
├── binder/            # environment and kernel setup used by Binder
├── environment.yml    # conda environment for local installs
└── requirements.txt   # pip alternative
```

---

## Troubleshooting

**The login cell fails or asks for my password again.**
Check your username and password on the [Copernicus Marine website](https://data.marine.copernicus.eu/). If you have just created your account, make sure you have confirmed it from the email you received.

**`ModuleNotFoundError: No module named 'copernicusmarine'`**
The notebook is running on the wrong kernel. Select **Copernicus Marine (Python)** from the kernel menu (top right of the notebook).

**A file name ends with `_(1)`, `_(2)`…**
When you run a download twice, the toolbox does not overwrite the existing file: it creates a new one with a suffix. Store the output of the command in a variable and open `response.file_path` instead of typing the file name.

**A download takes a very long time.**
Always start with `dry_run=True` to check the number of files and the total size before downloading. Some datasets are several hundred GB.

---

## Useful links

- [Copernicus Marine Data Store](https://data.marine.copernicus.eu/products): browse all products and datasets
- [Copernicus Marine Help Center](https://help.marine.copernicus.eu/): guides and FAQs
- [Toolbox documentation](https://toolbox-docs.marine.copernicus.eu/): full reference of the commands and their options
- [xarray documentation](https://docs.xarray.dev/): working with NetCDF and gridded data in Python

---

## Data credits

All data used in this training are provided by the **E.U. Copernicus Marine Service Information**.
