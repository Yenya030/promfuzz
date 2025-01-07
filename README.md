# PROMFUZZ


In PROMFUZZ, we first propose a novel Generative Pre-trained Transformer (GPT)-driven analysis framework, which leverages a dual-agent prompt engineering strategy to pinpoint potentially vulnerable functions for further scrutiny. We then implement a dual-stage coupling approach, which focuses on generating invariant checkers that leverage logic information extracted from potentially vulnerable functions. Finally, we design a bug-oriented fuzzing engine, which maps the logical information from the high-level business model to the low-level smart contract implementations, and performs the bug-oriented fuzzing on targeted functions.



## Installation


Follow the steps below to install and set up the project on your local machine:

```
    pip install -r requirements.txt  # The file was exported directly from my machine。

    sudo apt install libssl-dev libz3-dev pkg-config cmake build-essential clang
    
    cd ./fuzzingengine 

    cargo build --release

```



## Usage

### LLM-driven Multi-Perspective Analysis & Invariant Generation


* Invoke the python API in `./llmanalysis/script` and `./invariantgenerant/script`

### Bug-oriented Analysis Engine

* Insert the previously generated invariant into the smart contract.

* Move the smart contract files to the `./fuzzingengine/contracts` directory, and compile Smart Contracts.

    ```solc *.sol -o . --bin --abi ```

* Running the analysis engine.

    ```./fuzzingengine/target/release/cli evm -t './contracts/*' ```





