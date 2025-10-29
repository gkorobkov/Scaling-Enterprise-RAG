# Enterprise RAG - Scaling Retrieval Augmented Generation

A comprehensive evaluation framework for testing and scaling Retrieval Augmented Generation (RAG) systems in enterprise environments. This project provides automated testing infrastructure to validate RAG system responses against expected answers using multiple LLM providers.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Examples](#examples)
- [Project Structure](#project-structure)
- [Testing Best Practices](#testing-best-practices)
- [Troubleshooting](#troubleshooting)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project implements an evaluation system that:
- Tests RAG system outputs against predefined question-answer pairs
- Supports multiple LLM providers (OpenAI GPT-4, LMStudio with Qwen models)
- Provides automated pass/fail evaluation of generated answers
- Offers flexible test execution methods for different development workflows

## Why This Framework?

Evaluating RAG systems is challenging because:
- String matching fails to capture semantic equivalence
- Manual evaluation doesn't scale
- Different phrasings can convey the same meaning
- Enterprise RAG systems need consistent quality metrics

This framework solves these problems by using LLM-based semantic evaluation that understands meaning, not just exact matches.

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

## Prerequisites

Before installing, ensure you have:

- **Python 3.8+**: Required for all dependencies
- **pip**: Python package manager (usually comes with Python)
- **Git**: For version control and cloning the repository

### Optional Prerequisites

- **OpenAI API Key**: Required if using OpenAI for evaluation (recommended for production)
- **LMStudio**: Required if using local models for evaluation (free alternative)
  - Download from: https://lmstudio.ai/
  - Install Qwen3-4B-2507 model through LMStudio interface

## Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd Scaling-Enterprise-RAG
```

### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

**Option A: Using requirements.txt (if available)**
```bash
pip install -r requirements.txt
```

**Option B: Manual Installation**
```bash
pip install openai==1.12.0
pip install python-dotenv==1.0.0
pip install pytest==7.4.3
pip install lmstudio==0.1.0
```

**Option C: Using uv (Fast Package Manager)**
```bash
# Install uv
pip install uv

# Install dependencies
uv pip install openai python-dotenv pytest lmstudio
```

### Step 4: Verify Installation

```bash
python -c "import openai, dotenv, pytest, lmstudio; print('All dependencies installed successfully!')"
```

## Quick Start

Get up and running in 5 minutes:

### 1. Set Up Environment

```bash
# Copy environment template
copy template.env .env  # Windows
# OR
cp template.env .env    # Linux/macOS

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY="sk-your-key-here"
```

### 2. Run Your First Evaluation

```bash
# Using the standalone script (easiest)
python evals\run_test.py
```

### 3. View Results

You'll see output like:
```
============================================================
Question 1: What is Underwhelming Spatula?
Expected answer: Underwhelming Spatula is a kitchen tool...
Given answer: IDKLOL

--- Evaluation Result ---
Result: FAIL
============================================================
```

### 4. Integrate Your RAG System

Edit `evals/test_evals.py` and replace the placeholder:
```python
def run_RAG(user_question):
    # Replace this with your actual RAG system
    response = your_rag_system.query(user_question)
    return response
```

### 5. Run Tests Again

```bash
python -m pytest evals\test_evals.py -s
```

## Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# OpenAI Configuration (Required if using OpenAI)
OPENAI_API_KEY="sk-your-actual-api-key-here"
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4o
OPENAI_SCOPE=default

# Optional: Custom settings path
SETTINGS_PATH="settings\settings.json"
```

### Configuration Options

#### 1. OpenAI Configuration

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes (for OpenAI) | None |
| `OPENAI_BASE_URL` | API endpoint URL | No | https://api.openai.com/v1 |
| `OPENAI_MODEL` | Model to use | No | gpt-4o |
| `OPENAI_SCOPE` | API scope/organization | No | None |

**Getting an OpenAI API Key:**
1. Visit https://platform.openai.com/api-keys
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key and add to your `.env` file

#### 2. Model Selection

Edit `evals/evaluate.py` to choose your evaluation model:

```python
# Line ~18 in evaluate.py
model_type = "openai"  # Options: "openai", "lms", "qwen"
```

**Model Options:**

| Option | Provider | Cost | Speed | Setup |
|--------|----------|------|-------|-------|
| `openai` | OpenAI GPT-4o | Paid | Fast | API key only |
| `lms` | LMStudio (Qwen) | Free | Moderate | LMStudio + model download |
| `qwen` | LMStudio (Qwen) | Free | Moderate | Same as `lms` |

#### 3. LMStudio Configuration (Optional)

If using local models:

1. **Download LMStudio**: https://lmstudio.ai/
2. **Install Model**:
   - Open LMStudio
   - Search for "qwen3-4b-2507"
   - Click download
3. **Start Server**:
   - Click "Local Server" tab
   - Click "Start Server"
4. **Set Model Type**: In `evaluate.py`, set `model_type = "lms"`

### Test Dataset Configuration

Customize test cases in `evals/test_evals.py`:

```python
# Your custom questions
eval_questions = [
    "What are the office hours?",
    "Who is the CEO?",
    "What's the return policy?",
]

# Expected answers from your knowledge base
eval_answers = [
    "Office hours are Monday-Friday, 9 AM to 5 PM EST.",
    "The CEO is Jane Smith.",
    "Items can be returned within 30 days with receipt.",
]
```

## Usage

### Running Evaluations

Three execution methods are available, each suited for different scenarios:

#### Method 1: Standalone Script (Recommended for Development)

Best for: Quick testing, debugging, guaranteed console output

```bash
python evals\run_test.py
```

**Advantages:**
- Guaranteed output visibility
- No pytest configuration needed
- Easy to run and understand
- Good for debugging

**Output Example:**
```
============================================================
Запуск теста run_RAG
============================================================
Question 1: What is Underwhelming Spatula?
Expected answer: Underwhelming Spatula is a kitchen tool...
Given answer: IDKLOL
--- Evaluation Result ---
Result: FAIL
✅ Тест выполнен успешно!
```

#### Method 2: Pytest with Output Capture

Best for: Development, detailed output, watching assertions

```bash
python -m pytest evals\test_evals.py -s
```

**Advantages:**
- Full pytest features
- Detailed test output
- Shows assertion failures
- Good for CI/CD integration

#### Method 3: Pytest Verbose Mode

Best for: Detailed debugging, understanding test flow

```bash
python -m pytest evals\test_evals.py --capture=no -v
```

**Advantages:**
- Most detailed output
- Shows test discovery
- Displays all print statements
- Best for troubleshooting

#### Additional Pytest Options

```bash
# Run specific test
python -m pytest evals\test_evals.py::test_run_RAG -v

# Stop on first failure
python -m pytest evals\test_evals.py -x

# Show local variables on failure
python -m pytest evals\test_evals.py -l

# Generate HTML report
python -m pytest evals\test_evals.py --html=report.html
```

### Integrating Your RAG System

#### Step 1: Implement RAG Function

Replace the placeholder in `evals/test_evals.py`:

```python
def run_RAG(user_question):
    """
    Integration point for your RAG system.
    
    Args:
        user_question (str): The question to answer
        
    Returns:
        str: The generated answer from your RAG system
    """
    # Example: Using LangChain
    from your_rag_module import rag_chain
    response = rag_chain.invoke({"query": user_question})
    return response["answer"]
    
    # Example: Using custom RAG
    # from your_module import query_knowledge_base
    # return query_knowledge_base(user_question)
```

#### Step 2: Add Your Test Cases

```python
eval_questions = [
    "What is your company's refund policy?",
    "How do I reset my password?",
    "What are the shipping costs?",
]

eval_answers = [
    "We offer full refunds within 30 days of purchase.",
    "Click 'Forgot Password' on the login page and follow the email instructions.",
    "Shipping is free for orders over $50, otherwise $5.99 flat rate.",
]
```

#### Step 3: Run Evaluation

```bash
python evals\run_test.py
```

### Advanced Usage

#### Batch Testing with Custom Questions

Create a JSON file with test cases:

```json
// test_cases.json
{
  "test_suite_1": {
    "questions": [
      "What are your business hours?",
      "Do you ship internationally?"
    ],
    "answers": [
      "Monday-Friday 9 AM - 5 PM EST",
      "Yes, we ship to over 50 countries"
    ]
  }
}
```

Load and run:

```python
import json

with open('test_cases.json') as f:
    test_data = json.load(f)

eval_questions = test_data['test_suite_1']['questions']
eval_answers = test_data['test_suite_1']['answers']
```

#### Programmatic Execution

```python
from evals.test_evals import test_run_RAG

# Run tests programmatically
try:
    test_run_RAG()
    print("All tests passed!")
except AssertionError as e:
    print(f"Test failed: {e}")
```

## API Documentation

### Core Functions

#### `evaluate_generated_answer(expected_answer, generated_answer)`

Evaluates the quality of a generated answer against an expected answer using LLM-based semantic comparison.

**Location:** `evals/evaluate.py`

**Parameters:**
- `expected_answer` (str): The correct/expected answer from your knowledge base
- `generated_answer` (str): The answer generated by your RAG system

**Returns:**
- `str`: Evaluation result containing "PASS" if answers are semantically equivalent, "FAIL" otherwise

**Example:**
```python
from evals.evaluate import evaluate_generated_answer

expected = "The office is open Monday through Friday, 9 AM to 5 PM."
generated = "We're open weekdays from 9 to 5."

result = evaluate_generated_answer(expected, generated)
print(result)  # Should contain "PASS"
```

**Internal Behavior:**
1. Constructs evaluation prompt comparing both answers
2. Sends to configured LLM (OpenAI or LMStudio)
3. Returns LLM judgment as string

---

#### `send_to_openai(message)`

Sends a message to OpenAI's GPT-4o model for processing.

**Location:** `evals/evaluate.py`

**Parameters:**
- `message` (str): The prompt/message to send to the model

**Returns:**
- `str`: The model's response text (stripped of whitespace)

**Environment Variables Required:**
- `OPENAI_API_KEY`: Your OpenAI API key

**Example:**
```python
from evals.evaluate import send_to_openai

response = send_to_openai("Explain RAG in one sentence.")
print(response)
```

**Configuration:**
- Model: `gpt-4o`
- Temperature: Default (1.0)
- Max tokens: Default (unlimited)

---

#### `send_to_lms(message)`

Sends a message to a local LMStudio model for processing.

**Location:** `evals/evaluate.py`

**Parameters:**
- `message` (str): The prompt/message to send to the model

**Returns:**
- `str`: The model's response text

**Prerequisites:**
- LMStudio installed and running
- Qwen3-4B-2507 model downloaded

**Example:**
```python
from evals.evaluate import send_to_lms

response = send_to_lms("What is RAG?")
print(response)
```

**Configuration:**
- Model: `qwen/qwen3-4b-2507`
- Runs via LMStudio local server

---

#### `run_RAG(user_question)`

Integration point for your RAG system. This is where you connect your actual RAG implementation.

**Location:** `evals/test_evals.py`

**Parameters:**
- `user_question` (str): The question to be answered by your RAG system

**Returns:**
- `str`: The answer generated by your RAG system

**Default Implementation:**
```python
def run_RAG(user_question):
    return "IDKLOL"  # Placeholder - replace with your RAG system
```

**Example Implementations:**

**LangChain Integration:**
```python
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma

def run_RAG(user_question):
    vectorstore = Chroma(persist_directory="./chroma_db")
    qa_chain = RetrievalQA.from_chain_type(
        llm=your_llm,
        retriever=vectorstore.as_retriever()
    )
    result = qa_chain({"query": user_question})
    return result["result"]
```

**Custom RAG:**
```python
def run_RAG(user_question):
    # Retrieve relevant documents
    docs = vector_db.similarity_search(user_question, k=3)
    
    # Create context
    context = "\n".join([doc.page_content for doc in docs])
    
    # Generate answer
    prompt = f"Context: {context}\n\nQuestion: {user_question}\n\nAnswer:"
    answer = llm.generate(prompt)
    
    return answer
```

---

#### `test_run_RAG()`

Main test function that runs the complete evaluation pipeline.

**Location:** `evals/test_evals.py`

**Parameters:** None

**Returns:** None (uses pytest assertions)

**Behavior:**
1. Iterates through all questions in `eval_questions`
2. Calls `run_RAG()` for each question
3. Compares generated answer with expected answer using `evaluate_generated_answer()`
4. Asserts that result contains "PASS"
5. Prints detailed output for each evaluation

**Example Output:**
```
============================================================
Question 1: What is Underwhelming Spatula?
Expected answer: Underwhelming Spatula is a kitchen tool...
Given answer: A kitchen tool that combines whimsy with function.

--- Evaluation Result ---
Result type: <class 'str'>
Result value: PASS
Result contains 'PASS': True
============================================================
```

**Raises:**
- `AssertionError`: If evaluation result doesn't contain "PASS"

---

### Test Data Structures

#### `eval_questions`

List of questions to test against your RAG system.

**Type:** `list[str]`

**Location:** `evals/test_evals.py`

**Example:**
```python
eval_questions = [
    "What is Underwhelming Spatula?",
    "Who wrote 'Dubious Parenting Tips'?",
    "How long is Almost-Perfect Investment Guide?",
]
```

---

#### `eval_answers`

List of expected answers corresponding to `eval_questions`.

**Type:** `list[str]`

**Location:** `evals/test_evals.py`

**Important:** Must be same length as `eval_questions` and in matching order.

**Example:**
```python
eval_answers = [
    "Underwhelming Spatula is a kitchen tool that redefines expectations...",
    "Lisa Melton wrote Dubious Parenting Tips.",
    "The Almost-Perfect Investment Guide is 210 pages long.",
]
```

---

### Environment Variables Reference

| Variable | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `OPENAI_API_KEY` | string | Conditional* | None | OpenAI API authentication key |
| `OPENAI_BASE_URL` | string | No | https://api.openai.com/v1 | OpenAI API endpoint |
| `OPENAI_MODEL` | string | No | gpt-4o | Model identifier for OpenAI |
| `OPENAI_SCOPE` | string | No | None | Organization or project scope |
| `SETTINGS_PATH` | string | No | None | Path to custom settings JSON |

\* Required only if using OpenAI as evaluation model

---

### Error Handling

#### Common Errors

**`openai.AuthenticationError`**
```
Problem: Invalid or missing OPENAI_API_KEY
Solution: Check .env file and verify API key is correct
```

**`ValueError: Unknown model_type`**
```
Problem: Invalid model_type in evaluate.py
Solution: Set model_type to "openai", "lms", or "qwen"
```

**`ConnectionError` (LMStudio)**
```
Problem: LMStudio not running or model not loaded
Solution: Start LMStudio and ensure model is active
```

**`AssertionError: Expected PASS in result`**
```
Problem: RAG answer doesn't match expected answer
Solution: Check RAG implementation or adjust expected answers
```

---

## How It Works

### Evaluation Pipeline

```
┌─────────────────┐
│  Test Questions │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   run_RAG()     │  ← Your RAG System Integration
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Generated Answer│
└────────┬────────┘
         │
         ▼
┌─────────────────────────────┐
│ evaluate_generated_answer() │
│  • Compares with expected   │
│  • Uses LLM for evaluation  │
│  • Returns PASS/FAIL        │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────┐
│  Test Result    │
│  (PASS/FAIL)    │
└─────────────────┘
```

### Execution Flow

1. **Question Processing**: Test questions are sent to the RAG system via `run_RAG()`
2. **Answer Generation**: RAG system generates answers for each question
3. **Evaluation**: Generated answers are compared to expected answers using an LLM evaluator
4. **Judgment**: Evaluator returns PASS if answers are semantically equivalent, FAIL otherwise
5. **Reporting**: Detailed output shows questions, expected/generated answers, and evaluation results
6. **Assertion**: Test fails if any evaluation doesn't contain "PASS"

## Examples

### Example 1: Basic RAG Evaluation

```python
# test_evals.py
from evaluate import evaluate_generated_answer

def run_RAG(user_question):
    # Simple mock RAG system
    knowledge_base = {
        "What are your hours?": "We're open Monday-Friday, 9 AM to 5 PM.",
        "Where are you located?": "123 Main St, New York, NY 10001"
    }
    return knowledge_base.get(user_question, "I don't know.")

eval_questions = ["What are your hours?"]
eval_answers = ["Monday through Friday, 9 AM - 5 PM"]

def test_run_RAG():
    for i, question in enumerate(eval_questions):
        answer = run_RAG(question)
        result = evaluate_generated_answer(eval_answers[i], answer)
        assert "PASS" in result
```

**Run it:**
```bash
python -m pytest test_evals.py -s
```

---

### Example 2: LangChain Integration

```python
# langchain_rag.py
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Setup
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.load_local("./my_index", embeddings)
llm = ChatOpenAI(model_name="gpt-3.5-turbo")

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
)

def run_RAG(user_question):
    result = qa_chain({"query": user_question})
    return result["result"]

# Use with evaluation framework
eval_questions = [
    "What is the company's return policy?",
    "How do I track my order?",
]

eval_answers = [
    "Items can be returned within 30 days with original receipt.",
    "Use the tracking number sent to your email on the shipping carrier's website.",
]
```

---

### Example 3: Custom RAG with Pinecone

```python
# pinecone_rag.py
import pinecone
from openai import OpenAI

# Initialize
pinecone.init(api_key="your-key", environment="us-west1-gcp")
index = pinecone.Index("my-index")
client = OpenAI()

def run_RAG(user_question):
    # Get embedding for question
    embedding_response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=user_question
    )
    embedding = embedding_response.data[0].embedding
    
    # Query Pinecone
    results = index.query(
        vector=embedding,
        top_k=3,
        include_metadata=True
    )
    
    # Build context
    context = "\n\n".join([match.metadata["text"] for match in results.matches])
    
    # Generate answer
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Answer based on the context provided."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {user_question}"}
        ]
    )
    
    return response.choices[0].message.content
```

---

### Example 4: Multi-Model Evaluation

Compare performance across different evaluation models:

```python
# multi_model_eval.py
from evaluate import send_to_openai, send_to_lms

def evaluate_with_both_models(expected, generated):
    prompt = f"Expected: {expected}\nGenerated: {generated}\nEvaluation:"
    
    openai_result = send_to_openai(prompt)
    lms_result = send_to_lms(prompt)
    
    print(f"OpenAI says: {openai_result}")
    print(f"LMStudio says: {lms_result}")
    
    return {
        "openai": "PASS" in openai_result,
        "lms": "PASS" in lms_result
    }

# Use it
results = evaluate_with_both_models(
    "The product costs $49.99",
    "It's priced at fifty dollars"
)
```

---

### Example 5: Batch Testing from CSV

```python
# batch_test_csv.py
import csv
from evaluate import evaluate_generated_answer

def run_RAG(question):
    # Your RAG implementation
    pass

def test_from_csv(filepath):
    results = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            question = row['question']
            expected = row['expected_answer']
            
            generated = run_RAG(question)
            evaluation = evaluate_generated_answer(expected, generated)
            
            results.append({
                'question': question,
                'passed': 'PASS' in evaluation,
                'evaluation': evaluation
            })
    
    # Generate report
    passed = sum(1 for r in results if r['passed'])
    total = len(results)
    print(f"Results: {passed}/{total} passed ({passed/total*100:.1f}%)")
    
    return results

# CSV format:
# question,expected_answer
# "What are shipping costs?","$5.99 for orders under $50"
# "Do you ship internationally?","Yes, to over 50 countries"

results = test_from_csv('test_cases.csv')
```

---

### Example 6: Performance Benchmarking

```python
# benchmark.py
import time
from evaluate import evaluate_generated_answer

def run_RAG(question):
    # Your RAG implementation
    pass

def benchmark_rag(questions, answers):
    times = []
    results = []
    
    for question, expected in zip(questions, answers):
        start = time.time()
        generated = run_RAG(question)
        end = time.time()
        
        times.append(end - start)
        eval_result = evaluate_generated_answer(expected, generated)
        results.append('PASS' in eval_result)
    
    print(f"Average response time: {sum(times)/len(times):.2f}s")
    print(f"Pass rate: {sum(results)/len(results)*100:.1f}%")
    print(f"Fastest query: {min(times):.2f}s")
    print(f"Slowest query: {max(times):.2f}s")

benchmark_rag(eval_questions, eval_answers)
```

---

## Project Structure

```
Scaling-Enterprise-RAG/
│
├── evals/                      # Evaluation framework
│   ├── __init__.py
│   ├── evaluate.py             # Core evaluation logic
│   │   ├── send_to_openai()   # OpenAI API integration
│   │   ├── send_to_lms()      # LMStudio integration
│   │   └── evaluate_generated_answer()  # Main evaluation function
│   │
│   ├── test_evals.py           # Test cases and RAG integration
│   │   ├── run_RAG()          # RAG system integration point
│   │   ├── eval_questions[]   # Test questions
│   │   ├── eval_answers[]     # Expected answers
│   │   └── test_run_RAG()     # Main test function
│   │
│   └── run_test.py             # Standalone test executor
│
├── .env                        # Environment variables (git-ignored)
├── template.env                # Environment template
├── .gitignore                  # Git ignore rules
├── README.md                   # This file
└── requirements.txt            # Python dependencies (optional)
```

### File Descriptions

| File | Purpose | Key Components |
|------|---------|----------------|
| `evaluate.py` | LLM evaluation logic | Model integrations, evaluation prompts |
| `test_evals.py` | Test framework | RAG integration, test data, assertions |
| `run_test.py` | Test runner | Standalone execution, error handling |
| `.env` | Configuration | API keys, model settings |
| `template.env` | Config template | Example configuration values |

---

## Testing Best Practices

### 1. Start with Known-Good Answers

Begin with questions where you're confident of the correct answer:

```python
# Good: Factual, verifiable
eval_questions = [
    "What is the company founded date?",
    "What is the product SKU for item X?"
]

# Avoid: Subjective, ambiguous
eval_questions = [
    "Is the product good?",
    "What do customers think?"
]
```

### 2. Use Representative Questions

Test questions should cover your actual use cases:

```python
# Cover different question types
eval_questions = [
    "What is X?",              # Definition
    "How do I do Y?",          # Procedure
    "When does Z happen?",     # Temporal
    "Where can I find W?",     # Location
    "Why does V occur?",       # Causation
]
```

### 3. Test Edge Cases

Include challenging scenarios:

```python
eval_questions = [
    "What about products under $10?",           # Boundary condition
    "Do you ship to Antarctica?",               # Unusual case
    "What's your policy on refunds after 31 days?",  # Near-miss case
]
```

### 4. Maintain Answer Quality

Expected answers should be:
- **Accurate**: Match your source documents
- **Complete**: Include all necessary information
- **Concise**: Not overly verbose
- **Consistent**: Similar style across all answers

```python
# Good expected answer
"Items can be returned within 30 days of purchase with original receipt for full refund."

# Too vague
"We accept returns."

# Too verbose
"Our return policy states that customers who are not satisfied..."
```

### 5. Version Your Test Data

Track changes to test cases:

```python
# Add metadata
eval_metadata = {
    "version": "1.2",
    "last_updated": "2024-01-15",
    "author": "team@company.com"
}
```

### 6. Regular Test Maintenance

- **Review monthly**: Update questions as knowledge base changes
- **Add new tests**: When adding new content
- **Remove obsolete**: Delete outdated questions
- **Refine failures**: Investigate and fix recurring failures

### 7. Gradual Rollout

When integrating your RAG system:

1. Start with 3-5 test cases
2. Verify they pass
3. Add 5 more
4. Continue until you have 20-30 tests
5. Monitor pass rate over time

### 8. Document Test Intent

```python
# Document why each test exists
eval_questions = [
    "What is the return policy?",  # Core FAQ - must always work
    "Can I return opened software?",  # Edge case reported by support
    "What about defective items?",  # Legal requirement
]
```

---

## Troubleshooting

### Common Issues and Solutions

#### 1. Import Errors

**Problem:**
```
ModuleNotFoundError: No module named 'openai'
```

**Solution:**
```bash
# Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install openai python-dotenv pytest lmstudio
```

---

#### 2. OpenAI Authentication Failed

**Problem:**
```
openai.AuthenticationError: Invalid API key
```

**Solutions:**
1. Verify `.env` file exists in project root
2. Check API key format: `OPENAI_API_KEY="sk-..."`
3. Verify key is active at https://platform.openai.com/api-keys
4. Ensure no extra quotes or spaces

```bash
# Check if environment variable is loaded
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('OPENAI_API_KEY'))"
```

---

#### 3. LMStudio Connection Failed

**Problem:**
```
ConnectionError: Could not connect to LMStudio
```

**Solutions:**
1. Start LMStudio application
2. Load the Qwen model in LMStudio
3. Start the local server (Local Server tab → Start Server)
4. Verify server is running on default port

```python
# Test LMStudio connection
import lmstudio as lms
try:
    model = lms.llm("qwen/qwen3-4b-2507")
    print("LMStudio connected successfully")
except Exception as e:
    print(f"Connection failed: {e}")
```

---

#### 4. All Tests Failing

**Problem:**
```
AssertionError: Expected PASS in result, got: FAIL
```

**Diagnostic Steps:**

1. **Check if RAG is implemented:**
```python
# In test_evals.py
def run_RAG(user_question):
    print(f"RAG called with: {user_question}")  # Add logging
    return "IDKLOL"  # If this is still here, RAG isn't implemented
```

2. **Verify evaluation model is working:**
```python
from evaluate import evaluate_generated_answer
result = evaluate_generated_answer("The sky is blue", "The sky is blue")
print(result)  # Should contain PASS
```

3. **Check model_type configuration:**
```python
# In evaluate.py, line ~18
model_type = "openai"  # Must be "openai", "lms", or "qwen"
```

---

#### 5. No Output Visible

**Problem:**
Tests run but no output appears

**Solutions:**

Use standalone runner:
```bash
python evals\run_test.py
```

Or force pytest output:
```bash
python -m pytest evals\test_evals.py -s -v --capture=no
```

Add explicit prints:
```python
import sys
sys.stderr.write("This will always show\n")
sys.stderr.flush()
```

---

#### 6. Inconsistent Evaluation Results

**Problem:**
Same answer gets PASS sometimes, FAIL other times

**Causes & Solutions:**

1. **LLM variance**: Language models can vary
   - Solution: Run multiple times and check consistency
   - Consider using temperature=0 for deterministic results

2. **Ambiguous expected answers**:
```python
# Vague - inconsistent evaluation
"We ship to many countries"

# Specific - consistent evaluation  
"We ship to USA, Canada, UK, and 47 other countries"
```

3. **Model type inconsistency**:
   - Use the same model consistently
   - Document which model was used

---

#### 7. Slow Evaluation

**Problem:**
Tests take too long to run

**Solutions:**

1. **Use local models:**
```python
model_type = "lms"  # Faster than API calls
```

2. **Reduce test cases during development:**
```python
# Quick smoke test
eval_questions = eval_questions[:3]  # Test first 3 only
eval_answers = eval_answers[:3]
```

3. **Parallel execution:**
```bash
pytest evals/test_evals.py -n auto  # Requires pytest-xdist
```

---

#### 8. Windows Path Issues

**Problem:**
```
FileNotFoundError: .env not found
```

**Solution:**
Use raw strings or forward slashes:
```python
# Good
load_dotenv(".env")
load_dotenv("./env")

# Also good
from pathlib import Path
load_dotenv(Path(".env"))
```

---

### Getting Help

If you're still stuck:

1. **Enable debug mode:**
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

2. **Check versions:**
```bash
pip list | findstr "openai pytest python-dotenv"
```

3. **Minimal reproduction:**
```python
# Create test.py with minimal code
from evaluate import send_to_openai
print(send_to_openai("Say 'hello'"))
```

4. **Review logs:**
- Check pytest output carefully
- Look for stack traces
- Note any warning messages

---

## Evaluation Criteria

The evaluation system uses LLM-based semantic comparison rather than exact string matching:
- **PASS**: Generated answer provides the same information as expected answer
- **FAIL**: Generated answer differs significantly from expected answer

This approach handles variations in phrasing while ensuring content accuracy.

### What Counts as PASS?

✅ **Semantic equivalence:**
- Expected: "The office is open 9 AM to 5 PM"
- Generated: "We're open from 9 to 5"
- Result: **PASS** (same meaning, different wording)

✅ **Additional context:**
- Expected: "Shipping is $5.99"
- Generated: "Shipping costs $5.99 for standard delivery"
- Result: **PASS** (includes core information)

### What Counts as FAIL?

❌ **Missing information:**
- Expected: "Open Monday-Friday, 9 AM to 5 PM"
- Generated: "Open weekdays"
- Result: **FAIL** (missing hours)

❌ **Incorrect facts:**
- Expected: "Founded in 2010"
- Generated: "Founded in 2020"
- Result: **FAIL** (wrong information)

❌ **No answer:**
- Expected: "The product is waterproof"
- Generated: "I don't know"
- Result: **FAIL** (no information provided)

## Development

### Setting Up Development Environment

1. **Clone and setup:**
```bash
git clone <repository-url>
cd Scaling-Enterprise-RAG
python -m venv .venv
.venv\Scripts\activate
pip install -e .  # Editable install
```

2. **Install dev dependencies:**
```bash
pip install pytest pytest-cov black flake8 mypy
```

3. **Run tests:**
```bash
pytest evals/ -v
```

---

### Adding New Test Cases

Edit `evals/test_evals.py` and expand the test data:

```python
eval_questions = [
    # Existing tests
    "What is Underwhelming Spatula?",
    
    # Add new tests here
    "What is your return policy?",
    "How long does shipping take?",
]

eval_answers = [
    # Existing answers
    "Underwhelming Spatula is a kitchen tool...",
    
    # Corresponding answers
    "Items can be returned within 30 days with receipt.",
    "Standard shipping takes 5-7 business days.",
]
```

**Best Practices:**
- Keep questions and answers aligned
- Add comments explaining test purpose
- Test after each addition
- Group related tests together

---

### Switching LLM Providers

Modify the `model_type` variable in `evals/evaluate.py`:

```python
# Line ~18 in evaluate.py
model_type = "openai"  # or "lms" or "qwen"
```

**Provider Comparison:**

| Provider | Cost | Speed | Quality | Setup |
|----------|------|-------|---------|-------|
| OpenAI (GPT-4o) | $$$ | Fast | Excellent | Easy |
| LMStudio (Qwen) | Free | Medium | Good | Moderate |

**When to use each:**
- **OpenAI**: Production, high accuracy needs, have budget
- **LMStudio**: Development, cost-sensitive, offline work

---

### Custom Evaluation Logic

Extend `evaluate_generated_answer()` in `evals/evaluate.py`:

```python
def evaluate_generated_answer(expected_answer, generated_answer, criteria="semantic"):
    """
    Enhanced evaluation with custom criteria
    
    Args:
        expected_answer: The expected answer
        generated_answer: The generated answer
        criteria: "semantic" (default), "exact", or "fuzzy"
    """
    if criteria == "exact":
        return "PASS" if expected_answer == generated_answer else "FAIL"
    
    elif criteria == "fuzzy":
        # Use similarity score
        from difflib import SequenceMatcher
        ratio = SequenceMatcher(None, expected_answer, generated_answer).ratio()
        return "PASS" if ratio > 0.8 else "FAIL"
    
    else:  # semantic
        prompt = (
            f"Evaluate semantic equivalence.\n"
            f"Expected: {expected_answer}\n"
            f"Generated: {generated_answer}\n"
            f"Return PASS if semantically equivalent, else FAIL."
        )
        
        if model_type == "openai":
            return send_to_openai(prompt)
        elif model_type in ["lms", "qwen"]:
            return send_to_lms(prompt)
```

---

### Adding New Model Providers

To add support for a new LLM provider:

1. **Add provider function:**
```python
# In evaluate.py
def send_to_anthropic(message):
    """Send message to Anthropic Claude"""
    import anthropic
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        messages=[{"role": "user", "content": message}]
    )
    
    return response.content[0].text
```

2. **Update evaluation function:**
```python
def evaluate_generated_answer(expected_answer, generated_answer):
    prompt = f"..."
    model_type = "anthropic"  # New option
    
    if model_type == "openai":
        return send_to_openai(prompt)
    elif model_type in ["lms", "qwen"]:
        return send_to_lms(prompt)
    elif model_type == "anthropic":
        return send_to_anthropic(prompt)
    else:
        raise ValueError(f"Unknown model_type: {model_type}")
```

3. **Update environment template:**
```env
# Add to template.env
ANTHROPIC_API_KEY="your-anthropic-key"
```

---

### Code Quality

**Format code:**
```bash
black evals/
```

**Lint code:**
```bash
flake8 evals/ --max-line-length=100
```

**Type checking:**
```bash
mypy evals/ --ignore-missing-imports
```

---

### Testing Your Changes

**Run specific test:**
```bash
pytest evals/test_evals.py::test_run_RAG -v
```

**Run with coverage:**
```bash
pytest evals/ --cov=evals --cov-report=html
```

**View coverage report:**
```bash
# Open htmlcov/index.html in browser
```

---

## CI/CD Integration

### GitHub Actions

Create `.github/workflows/test.yml`:

```yaml
name: RAG Evaluation Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run tests
      env:
        OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
      run: |
        pytest evals/test_evals.py -v
```

**Setup:**
1. Add `OPENAI_API_KEY` to GitHub Secrets
2. Commit workflow file
3. Push to trigger tests

---

### Docker Support

Create `Dockerfile`:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "evals/test_evals.py", "-v"]
```

**Build and run:**
```bash
docker build -t rag-eval .
docker run --env-file .env rag-eval
```

---

## Performance Optimization

### 1. Caching Evaluations

```python
# cache_evaluations.py
import json
from functools import lru_cache

@lru_cache(maxsize=1000)
def cached_evaluate(expected, generated):
    return evaluate_generated_answer(expected, generated)

# Save cache to disk
def save_cache(filepath="eval_cache.json"):
    cache_data = {
        "cache": dict(cached_evaluate.cache_info()),
        "data": dict(cached_evaluate.cache)
    }
    with open(filepath, 'w') as f:
        json.dump(cache_data, f)
```

### 2. Parallel Execution

```python
# parallel_eval.py
from concurrent.futures import ThreadPoolExecutor

def parallel_evaluate(questions, answers):
    results = []
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for q, a in zip(questions, answers):
            generated = run_RAG(q)
            future = executor.submit(evaluate_generated_answer, a, generated)
            futures.append(future)
        
        for future in futures:
            results.append(future.result())
    
    return results
```

### 3. Batch Processing

```python
# batch_eval.py
def evaluate_batch(questions, answers, batch_size=10):
    for i in range(0, len(questions), batch_size):
        batch_q = questions[i:i+batch_size]
        batch_a = answers[i:i+batch_size]
        
        # Process batch
        for q, a in zip(batch_q, batch_a):
            yield evaluate(q, a)
```

---

## Advanced Features

### Custom Metrics

Track additional performance metrics:

```python
# metrics.py
import time
from dataclasses import dataclass
from typing import List

@dataclass
class EvalMetrics:
    question: str
    passed: bool
    response_time: float
    token_count: int
    confidence: float

def evaluate_with_metrics(question, expected) -> EvalMetrics:
    start = time.time()
    
    generated = run_RAG(question)
    result = evaluate_generated_answer(expected, generated)
    
    end = time.time()
    
    return EvalMetrics(
        question=question,
        passed="PASS" in result,
        response_time=end - start,
        token_count=len(generated.split()),
        confidence=extract_confidence(result)
    )

def generate_report(metrics: List[EvalMetrics]):
    avg_time = sum(m.response_time for m in metrics) / len(metrics)
    pass_rate = sum(m.passed for m in metrics) / len(metrics) * 100
    
    print(f"Pass Rate: {pass_rate:.1f}%")
    print(f"Avg Response Time: {avg_time:.2f}s")
```

---

## Roadmap

### v1.1 (Current)
- ✅ OpenAI integration
- ✅ LMStudio integration
- ✅ Basic evaluation framework
- ✅ Pytest integration

### v1.2 (In Progress)
- 🔄 Anthropic Claude support
- 🔄 Confidence scoring
- 🔄 HTML report generation
- 🔄 Batch evaluation API

### v1.3 (Planned)
- 📋 Metrics dashboard
- 📋 A/B testing framework
- 📋 Cost tracking
- 📋 Regression testing

### v2.0 (Future)
- 📋 Web UI for test management
- 📋 Multi-language support
- 📋 RAG pipeline profiling
- 📋 Auto-generated test cases
- 📋 Integration with LangSmith/LangFuse

---

## Contributing

We welcome contributions! Here's how to get started:

### Contribution Guidelines

1. **Fork the repository**
2. **Create a feature branch:**
```bash
git checkout -b feature/your-feature-name
```

3. **Make your changes**
4. **Add tests:**
```python
# test_new_feature.py
def test_your_feature():
    assert your_function() == expected_result
```

5. **Run tests:**
```bash
pytest evals/ -v
black evals/
flake8 evals/
```

6. **Commit with clear message:**
```bash
git commit -m "Add: Feature description"
```

7. **Push and create PR:**
```bash
git push origin feature/your-feature-name
```

### Contribution Ideas

- **New model providers**: Add Anthropic, Cohere, etc.
- **Evaluation metrics**: Implement confidence scoring, similarity metrics
- **Reporting**: Build HTML/PDF report generators
- **Performance**: Optimize evaluation speed
- **Documentation**: Improve examples, tutorials
- **Testing**: Add more test coverage

### Code Standards

- Follow PEP 8 style guide
- Use type hints where possible
- Add docstrings to functions
- Keep functions focused and small
- Write tests for new features

---

## FAQ

### Q: Can I use this for non-English RAG systems?

A: Yes! The framework supports any language that your chosen LLM supports. Just ensure your test questions and answers are in the target language.

### Q: How accurate is LLM-based evaluation?

A: Generally 85-95% accurate for semantic equivalence. For critical applications, consider:
- Human review of edge cases
- Multiple evaluator agreement
- Periodic human audits

### Q: Can I evaluate multiple RAG systems?

A: Yes! Create multiple `run_RAG()` implementations:

```python
def run_RAG_system_a(question):
    # System A implementation
    pass

def run_RAG_system_b(question):
    # System B implementation
    pass

# Compare in tests
for question, expected in zip(eval_questions, eval_answers):
    answer_a = run_RAG_system_a(question)
    answer_b = run_RAG_system_b(question)
    # Evaluate both
```

### Q: How much does evaluation cost?

With OpenAI:
- ~$0.01-0.03 per evaluation (GPT-4)
- 100 evaluations ≈ $1-3
- Use LMStudio for free alternative

### Q: Can I run this offline?

A: Yes, if using LMStudio:
1. Download LMStudio and model while online
2. Set `model_type = "lms"`
3. Run evaluations offline

---

## License

[MIT License / Apache 2.0 / Specify your license here]

---

## Support

- **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-repo/discussions)
- **Email**: support@your-domain.com

---

## Acknowledgments

- OpenAI for GPT-4 API
- LMStudio for local model support
- Qwen team for the Qwen models
- pytest community for testing framework

---

## Citation

If you use this framework in research, please cite:

```bibtex
@software{enterprise_rag_eval,
  title = {Enterprise RAG Evaluation Framework},
  author = {Your Name},
  year = {2024},
  url = {https://github.com/your-repo}
}
```

---

**Built with ❤️ for the RAG community**