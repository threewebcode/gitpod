#!/bin/env bash

# Array of repository URLs
repositories=(
#  "https://github.com/jtroo/kanata.git"
#  "https://github.com/plandex-ai/plandex.git"
#  "https://github.com/lapce/lapce.git"
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
#  "https://github.com/ethereum-optimism/optimism.git"
#  "https://github.com/pancakeswap/pancake-frontend.git"
#  "https://github.com/Uniswap/interface.git"
#  "https://github.com/gmx-io/gmx-contracts.git"
#  "https://github.com/dydxprotocol/v4-documentation.git"
#  "https://github.com/dydxprotocol/v4-chain.git"
  "https://github.com/dydxprotocol/v4-web.git"
  "https://github.com/dydxprotocol/v4-infrastructure.git"
#  "https://github.com/drift-labs/gateway.git"
#  "https://github.com/drift-labs/dlob-server.git"
#  "https://github.com/drift-labs/protocol-v2.git"
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
