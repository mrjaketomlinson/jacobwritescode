from dataclasses import dataclass


@dataclass
class PipelineContext:
    data_path: str
    logger: object
    metrics: object
    user_id: str
    run_id: str
    retry_count: int
    alert_email: str
    db_client: object
    region: str
    is_test_run: bool


def extract_data(context: PipelineContext):
    context.logger.info(f"Extracting for user {context.user_id}")
    return context.db_client.read(context.data_path)


def transform_data(context: PipelineContext, data):
    context.metrics.increment("transform.start")
    return [row for row in data if row["region"] == context.region]


def load_data(context: PipelineContext, data):
    context.logger.info(f"Loading {len(data)} rows")
    context.db_client.write("output", data)


def run_pipeline(context: PipelineContext):
    context.logger.info("Pipeline starting")
    context.metrics.increment("pipeline.start")

    data = extract_data(context)
    transformed = transform_data(context, data)
    load_data(context, transformed)
