# MO833 Experiment instructions
## Build docker image and donwload files
in order do build docker image and download cifar10 dataset, cd to this folder and simply run:
`python3 build_experiment.py`
in both master and worker machines. then to run the experiment, run:
`python3 experiment_master.py`
on master machine and
`python3 experiment_worker.py`
on worker machine

in both cases, the master machine private IP will be requested in order to proceed.
