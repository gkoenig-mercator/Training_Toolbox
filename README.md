# Introduction to the Copernicus Marine Toolbox

Hands-on training to discover, explore and download ocean data from the [Copernicus Marine Service](https://marine.copernicus.eu/) with the **Copernicus Marine Toolbox** in Python.

The examples focus on **polar regions**: Arctic physics and biogeochemistry models, sea ice, ocean colour and in-situ observations.

---

## What you will learn

By the end of this session, you will be able to:

- **search** the Copernicus Marine catalogue and read the metadata of products and datasets (`describe`)
- **download original files** as delivered by the data producers (`get`)
- **extract only the data you need**, for a given area, period, depth and set of variables (`subset`)
- open and plot the downloaded data with **xarray**

No prior knowledge of the toolbox is needed. Basic Python (variables, loops, lists) is enough.

---

## Contents

Follow the notebooks in this order:

| # | Notebook | Topic | Duration |
|---|----------|-------|----------|
| 1 | `Tutorial_introduction_describe.ipynb` | Exploring the catalogue and its metadata | ~15 min |
| 2 | `Tutorial_introduction_get.ipynb` | Downloading original files | ~25 min |
| 3 | `Tutorial_introduction_subset.ipynb` | Extracting a subset of a dataset | ~25 min |
| 4 | `Tutorial_final_exercise.ipynb` | Quiz and final project: sea ice in the Barents Sea | ~15 min |

The `videos/` folder contains short screen recordings used in the notebooks. You don't need to open them separately: they play directly inside the notebooks.

---

## Before the session

### 1. Create a Copernicus Marine account

Accounts are free. Register at [data.marine.copernicus.eu/register](https://data.marine.copernicus.eu/register) and keep your **username and password** at hand: you will need them in the first notebook.

### 2. Get the notebooks

If you are using the JupyterLab provided for the training, everything is already set up and you can skip this step.

Otherwise, clone this repository:

```bash
git clone <URL of this repository>
cd <repository folder>
```

Then install the required packages:

```bash
pip install copernicusmarine==2.5.0 xarray pandas matplotlib jupyterlab
```

> The notebooks were written for version **2.5.0** of the toolbox. Other versions may behave slightly differently.

---

## How the notebooks work

- **Run the cells in order**, from top to bottom.
- **Log in once.** Your credentials are saved after the first login, so the next notebooks can skip this step.
- **Exercises** are followed by a **Hint**, which you can expand by clicking on it, and a **Solution** section. Try on your own first!
- **Long outputs:** right-click on a cell output and select **Enable Scrolling for Outputs** to make it easier to read.

---

## Troubleshooting

**The login cell fails or asks for my password again.**
Check your username and password on the [Copernicus Marine website](https://data.marine.copernicus.eu/). If you have just created your account, make sure you have confirmed it from the email you received.

**A file name ends with `_(1)`, `_(2)`…**
When you run a download twice, the toolbox does not overwrite the existing file: it creates a new one with a suffix. Store the output of the command in a variable and open `response.file_path` instead of typing the file name.

**A download takes a very long time.**
Always start with `dry_run=True` to check the number of files and the total size before downloading. Some datasets are several hundred GB.

**A cell from the catalogue (`describe`) is very slow.**
That's expected: without a `product_id` or `dataset_id`, describe goes through the whole catalogue.

---

## Useful links

- [Copernicus Marine Data Store](https://data.marine.copernicus.eu/products): browse all products and datasets
- [Toolbox documentation](https://toolbox-docs.marine.copernicus.eu/): full reference of the commands and their options
- [xarray documentation](https://docs.xarray.dev/): working with NetCDF and gridded data in Python

---

## Data credits

All data used in this training are provided by the **E.U. Copernicus Marine Service Information**.
