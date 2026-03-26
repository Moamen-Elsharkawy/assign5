import sys

THRESHOLD = 0.85

with open("model_info.txt", "r") as f:
    lines = f.read().strip().splitlines()

run_id = lines[0].strip()
accuracy = float(lines[1].strip())

print("Run ID:", run_id)
print("Accuracy:", accuracy)
print("Threshold:", THRESHOLD)

if accuracy < THRESHOLD:
    print("Model accuracy is below threshold. Deployment failed.")
    sys.exit(1)

print("Model passed threshold. Deployment can continue.")