#!/bin/bash

function run_metrics() {
    iters=(200 400 800 1400 2000)
    #iters=(1600 3000)
    name_data='dtd_256_selec_rc20_sub25k'
    data_file="out/${name_data}.zip"
    name_out_specs="" # '_tl'
    #data_file="out/metfaces_64.zip"
    file_output_main="out/out_metrics_${name_data}${name_out_specs}"
    for iter in "${iters[@]}"; do
        file_output="${file_output_main}_${iter}.txt"
        echo "File output: ${file_output}"
        iter_str=$(printf "%06d" $iter)
        network_file="out/network-snapshot-${iter_str}.pkl"      
        echo "Running metrics for ${network_file} ..."  
        ./docker_run.sh python3 calc_metrics.py --metrics=fid50k_full,kid50k_full,is50k,pr50k3 --data=$data_file --network=$network_file >> $file_output
        #./docker_run.sh python3 calc_metrics.py --metrics=pr50k3 --data=$data_file --network=$network_file >> $file_output
    done
}

run_metrics

