class BadLogger:
    """
    Simulates a logger without Singleton pattern.
    Each instance opens a new, independent file handle.
    """

    def __init__(self, log_filename="app_test.log"):
        # This happens every time an object is created!
        self.log_file = open(log_filename, "a")
        print(f"BadLogger: Opened NEW file handle: {id(self.log_file)}")
        self.log_filename = log_filename

    def log(self, message):
        import datetime

        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        self.log_file.write(log_entry)
        self.log_file.flush()

    def close(self):
        # We must manually close each redundant handle
        self.log_file.close()
        print(f"BadLogger: Closed file handle: {id(self.log_file)}")


if __name__ == "__main__":
    # 1. Create the first logger instance
    log_a = BadLogger()
    log_a.log("Operation A started.")

    # 2. Create the second logger instance
    # This opens a *second* file handle for the same file.
    log_b = BadLogger()
    log_b.log("Operation B completed.")

    print(f"\nAre log_a and log_b the same object? {log_a is log_b}")  # False

    # Check the file handles in memory:
    print(f"Handle A ID: {id(log_a.log_file)}")
    print(f"Handle B ID: {id(log_b.log_file)}")
    # The IDs will be DIFFERENT, meaning two separate OS resources were allocated.

    # 3. Cleanup:
    # You must remember to close both redundant handles, which adds complexity.
    log_a.close()
    log_b.close()
