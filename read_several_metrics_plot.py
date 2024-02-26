import os
import glob
import matplotlib.pyplot as plt

from read_metrics_json_plot import  read_metric_json

def read_metrics_json_combine_plots(paths_json_files, label_files, metrics_names, output_path, xlabel, outname_specs):
    for metric_name in metrics_names:
        fig, ax = plt.subplots()
        for path_json_file, label_data in zip(paths_json_files, label_files):
            # Read json
            # Find json in path 
            json_file_path = glob.glob(f'{path_json_file}/*.json')[0]
            #json_file_path = f'{path_json_file}/metrics_{name_data}.json'
            metric, iters = read_metric_json(json_file_path, metric_name)

            # Plot
            ax.plot(iters, metric, label=label_data)
        ax.set_ylabel(metric_name)
        ax.set_xlabel(xlabel)
        ax.legend()

        if output_path is not None:
            filesave = f'{output_path}/{metric_name}{outname_specs}.png'
            fig.savefig(filesave, bbox_inches='tight', dpi=300)

if __name__ == "__main__":
    # Paths of metrics json files
    paths_json_files = [
            #'/mnt/d/Results/stygan2-ada/kits19/metrics_256_tl_ffhq/',
            '/mnt/d/Results/stygan2-ada/metfaces/metrics_256_tf',
            '/mnt/d/Results/stygan2-ada/metfaces/metrics_256_tffreeze4']

    labels_files = [#'kits19_256_tl', 
                    'met_256_tf', 
                    'met_256_tffr4']

    output_path = '/mnt/d/Results/stygan2-ada/metrics'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    outname_specs = '_met_256'

    xlabel = 'Iterations'

    metrics_names = ["fid50k_full", "kid50k_full", "pr50k3_full_precision", 
                    "pr50k3_full_recall", "is50k_mean", "is50k_std"]

    read_metrics_json_combine_plots(paths_json_files, labels_files, metrics_names, output_path, xlabel, outname_specs)  
