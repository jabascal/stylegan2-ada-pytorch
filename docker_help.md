# Docker commands for the different utilities of StyleGAN2-ADA

## GENERATION  
output in out/
```
    ./docker_run.sh python3 generate.py --outdir=out --trunc=1 --seeds=85,265,297,849     --network=https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada-pytorch/pretrained/metfaces.pkl

    ./docker_run.sh python3 generate.py --outdir=out --trunc=1 --seeds=0,10,20,30,85,265,297,849 --network=out/model.pkl
```

## TRAIN
```
    ./docker_run.sh python3 train.py --outdir=out/training-runs --data=out/cifar10.zip --gpus=1
```

## TRANSFER LEARNING
resume     = None, # Load previous network: 'noresume' (default), 'ffhq256', 'ffhq512', 'ffhq1024', 'celebahq256', 'lsundog256', <file>, <url>
freezed    = None, # Freeze-D: <int>, default = 0 discriminator layers
```
    ./docker_run.sh python3 train.py --outdir=out/training-runs --data=out/metfaces_256.zip --gpus=1 --resume='ffhq256' 

    ./docker_run.sh python3 train.py --outdir=out/training-runs --data=out/cifar10.zip --gpus=1 --resume=out/network-snapshot-001400.pkl 
```

## EVALUATION - METRICS
### Previous training run: look up options automatically, save result to text file.
```
    python calc_metrics.py --metrics=pr50k3_full \
        --network=~/training-runs/00000-ffhq10k-res64-auto1/network-snapshot-000000.pkl
```
### Pretrained network pickle: specify dataset explicitly, print result to stdout
* download a pre-trained network pickle, in which case the values of --mirror and --metricdata have to be specified explicitly.
* many of the metrics have a significant one-off cost (up to an hour or more) when they are calculated for the first time using a given datase
*  using a different random seed each time 

```
    python calc_metrics.py --metrics=fid50k_full --metricdata=~/datasets/ffhq --mirror=1 \
        --network=https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada/pretrained/ffhq.pkl
```

```
    ./docker_run.sh python3 calc_metrics.py --metrics=fid50k_full,kid50k_full,pr50k3_full,is50k --data=out/cifar10.zip --network=out/network-snapshot-001400.pkl >> output.txt
```

* Metrics (1024 x 1024, 256 x 256) ADA paper:
    fid50k_full	15 min	5 min	Fréchet inception distance[1] against the full dataset.
    kid50k_full	15 min	5 min	Kernel inception distance[2] against the full dataset.
    pr50k3_full	20 min	10 min	Precision and recall[3] againt the full dataset.
    is50k	    25 min	5 min	Inception score[4] for CIFAR-10.

To read and display the results, use the following:
```
    ./copy_networks_specific_iters.sh
    ./docker_run_eval_models_diff_iters.sh
    python read_metrics_output_json.py
    python read_metrics_json_plot.py
```

## PROJECTING IMAGES INTO LATENT SPACE
```
    python projector.py --outdir=out --target=targetimg.png \
        --network=https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada/pretrained/ffhq.pkl
```

-  target image should be cropped and aligned similar to the original FFHQ dataset

- You can render the resulting latent vector by specifying --dlatents for python generate.py
```
    python generate.py --outdir=out --dlatents=out/dlatents.npz \
        --network=https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada/pretrained/ffhq.pkl
```

## NOTES
-If docker not recognize in wsl, open docker desktop settings and check default distro and leave open
-Model model.pkl must be within current dir