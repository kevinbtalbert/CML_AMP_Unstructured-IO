#!/bin/bash

# Define the target directory
TARGET_DIR="/home/cdsw/assets/example-docs"

# Create the target directory if it does not exist
mkdir -p "$TARGET_DIR"

# Download the repository as a ZIP file
curl -L https://github.com/Unstructured-IO/unstructured-ingest/archive/44d5db1b19d0348a958ae707c39589d65ad1472a.zip -o main.zip

# Unzip only the example-docs directory
unzip -q main.zip "unstructured-ingest-main/example-docs/*" -d temp_unstructured_ingest

# Move the example-docs directory to the target location
mv temp_unstructured_ingest/unstructured-ingest-main/example-docs/* "$TARGET_DIR"

# Clean up the temporary files and directories
rm -rf main.zip temp_unstructured_ingest
