#!/bin/python3

from datetime import datetime  # Allows us to have the timestamp
from subprocess import run  # Allows us to use the btrfs command
from configparser import RawConfigParser  # Allows us to read in a configuration file
from ast import literal_eval  # Allows us to make our values from the configuration file usable
from glob import glob  # Sorts the contents of the snapshot directory
from os import listdir, path  # //
from sys import exit  # Exit the program if something is wrong
from argparse import ArgumentParser  # Pass arguments to the script

# Argument parser setup
argument_parser = ArgumentParser()
argument_parser.add_argument('-i', '--info', default='default', help='add additionnal information', required=False)
argument_parser.add_argument('-c', '--create', action="store_true", help='create snapshots')
argument_parser.add_argument('-d', '--delete', action="store_true", help='delete old snapshots')
argument_parser.add_argument('-w', '--wipe', action="store_true", help='wipe snapshots')
option = argument_parser.parse_args()

try:
    # Config parser setup
    config_parser = RawConfigParser()
    config_parser.read('/etc/snapshot/snapshot.conf')
except:
    exit("File not found !")

try:
    # Dictionary from each sections
    subvolume_dictionary = dict(config_parser.items('subvolumes'))
    main_dictionary = dict(config_parser.items('main'))
except:
    exit("Sections not found !")

try:
    # Constants from the main section
    snapshot_dir = literal_eval(main_dictionary['snapshot_dir'])
    keep_snapshots = int(main_dictionary['keep_snapshots'])
    date_format = literal_eval(main_dictionary['date_format'])
    current_date = datetime.now().strftime(date_format)
except:
    exit("Main items not found !")


# Create snapshots
def create_snapshot():
    for subvol_name in subvolume_dictionary:

        # Values from each items of the subvolumes section
        subvol_directory = literal_eval(subvolume_dictionary[subvol_name])
        subvol_information = option.info

        try:
            run(['btrfs', 'subvolume', 'snapshot', '-r', f'{subvol_directory}',
                f'{snapshot_dir}/{current_date}_{subvol_information}_{subvol_name}'], check=True)
        except:
            exit("Creation of snapshots failed.")


# Delete old snapshots
def delete_snapshot():
    for subvol_name in subvolume_dictionary:

        # Sort every snapshots from the directory by date of creation
        old_snapshots = sorted(glob(path.join(
            snapshot_dir, f'*{subvol_name}')), key=path.getmtime)

        try:
            # Here I slice everything except the last snapshots
            for snap in old_snapshots[:-keep_snapshots]:
                run(['btrfs', 'subvolume', 'delete', f'{snap}'], check=True)
        except:
            exit("Deletion of snapshots failed.")


# Wipe all snapshots
def wipe_snapshot():
    # Ask if we really want to delete all our subvolumes
    ask_wipe = input("Do you want to delete ALL your subvolumes ? This action is irreversible (y|n): ")
    if ask_wipe.lower() != "y":
        exit("Cancellation of the deletion !")

    # Get every subvolumes from the snapshot dir
    snapshot_dictionary = listdir(f'{snapshot_dir}')

    # Here I delete every subvolumes inside the snapshot dir
    for snapshot_name in snapshot_dictionary:
        try:
            run(['btrfs', 'subvolume', 'delete', f'{snapshot_dir}/{snapshot_name}'], check=True)
        except:
            exit("Deletion of snapshots failed.")


# Assigns a function to the options
if option.create:
    create_snapshot()
if option.delete:
    delete_snapshot()
if option.wipe:
    wipe_snapshot()
