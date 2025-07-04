# Agent Guide

pip install -r requirements.txt  # The file was exported directly from my machine。

sudo apt install libssl-dev libz3-dev pkg-config cmake build-essential clang-14

Have already been run there is no need to run those commands. 

This repository implements **PROMFUZZ**, a smart contract security analysis tool.
PROMFUZZ uses LLM-driven analysis to generate invariants and a fuzzing engine to test EVM and Move smart contracts.

## Repository structure
- `fuzzingengine/` – Rust implementation of the fuzzing engine (ItyFuzz). See `fuzzingengine/src/README.md` for details.
- `llmanalysis/` – Python code and prompt files for LLM-based multi-perspective analysis.
- `invariantgenerant/` – Python script and prompts for generating invariants from source code.
- `requirements.txt` – Python dependencies for the analysis tools.
- `README.md` – top‑level usage instructions.

### fuzzingengine
The `fuzzingengine/src` README explains the layout:
```
Folders:
- `generic_vm` - traits representing VM of any smart contracts
- `evm` - Implementation of `generic_vm` for Ethereum Virtual Machine using revm.
- `move` - Implementation of `generic_vm` for MoveVM.
- `fuzzers` - Definition of fuzzers for each VM.

Files:
- `executor.rs` - definition of `Executor` trait from LibAFL.
- `feedback.rs` - definition of `Feedback` trait from LibAFL for collecting and analyzing feedback like coverage and comparison.
- `indexed_corpus.rs` - just a corpus that has self-increment ID for each testcase.
- `input.rs` - definition of `Input` trait from LibAFL.
- `oracle.rs` - definition of `Oracle` trait.
- `scheduler.rs` - definition of `Scheduler` trait from LibAFL, implements infant scheduler proposed in paper.
- `state.rs` - definition of `State` trait from LibAFL that supports infant corpus proposed in paper.
- `state_input.rs` - implementation of `Input` trait for VM states.
- `tracer.rs` - traces of the snapshot of the state, used for regenerating the transactions leading to the VM state.

Utils:
- `rand_utils.rs` - random utilities.
- `types.rs` - utilities for type conversion.
- `telemetry.rs` - utilities for reporting fuzzing campaign telemetry information.
- `const.rs` - constants used in the project.
```

### Usage overview
According to the main README you install dependencies, build the Rust code and run the analysis engine:
```
pip install -r requirements.txt
sudo apt install libssl-dev libz3-dev pkg-config cmake build-essential clang
cd ./fuzzingengine
cargo build --release
```
Then run the engine on your compiled contracts:
```
./fuzzingengine/target/release/cli evm -t './contracts/*'
```

### Notes
Tests exist under `fuzzingengine/tests`, but they should not be executed automatically in this environment.
