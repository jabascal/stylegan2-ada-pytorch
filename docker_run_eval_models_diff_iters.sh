#!/bin/bash

function run_metrics() {
    iters=(200 400 800 1400)
    data_file="out/cifar10.zip"
    file_output_main="out_metrics_cifar10"
    for iter in "${iters[@]}"; do
        file_output="${file_output_main}_${iter}.txt"
        ./docker_run.sh python3 calc_metrics.py --metrics=fid50k_full,kid50k_full,pr50k3_full,is50k --data={data_file} --network=out/network-snapshot-00${metric}.pkl >> $file_output
    done
}

run_metrics
