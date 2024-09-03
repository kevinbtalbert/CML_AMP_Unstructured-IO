#!/bin/bash

# Add the target repository as a remote
git remote add unstructured-ingest https://github.com/Unstructured-IO/unstructured-ingest.git

# Enable sparse checkout
git config core.sparseCheckout true

# Set the subdirectory to fetch
echo "example-docs/*" >> .git/info/sparse-checkout

# Fetch and checkout the subdirectory
git fetch unstructured-ingest main
git checkout unstructured-ingest/main
