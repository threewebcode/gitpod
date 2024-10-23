#!/bin/env bash

# Array of repository URLs
repositories=(
#  "https://github.com/bitcoin/bitcoin.git"
#  "https://github.com/prysmaticlabs/prysm.git"
#  "https://github.com/ethereum/solidity.git"
#  "https://github.com/succinctlabs/sp1.git"
#  "https://github.com/risc0/risc0.git"
#  "https://github.com/rust-lang/rust.git"
#  "https://github.com/ethereum/go-ethereum.git"
#  "https://github.com/sigp/lighthouse.git"
#  "https://github.com/Consensys/teku.git"
#  "https://github.com/hyperledger/besu.git"
   "https://github.com/ethereum-optimism/optimism.git"
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
