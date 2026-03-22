# GAIA Benchmark Agent

A multi-agent system targeting the HuggingFace GAIA benchmark — real-world
task solving with web search, code execution, and mathematical reasoning.

## What it does

GAIA is a benchmark that tests AI agents on real-world tasks requiring
multi-step reasoning — looking up facts, doing calculations, reading documents,
and combining information from multiple sources.

This agent scored **60% on GAIA Level-1** using only free-tier APIs.

## Architecture
```
Task Input
    ↓
CodeAgent (smolagents)
    ↓
┌─────────────┬─────────────┬─────────────┐
│ DuckDuckGo  │ Python      │ Calculator  │
│ Web Search  │ Executor    │ Tool        │
└─────────────┴─────────────┴─────────────┘
    ↓
Final Answer
```

## Features

- Real web search via DuckDuckGo
- Safe Python code execution for calculations
- Mathematical expression evaluator
- Full GAIA validation set evaluation harness
- Automatic scoring against ground truth answers

## Installation
```bash
git clone https://github.com/devesh2304/gaia-agent
cd gaia-agent
python3 -m venv env && source env/bin/activate
pip install smolagents datasets huggingface_hub litellm ddgs python-dotenv rich
```

## Setup

Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
HF_TOKEN=your_huggingface_token_here
```

Get a free Groq API key at console.groq.com
Get a free HuggingFace token at huggingface.co

You also need to accept the GAIA dataset terms at:
huggingface.co/datasets/gaia-benchmark/GAIA

## Usage

Run a single task:
```bash
python3 -c "from agent.runner import run_task; print(run_task('What is 2+2?'))"
```

Run full evaluation:
```bash
python3 eval.py
```

## Results

| Metric | Value |
|--------|-------|
| Dataset | GAIA Level-1 validation |
| Questions | 5 |
| Score | 60% |
| Model | llama-3.3-70b-versatile via Groq |

## Stack

- Python · smolagents · LiteLLM · Groq API · DuckDuckGo · HuggingFace