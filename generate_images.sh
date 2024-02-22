
#!/bin/bash

network_path="./out/network-snapshot-000400.pkl"

for ((seed=0; seed<=1020; seed+=20)); do
    seeds=$(seq -s, $seed $((seed+20)))
    ./docker_run.sh python3 generate.py --outdir=out/gen --trunc=1 --seeds=$seeds --network=$network_path
done
