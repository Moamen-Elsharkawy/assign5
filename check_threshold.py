import sys
import mlflow

THRESHOLD = 0.85

with open("model_info.txt", "r") as f:
    run_id = f.read().strip()

client = mlflow.tracking.MlflowClient()
run = client.get_run(run_id)

accuracy = run.data.metrics.get("accuracy")

if accuracy is None:
    print("ERROR: accuracy metric not found.")
    sys.exit(1)

print("Run ID:", run_id)
print("Accuracy:", accuracy)
print("Threshold:", THRESHOLD)

if accuracy < THRESHOLD:
    print("Model accuracy is below threshold. Deployment failed.")
    sys.exit(1)

print("Model passed threshold. Deployment can continue.")