import re

def analyze_logs(logs: str) -> str:
    """
    Simple mock AI analyzer.
    Detects common pytest failures and returns explanation.
    """

    if "ZeroDivisionError" in logs:
        return """
Root Cause:
Division by zero detected.

Suggested Fix:
Ensure denominator is validated before division.
Example:
    if b == 0:
        raise ValueError("Cannot divide by zero")
"""

    if "AssertionError" in logs:
        return """
Root Cause:
A test assertion failed. The expected value does not match the actual output.

Suggested Fix:
Review the function logic and ensure it returns expected result.
"""

    if "ModuleNotFoundError" in logs:
        return """
Root Cause:
Python cannot find the specified module.

Suggested Fix:
Check import paths and ensure package structure is correct.
"""

    return """
Root Cause:
Generic test failure.

Suggested Fix:
Review test output logs and validate recent code changes.
"""


# Read CI test output
try:
    with open("test_output.txt", "r") as f:
        logs = f.read()
except FileNotFoundError:
    logs = "No logs found."

analysis = analyze_logs(logs)

print("==== MOCK AI ANALYSIS ====")
print(analysis)

# Save output (optional)
with open("analysis.txt", "w") as f:
    f.write(analysis)
