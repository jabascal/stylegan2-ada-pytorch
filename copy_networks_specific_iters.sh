#!/bin/bash

# Define the source and destination directories
src_dir="/mnt/d/Results/stygan2-ada/metfaces"
dest_dir="out"

# Loop over the iteration numbers
for i in 200 400 800 1600 2200; do
    # Zero-pad the iteration number
    iter_num=$(printf "%06d" $i)

    # Define the source file path
    src_file="${src_dir}/00000-metfaces_64-auto1/network-snapshot-${iter_num}.pkl"

    # Copy the file
    cp $src_file $dest_dir/
done