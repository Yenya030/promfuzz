# PROMFUZZ


In PROMFUZZ, we first propose a novel Generative Pre-trained Transformer (GPT)-driven analysis framework, which leverages a dual-agent prompt engineering strategy to pinpoint potentially vulnerable functions for further scrutiny. We then implement a dual-stage coupling approach, which focuses on generating invariant checkers that leverage logic information, i.e., key variables and statements related to the business logic, extracted from potentially vulnerable functions. Finally, we design a bug-oriented fuzzing engine, which maps the logical information from the high-level business model to the low-level smart contract implementations, and performs the bug-oriented fuzzing on targeted functions.



This repository contains the prompts used in PROMFUZZ. We are currently in the process of a phased internal review to ensure compliance with all necessary internal and regulatory standards. The code will be released in stages, and we are dedicated to making it fully available as promptly as possible. We value and appreciate the community's patience and understanding during this process.