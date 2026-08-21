# Manus UI Research Hub

This repository is the **integration hub** for the public-source research and deterministic development lanes.

## Submodule Model

The hub will pin exactly two user-owned repositories by commit SHA:

| Path | Repository role | Owning organization |
|---|---|---|
| `research/manus-public-ui-research` | Source inventories, static assessments, and synthetic research fixtures | `search-astute-ly` |
| `development/manus-ui-adapter-lab` | Deterministic local adapter helpers and tests | `Research-Astute` |

Submodules are references, not runtime dependencies. Every pin advance requires a pull request, source revision evidence, license/provenance review, and deterministic integrity validation.

## Integration Boundary

The hub coordinates documentation, release checks, and reviewable references. It does not collect account data, execute remote scripts, use credentials or session material, run browser automation, or make network-probing requests. CI remains read-only and validates only repository metadata, file policy, and local tests.

## Parallel Development Flow

The research lane publishes evidence-backed observations. The development lane consumes only approved, synthetic contracts. The hub accepts a reference only after both lanes provide a matching provenance identifier and test/assessment record. No source is copied into the hub through broad directory transfer.
