#!/bin/bash

# Subvolumes to snapshots
SUBVOLUMES="/ /var"

# Only keep newest snapshots of each subvolumes
OLD=3

# Create snapshots of subvolumes
create_snapshot() {
    for subvol in ${SUBVOLUMES}; do

        # Replace / with "root", and remove / for other one
        if [[ -z ${subvol//\/} ]]; then
            subvol_name='root'
        else
            subvol_name=${subvol//\/}
        fi

        btrfs subvolume snapshot -r ${subvol} /.snapshots/$(date +%s)_${subvol_name}
    done
}

# Delete old snapshots
delete_snapshot() {
    for subvol in ${SUBVOLUMES}; do

        # Replace / with "root", and remove / for other one
        if [[ -z ${subvol//\/} ]]; then
            subvol_name='root'
        else
            subvol_name=${subvol//\/}
        fi

        # Get old snapshots name
        old_snapshots=$(ls -t /.snapshots/ | grep ${subvol_name} | sort | head -n -${OLD})

        # Delete snapshots
        for snapshots in ${old_snapshots}; do
            btrfs subvolume delete /.snapshots/${snapshots}
        done
    done
}

create_snapshot
delete_snapshot
