def extract_data(
    data_path,
    logger,
    metrics,
    user_id,
    run_id,
    retry_count,
    alert_email,
    db_client,
    region,
    is_test_run,
): ...


def transform_data(
    data,
    logger,
    metrics,
    user_id,
    run_id,
    retry_count,
    alert_email,
    db_client,
    region,
    is_test_run,
): ...


def load_data(
    data,
    logger,
    metrics,
    user_id,
    run_id,
    retry_count,
    alert_email,
    db_client,
    region,
    is_test_run,
): ...


def run_pipeline(
    data_path,
    logger,
    metrics,
    user_id,
    run_id,
    retry_count,
    alert_email,
    db_client,
    region,
    is_test_run,
):
    logger.info(f"Running pipeline for {user_id} in {region}")
    metrics.increment("pipeline.start")

    data = extract_data(
        data_path,
        logger,
        metrics,
        user_id,
        run_id,
        retry_count,
        alert_email,
        db_client,
        region,
        is_test_run,
    )

    transformed = transform_data(
        data,
        logger,
        metrics,
        user_id,
        run_id,
        retry_count,
        alert_email,
        db_client,
        region,
        is_test_run,
    )

    load_data(
        transformed,
        logger,
        metrics,
        user_id,
        run_id,
        retry_count,
        alert_email,
        db_client,
        region,
        is_test_run,
    )
