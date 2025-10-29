# Contributing to Enterprise RAG Evaluation Framework

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Submitting Changes](#submitting-changes)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what's best for the community
- Show empathy towards other contributors

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- Basic understanding of RAG systems and LLMs

### Find an Issue
- Check [Issues](https://github.com/your-repo/issues) for open tasks
- Look for issues labeled `good first issue` or `help wanted`
- Comment on the issue to let others know you're working on it

## Development Setup

1. **Fork and clone the repository:**
```bash
git clone https://github.com/YOUR-USERNAME/Scaling-Enterprise-RAG.git
cd Scaling-Enterprise-RAG
```

2. **Create a virtual environment:**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# OR
source .venv/bin/activate  # Linux/macOS
```

3. **Install development dependencies:**
```bash
pip install -r requirements-dev.txt
```

4. **Set up pre-commit hooks (optional):**
```bash
pip install pre-commit
pre-commit install
```

5. **Configure environment:**
```bash
copy template.env .env  # Windows
# OR
cp template.env .env    # Linux/macOS

# Add your API keys to .env
```

6. **Verify installation:**
```bash
pytest evals/ -v
```

## Making Changes

### Create a Branch

Always create a new branch for your changes:

```bash
git checkout -b feature/your-feature-name
# OR
git checkout -b fix/bug-description
# OR
git checkout -b docs/documentation-update
```

Branch naming conventions:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Test additions or improvements

### Code Style

Follow these guidelines:

1. **Format with Black:**
```bash
black evals/
```

2. **Sort imports with isort:**
```bash
isort evals/
```

3. **Lint with Flake8:**
```bash
flake8 evals/ --max-line-length=100
```

4. **Type check with mypy:**
```bash
mypy evals/ --ignore-missing-imports
```

### Code Structure

- Keep functions focused and single-purpose
- Use descriptive variable and function names
- Add docstrings to all functions
- Use type hints where possible

**Example:**

```python
def evaluate_generated_answer(
    expected_answer: str, 
    generated_answer: str
) -> str:
    """
    Evaluates a generated answer against an expected answer.
    
    Args:
        expected_answer: The correct answer from knowledge base
        generated_answer: The answer produced by RAG system
        
    Returns:
        String containing "PASS" if semantically equivalent, else "FAIL"
        
    Raises:
        ValueError: If model_type is not recognized
    """
    # Implementation
    pass
```

## Submitting Changes

### Before Submitting

1. **Run all tests:**
```bash
pytest evals/ -v
```

2. **Check code quality:**
```bash
black evals/ --check
flake8 evals/
mypy evals/
```

3. **Update documentation:**
- Update README.md if adding new features
- Add docstrings to new functions
- Update API documentation if needed

4. **Test your changes:**
```bash
# Run specific tests
pytest evals/test_your_feature.py -v

# Run with coverage
pytest evals/ --cov=evals --cov-report=html
```

### Commit Messages

Write clear, descriptive commit messages:

```bash
# Good commit messages
git commit -m "Add: Support for Anthropic Claude evaluation"
git commit -m "Fix: OpenAI API authentication error handling"
git commit -m "Docs: Update installation instructions for Windows"
git commit -m "Refactor: Extract evaluation logic into separate module"

# Bad commit messages (avoid these)
git commit -m "fixed stuff"
git commit -m "updates"
git commit -m "WIP"
```

Format:
```
<type>: <description>

[optional body]
[optional footer]
```

Types:
- `Add:` - New feature
- `Fix:` - Bug fix
- `Docs:` - Documentation changes
- `Refactor:` - Code refactoring
- `Test:` - Adding or updating tests
- `Chore:` - Maintenance tasks

### Create Pull Request

1. **Push your branch:**
```bash
git push origin feature/your-feature-name
```

2. **Create PR on GitHub:**
- Go to the repository
- Click "New Pull Request"
- Select your branch
- Fill in the PR template

3. **PR Description should include:**
- What changes were made
- Why the changes were needed
- How to test the changes
- Screenshots (if applicable)
- Related issue numbers

**Example PR description:**

```markdown
## Description
Adds support for Anthropic Claude as an evaluation model.

## Changes
- Added `send_to_anthropic()` function in `evaluate.py`
- Updated `evaluate_generated_answer()` to support Claude
- Added environment variable `ANTHROPIC_API_KEY`
- Updated documentation with Claude setup instructions

## Testing
- Tested with Claude Opus and Sonnet models
- All existing tests pass
- Added new tests in `test_anthropic.py`

## Related Issues
Closes #42
```

4. **Respond to review feedback:**
- Address all comments
- Make requested changes
- Re-request review when ready

## Coding Standards

### Python Style Guide

Follow [PEP 8](https://pep8.org/) with these specifics:

- Line length: 100 characters (not 79)
- Use double quotes for strings
- 4 spaces for indentation (no tabs)
- Blank line between functions
- Two blank lines between classes

### Documentation

- Add docstrings to all public functions
- Use Google-style docstrings
- Include type hints in function signatures
- Document exceptions that can be raised

**Example:**

```python
def evaluate_batch(
    questions: list[str],
    answers: list[str],
    batch_size: int = 10
) -> list[str]:
    """
    Evaluates multiple questions in batches.
    
    Args:
        questions: List of questions to evaluate
        answers: List of expected answers
        batch_size: Number of questions per batch (default: 10)
        
    Returns:
        List of evaluation results ("PASS" or "FAIL")
        
    Raises:
        ValueError: If questions and answers have different lengths
        
    Example:
        >>> results = evaluate_batch(
        ...     ["What is X?", "What is Y?"],
        ...     ["X is...", "Y is..."]
        ... )
        >>> print(results)
        ['PASS', 'PASS']
    """
    if len(questions) != len(answers):
        raise ValueError("Questions and answers must have same length")
    # Implementation
```

## Testing Guidelines

### Writing Tests

1. **Test file naming:**
```
test_<module_name>.py
```

2. **Test function naming:**
```python
def test_<what_is_being_tested>():
    """Test description"""
    pass
```

3. **Test structure (AAA pattern):**
```python
def test_evaluate_returns_pass():
    """Test that identical answers return PASS"""
    # Arrange
    expected = "The sky is blue"
    generated = "The sky is blue"
    
    # Act
    result = evaluate_generated_answer(expected, generated)
    
    # Assert
    assert "PASS" in result
```

4. **Use fixtures for common setup:**
```python
import pytest

@pytest.fixture
def sample_questions():
    return ["What is X?", "What is Y?"]

@pytest.fixture
def sample_answers():
    return ["X is...", "Y is..."]

def test_with_fixtures(sample_questions, sample_answers):
    # Use fixtures
    assert len(sample_questions) == len(sample_answers)
```

### Running Tests

```bash
# Run all tests
pytest evals/

# Run specific test file
pytest evals/test_evaluate.py

# Run specific test
pytest evals/test_evaluate.py::test_specific_function

# Run with verbose output
pytest evals/ -v

# Run with coverage
pytest evals/ --cov=evals

# Run only failed tests
pytest evals/ --lf

# Stop on first failure
pytest evals/ -x
```

## Pull Request Review Process

### Review Checklist

Reviewers will check:
- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] New features have tests
- [ ] Documentation is updated
- [ ] No breaking changes (or properly documented)
- [ ] Commit messages are clear
- [ ] PR description is complete

### Response Time

- Initial review: within 48 hours
- Follow-up reviews: within 24 hours
- PRs may require multiple review rounds

### Getting Help

If you need help during review:
- Comment on the PR with specific questions
- Tag relevant maintainers
- Join discussions in GitHub Discussions

## Types of Contributions

### Code Contributions

- New features
- Bug fixes
- Performance improvements
- Code refactoring

### Non-Code Contributions

- Documentation improvements
- Tutorial creation
- Bug reports
- Feature requests
- Code reviews
- Answering questions in Discussions

All contributions are valued equally!

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Acknowledged in relevant documentation

## Questions?

- Check [FAQ in README](README.md#faq)
- Open a [Discussion](https://github.com/your-repo/discussions)
- Email: maintainers@your-domain.com

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing to Enterprise RAG Evaluation Framework! 🎉
