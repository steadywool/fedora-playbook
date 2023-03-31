#!/bin/python3

import datetime  # Allows us to have the timestamp
import subprocess  # Allows us to use the btrfs command
import configparser  # Allows us to read in a configuration file
import ast  # Allows us to make our values from the configuration file usable
import glob  # Sorts the contents of the snapshot directory
import os  # //
import sys  # Exit the program if something is wrong
import argparse  # Pass arguments to the script

# Only execute this script as root
if not os.geteuid() == 0:
    sys.exit("Execute this script as root !")

# Argument parser setup
argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('-i', '--info', default='default', help='add additionnal information', required=False)
argument_parser.add_argument('-c', '--create', action="store_true", help='create snapshots')
argument_parser.add_argument('-d', '--delete', action="store_true", help='remove old snapshots')
option = argument_parser.parse_args()

try:
    # Config parser setup
    config_parser = configparser.RawConfigParser()
    config_parser.read('/etc/snapshot/snapshot.conf')
except:
    sys.exit("File not found !")

try:
    # Dictionary from each sections
    subvolume_dictionary = dict(config_parser.items('subvolumes'))
    main_dictionary = dict(config_parser.items('main'))
except:
    sys.exit("Sections not found !")

try:
    # Constants from the main section
    snapshot_dir = ast.literal_eval(main_dictionary['snapshot_dir'])
    keep_snapshots = int(main_dictionary['keep_snapshots'])
    date_format = ast.literal_eval(main_dictionary['date_format'])
    current_date = datetime.datetime.now().strftime(date_format)
except:
    sys.exit("Main items not found !")


# Create snapshots
def create_snapshot():
    for subvol_name in subvolume_dictionary:

        # Values from each items of the subvolumes section
        subvol_directory = ast.literal_eval(subvolume_dictionary[subvol_name])
        subvol_information = option.info

        try:
            subprocess.run(['btrfs', 'subvolume', 'snapshot', '-r',
                           f'{subvol_directory}', f'{snapshot_dir}/{current_date}_{subvol_information}_{subvol_name}'], check=True)
        except:
            sys.exit("Creation of snapshots failed.")


# Delete old snapshots
def delete_snapshot():
    for subvol_name in subvolume_dictionary:

        # Sort every snapshots from the directory by date of creation
        old_snapshots = sorted(glob.glob(os.path.join(
            snapshot_dir, f'*{subvol_name}')), key=os.path.getmtime)

        try:
            # Here I slice everything except the last snapshots
            for snap in old_snapshots[:-keep_snapshots]:
                subprocess.run(
                    ['btrfs', 'subvolume', 'delete', f'{snap}'], check=True)
        except:
            sys.exit("Deletion of snapshots failed.")


# Assigns a function to the options
if option.create:
    create_snapshot()
if option.delete:
    delete_snapshot()
