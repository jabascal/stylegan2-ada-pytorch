
#!/bin/bash

# path="/mnt/d/Results/stygan2-ada/dtd/00000-dtd_256_selec_rc10-auto1-resumecustom"
path="/mnt/d/Reports/gm_img/images/new"
rename_tag="kits_256_155sub_400k"

for file in "$path"/*.png; do
    if [[ -f "$file" ]]; then
        new_name="${file%.*}_${rename_tag}.${file##*.}"
        mv "$file" "$new_name"
    fi
done
