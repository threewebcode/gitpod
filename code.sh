#!/bin/env bash

# Array of repository URLs
repositories=(
  "https://github.com/elys-network/elys.git"
#  "https://github.com/google-gemini/gemini-cli.git"
#  "https://github.com/blockworks-foundation/mango-v4-service.git"
#  "https://github.com/blockworks-foundation/mango-v4-ui.git"
#  "https://github.com/anza-xyz/solana-sdk.git"
#  "https://github.com/anza-xyz/agave.git"
#  "https://github.com/blockworks-foundation/mango-v4.git"
#  "https://github.com/drift-labs/protocol-v2.git"
#  "https://github.com/Ellipsis-Labs/phoenix-v1.git"
#  "https://github.com/Bonfida/dex-v4.git"
#  "https://github.com/mrgnlabs/marginfi-v2.git"
#  "https://github.com/saros-xyz/saros-swap.git"
#  "https://github.com/solana-labs/perpetuals.git"
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
#  "https://github.com/dydxprotocol/v4-web.git"
#  "https://github.com/dydxprotocol/v4-infrastructure.git"
#  "https://github.com/drift-labs/gateway.git"
#  "https://github.com/drift-labs/dlob-server.git"
#  "https://github.com/drift-labs/protocol-v2.git"
#  "https://github.com/perpetual-protocol/perp-docs.git"
#  "https://github.com/perpetual-protocol/perp-oracle-contract.git"
#  "https://github.com/perpetual-protocol/perp-curie-contract.git"
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
