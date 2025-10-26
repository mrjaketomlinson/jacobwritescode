def load_csv(file_path):
    return 'csv file'

def load_json(file_path):
    return 'json file'

def load_parquet(file_path):
    return 'parquet file'

def load_data(file_path, file_type):
    if file_type == "csv":
        return load_csv(file_path)
    elif file_type == "json":
        return load_json(file_path)
    elif file_type == "parquet":
        return load_parquet(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")