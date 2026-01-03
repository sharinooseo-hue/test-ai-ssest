import pandas as pd

# Load historical test execution data (simulated CI logs)
df = pd.read_csv("data/test_history.csv")

# Simple and explainable risk scoring model
df["RiskScore"] = (
    0.4 * df["PastFail"] +
    0.3 * df["RecentFail"] +
    0.2 * df["FilesChanged"] +
    0.1 * df["CodeChurn"]
)

# Sort tests by descending risk
df = df.sort_values("RiskScore", ascending=False)

print("\n=== AI-Assisted Regression Test Prioritization ===\n")
print(df[["TestName", "RiskScore"]])
print("\nNote: This output supports human decision-making. Final execution choice remains manual.\n")
