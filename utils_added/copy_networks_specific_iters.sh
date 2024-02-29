#!/bin/bash

# Define the source and destination directories
src_dir="/mnt/d/Results/stygan2-ada/dtd/00000-dtd_256_rc20-auto1-resumeffhq256"
dest_dir="out"

# Loop over the iteration numbers
for i in 200 400 800 1400 2000; do
    # Zero-pad the iteration number
    iter_num=$(printf "%06d" $i)

    # Define the source file path
    src_file="${src_dir}/network-snapshot-${iter_num}.pkl"

    # Copy the file
    cp $src_file $dest_dir/
done