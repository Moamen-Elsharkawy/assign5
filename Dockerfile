FROM python:3.10-slim

ARG RUN_ID

WORKDIR /app

RUN echo "Preparing container..."
RUN echo "Downloading model for RUN_ID=${RUN_ID}"

CMD ["sh", "-c", "echo Container started for model run: ${RUN_ID}"]