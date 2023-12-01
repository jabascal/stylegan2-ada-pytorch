
#!/bin/bash

path="/mnt/d/Reports/gm_img/images2"
rename_tag="cifar10"

for file in "$path"/*.png; do
    if [[ -f "$file" ]]; then
        new_name="${file%.*}_${rename_tag}.${file##*.}"
        mv "$file" "$new_name"
    fi
done
