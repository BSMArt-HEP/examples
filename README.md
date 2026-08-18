# BSMArt examples repository

This is a repository for storing examples, community example scans and contributed tools for [BSMArt](https://goodsell.pages.in2p3.fr/bsmart/).





To use the examples provided here, you should:
 * Install `BSMArt`.
 * Build the necessary model (if any). This can be done using BSMArt-PrepareModel <modelname> and will create a scan directory BSMArt_<modelname>. You can skip this step if the scan does not need to run SARAH/SPheno/HiggsTools/etc.
 * Run  `BSMArt-PrepareBSMArt <modelname> --template=<template-path>` where <template-path> is the path to the example scan you want to run. This will create a scan of that name in the BSMArt_<modelname> folder with all paths and data updated. If you are running this from a directory that is different from where you built the model, you may (depending on whether the scan needs tools like SPheno, and whether the relevant files have been stored in globally/in your virtual environment) need to add `--scriptdir=<path to ScriptsAndLogs directory>` for it to find the file `BSMArt_data_<modelname>.json`.
 * Copy any other files present (tools directory, Les Houches input files) to the newly created scan directory.


A good starting point are the toy model scans [Random](Toy/random_rosen.json), [CMAES](CMAES_ND/Toy/cmaes_rosen.json) and [CMAES_ND](CMAES_ND/Toy/cmaesnd_rosen.json): these run as-is without any model, Les Houches file or configuration, although for the latter two the cmaes (and pyod for ND) packages must be installed.