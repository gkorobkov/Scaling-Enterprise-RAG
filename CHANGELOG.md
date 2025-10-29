# Changelog

All notable changes to the Enterprise RAG Evaluation Framework will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Anthropic Claude evaluation support
- Confidence scoring for evaluations
- HTML report generation
- Metrics dashboard
- A/B testing framework
- Cost tracking per evaluation

## [1.1.0] - 2025-10-29

### Added
- Comprehensive README with full API documentation
- Quick Start guide for new users
- Detailed troubleshooting section
- Usage examples for common scenarios
- CI/CD integration examples (GitHub Actions, Docker)
- Performance optimization strategies
- Contributing guidelines (CONTRIBUTING.md)
- Development requirements file (requirements-dev.txt)
- Changelog file
- FAQ section

### Changed
- Enhanced requirements.txt with detailed comments
- Improved code documentation with type hints
- Updated test output formatting for better readability

### Documentation
- Added API reference for all core functions
- Included LangChain integration examples
- Added Pinecone RAG example
- Documented environment variables
- Created testing best practices section

## [1.0.0] - 2025-10-28

### Added
- Initial release of Enterprise RAG Evaluation Framework
- OpenAI GPT-4o integration for evaluation
- LMStudio integration for local model evaluation
- Support for Qwen3-4B-2507 model
- Core evaluation function with semantic comparison
- Pytest integration for test execution
- Three test execution methods (pytest, standalone, verbose)
- Sample test dataset with 3 example questions
- Environment variable configuration via .env
- Template environment file (template.env)
- Basic error handling and logging

### Core Features
- `evaluate_generated_answer()` - Main evaluation function
- `send_to_openai()` - OpenAI API integration
- `send_to_lms()` - LMStudio integration
- `run_RAG()` - RAG system integration point
- `test_run_RAG()` - Main test function

### Testing
- Pytest-based test framework
- Standalone test runner (run_test.py)
- Detailed evaluation output with questions, answers, and results
- Assertion-based pass/fail evaluation

### Configuration
- Environment variable support for API keys
- Configurable model selection (OpenAI vs LMStudio)
- Template configuration file

---

## Version History

### Version Numbering
- **Major** (X.0.0): Breaking changes
- **Minor** (1.X.0): New features, backwards compatible
- **Patch** (1.0.X): Bug fixes, backwards compatible

### Release Schedule
- Major releases: As needed for breaking changes
- Minor releases: Monthly or when significant features are added
- Patch releases: As needed for bug fixes

---

## Migration Guides

### Migrating from 1.0.0 to 1.1.0

No breaking changes. All 1.0.0 code will work with 1.1.0.

**New features to adopt:**
1. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

2. Use new examples from README for your RAG integration

3. Optionally set up CI/CD using provided templates

---

## Deprecation Notices

None currently.

---

## Known Issues

### v1.1.0
- LMStudio connection may be slow on first model load
- Large evaluation batches (>100 questions) may hit API rate limits
- Windows path handling in some edge cases

### Workarounds
- Pre-load LMStudio models before running tests
- Use batch processing with delays between API calls
- Use forward slashes in paths or raw strings

---

## Upgrade Instructions

### From 1.0.0 to 1.1.0

```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# No code changes needed
```

---

## Contributors

Thank you to all contributors who helped with this release!

### v1.1.0
- Comprehensive documentation improvements
- Example additions
- Testing best practices

### v1.0.0
- Initial framework development
- Core evaluation logic
- OpenAI and LMStudio integrations

---

## Feedback

Have feedback on these changes? Please:
- Open an issue: https://github.com/your-repo/issues
- Start a discussion: https://github.com/your-repo/discussions
- Email us: feedback@your-domain.com

---

**Note:** This project is actively maintained. Check back for updates!
