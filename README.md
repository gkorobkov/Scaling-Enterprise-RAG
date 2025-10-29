# Enterprise RAG - Scaling Retrieval Augmented Generation

A comprehensive evaluation framework for testing and scaling Retrieval Augmented Generation (RAG) systems in enterprise environments. This project provides automated testing infrastructure to validate RAG system responses against expected answers using multiple LLM providers.

## Overview

This project implements an evaluation system that:
- Tests RAG system outputs against predefined question-answer pairs
- Supports multiple LLM providers (OpenAI GPT-4, LMStudio with Qwen models)
- Provides automated pass/fail evaluation of generated answers
- Offers flexible test execution methods for different development workflows

## Features

### Multi-Provider LLM Support
- **OpenAI Integration**: Uses GPT-4o for answer evaluation
- **LMStudio Integration**: Local model support with Qwen3-4B-2507
- Configurable provider selection for evaluation tasks

### Automated Answer Evaluation
- Compares generated RAG answers against expected answers
- Returns PASS/FAIL results based on semantic equivalence
- Detailed evaluation logging with question, expected, and generated answers
- Assertion-based testing for CI/CD integration

### Flexible Test Execution
Three methods to run evaluations:
1. **Pytest with output**: `python -m pytest evals\test_evals.py -s`
2. **Standalone script**: `python evals\run_test.py`
3. **Pytest verbose**: `python -m pytest evals\test_evals.py --capture=no -v`

### Sample Test Dataset
Includes example questions covering:
- Product descriptions ("What is Underwhelming Spatula?")
- Author attribution ("Who wrote 'Dubious Parenting Tips'?")
- Content metadata ("How long is Almost-Perfect Investment Guide?")

## Project Structure

```
Scaling-Enterprise-RAG/
├── evals/
│   ├── evaluate.py       # Core evaluation logic with LLM integrations
│   ├── test_evals.py     # Pytest test cases and evaluation runner
│   └── run_test.py       # Standalone test executor
├── .env                  # Environment configuration (not in repo)
├── template.env          # Environment template
├── .gitignore           
└── README.md
```

## Installation

Install required dependencies:

```bash
pip install openai
pip install python-dotenv
pip install pytest 
pip install lmstudio
```

Or use a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt  # If available
```

## Configuration

1. Copy the template environment file:
```bash
copy template.env .env
```

2. Configure your API credentials in `.env`:
```env
OPENAI_API_KEY="your-openai-api-key"
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4o
OPENAI_SCOPE=your-scope
```

3. Select evaluation model in `evals/evaluate.py`:
```python
model_type = "lms"  # or "openai"
```

## Usage

### Running Evaluations

Choose one of the following methods:

**Method 1: Pytest with output capture**
```bash
python -m pytest evals\test_evals.py -s
```

**Method 2: Standalone script (guaranteed output)**
```bash
python evals\run_test.py
```

**Method 3: Pytest verbose mode**
```bash
python -m pytest evals\test_evals.py --capture=no -v
```

### Integrating Your RAG System

1. Replace the placeholder `run_RAG()` function in `test_evals.py`:
```python
def run_RAG(user_question):
    # Replace with your actual RAG system call
    return "IDKLOL"  # Current placeholder
```

2. Add your own test cases:
```python
eval_questions = [
    "Your question here?",
]

eval_answers = [
    "Your expected answer here.",
]
```

3. Run the tests to validate your RAG system performance

## How It Works

1. **Question Processing**: Test questions are sent to the RAG system via `run_RAG()`
2. **Answer Generation**: RAG system generates answers for each question
3. **Evaluation**: Generated answers are compared to expected answers using an LLM evaluator
4. **Judgment**: Evaluator returns PASS if answers are semantically equivalent, FAIL otherwise
5. **Reporting**: Detailed output shows questions, expected/generated answers, and evaluation results

## Evaluation Criteria

The evaluation system uses LLM-based semantic comparison rather than exact string matching:
- **PASS**: Generated answer provides the same information as expected answer
- **FAIL**: Generated answer differs significantly from expected answer

This approach handles variations in phrasing while ensuring content accuracy.

## Development

### Adding New Test Cases
Edit `evals/test_evals.py` and add to the `eval_questions` and `eval_answers` lists.

### Switching LLM Providers
Modify the `model_type` variable in `evals/evaluate.py`:
- `"openai"`: Uses OpenAI GPT-4o (requires API key)
- `"lms"` or `"qwen"`: Uses local LMStudio with Qwen model

### Custom Evaluation Logic
Extend `evaluate_generated_answer()` in `evals/evaluate.py` to implement custom evaluation criteria.

## Future Enhancements

- Support for additional LLM providers
- Metrics tracking (accuracy, response time)
- Batch evaluation reporting
- Integration with CI/CD pipelines
- RAG system performance benchmarking
- Vector database evaluation support

## License

[Specify your license here]

## Contributing

[Add contribution guidelines if applicable]