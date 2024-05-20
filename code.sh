#!/bin/env bash

# Array of repository URLs
repositories=(
  "https://github.com/bitcoin/bitcoin.git"
  "https://github.com/prysmaticlabs/prysm.git"
  "https://github.com/ethereum/solidity.git"
  "https://github.com/succinctlabs/sp1.git"
  "https://github.com/risc0/risc0.git"
)

# Clone or update repositories
for repository in "${repositories[@]}"; do
  # Extract repository name
  repo_name=$(basename "$repository" .git)
  
  # Check if the repository already exists
  if [ -d "$repo_name" ]; then
    echo "Repository $repo_name already exists. Skipping..."
  else
    # Clone the repository
    git clone --depth 1 "$repository"
  fi
done