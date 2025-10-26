class DataLoader:
    def load_data(self, file_path, **kwargs):
        raise NotImplementedError("Subclasses should implement this method")


class CsvDataLoader(DataLoader):
    def load_data(self, file_path, **kwargs):
        return f"csv @ {file_path}"


class JsonDataLoader(DataLoader):
    def load_data(self, file_path, **kwargs):
        return f"json @ {file_path}"


class ParquetDataLoader(DataLoader):
    def load_data(self, file_path, **kwargs):
        return f"parquet @ {file_path}"


class DataLoaderFactory:
    def __init__(self):
         self._formats = {}

    def register_format(self, format, creator):
         self._formats[format] = creator

    def create_data_loader(self, file_type):
        creator = self._formats.get(file_type.upper())
        if not creator:
            raise ValueError(f"{file_type} is unsupported")
        return creator()


factory = DataLoaderFactory()
factory.register_format('CSV', CsvDataLoader)
factory.register_format('JSON', JsonDataLoader)
factory.register_format('PARQUET', ParquetDataLoader)


if __name__ == "__main__":
    loader = factory.create_data_loader("CSV")
    data = loader.load_data("/path/to/file.csv")

    print(data)