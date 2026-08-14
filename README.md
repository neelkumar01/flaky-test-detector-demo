### FlakeLens Testing

A small controlled test repository for validating [FlakeLens](https://github.com/neelkumar01/flakeLens) an AI assisted flaky test detection tool for CI pipelines

### Purpose

This repository provides a predictable environment for testing whether `FlakeLens` can:

- Distinguish flaky tests from stable tests
- Detect inconsistent pass / fail behavior across CI runs
- Consume JUnit test results
- Fall back to GitHub Actions logs when structured results are unavailable
- Provide useful failure evidence for AI assisted analysis

### Test Suite

The repository contains a small pytest suite with 7 tests:

- 3 stable tests that should consistently pass
- 4 intentionally flaky tests that simulate common sources of nondeterministic failures:
  - Randomness
  - Timing sensitivity
  - Temporary resource availability
  - Network failures

The flaky behavior is intentionally introduced so that the expected results are known before running `FlakeLens`

### CI Setup

Tests run through GitHub Actions using Python and pytest

Each CI run produces test output that can be analyzed in two ways:

- JUnit XML - structured test results are generated and uploaded as a workflow artifact
- CI logs — FlakeLens can parse GitHub Actions logs as a fallback when the JUnit artifact is unavailable

This allows both ingestion paths supported by FlakeLens to be tested using the same repository

[View all CI workflow runs](https://github.com/neelkumar01/flakeLens-testing/actions)

- First 15 runs: JUnit XML artifacts were generated 
- Next 10 runs: JUnit artifact upload was disabled to validate FlakeLens GitHub Actions log parsing fallback
