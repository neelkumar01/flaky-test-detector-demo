import random
import time


# -------------------------
# Stable tests
# -------------------------

def test_addition():
    assert 2 + 2 == 4


def test_string_formatting():
    assert "flake".upper() == "FLAKE"


def test_list_length():
    assert len([1, 2, 3]) == 3


# -------------------------
# Flaky: randomness
# -------------------------

def test_random_failure():
    value = random.random()

    assert value > 0.30, (
        f"random value {value:.2f} was below threshold"
    )


# -------------------------
# Flaky: timing
# -------------------------

def test_timing_sensitive_operation():
    delay = random.uniform(0.01, 0.08)

    start = time.time()
    time.sleep(delay)
    elapsed = time.time() - start

    assert elapsed < 0.06, (
        f"operation took {elapsed:.3f}s, "
        "expected under 0.060s"
    )


# -------------------------
# Flaky: resource availability
# -------------------------

def test_temporary_resource():
    available = random.random() > 0.20

    assert available, (
        "temporary resource was unavailable"
    )


# -------------------------
# Flaky: simulated network
# -------------------------

def test_network_request():
    request_succeeded = random.random() > 0.25

    assert request_succeeded, (
        "connection reset while contacting service"
    )