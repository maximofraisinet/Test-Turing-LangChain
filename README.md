Test Turing Bot
===========

A small experimental chatbot prototype built to explore LangChain and evaluate whether a carefully crafted initial prompt can help the bot pass a simple Turing-style test.

What it is
- Minimal Python bot using LangChain to drive a local or remote LLM.
- The project centers on an initial system/user prompt designed to encourage human-like responses for manual Turing-style evaluation.

Purpose
- Experimentation and learning: verify prompting strategies and LangChain integration when attempting to make responses that are indistinguishable from a human in short conversational exchanges.

How to run
- Execute the main script with: `python test_turing.py`.
- Configure your model or credentials as required by your LangChain/LLM setup before running (this project does not bundle model binaries or provider credentials).
