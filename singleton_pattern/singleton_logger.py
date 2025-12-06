class SingletonLogger:
    """
    Ensures only one instance of the Logger exists and controls
    access to the single, shared file handle.
    """

    # 1. Class attribute to hold the single instance
    _instance = None
    _is_initialized = False  # Flag to control one-time initialization

    def __new__(cls, log_filename="app_test.log"):
        # This is the core logic of the Singleton pattern
        if cls._instance is None:
            # Create the *one and only* instance
            print("SingletonLogger: Creating the one and only instance.")
            cls._instance = super().__new__(cls)

            # Initialization (handled separately below)
            cls._instance._initialize(log_filename)

        # Always return the same instance
        return cls._instance

    def _initialize(self, log_filename):
        """Initializes the resource (file handle) only once."""
        if not self._is_initialized:
            try:
                # Open the file handle ONCE
                self.log_file = open(log_filename, "a")
                print(
                    f"SingletonLogger: Opened SHARED file handle: {id(self.log_file)}"
                )
                self._is_initialized = True
            except IOError as e:
                print(f"Error opening log file: {e}")

    def log(self, message):
        """Writes the message using the shared file handle."""
        import datetime

        if self._is_initialized:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            log_entry = f"[{timestamp}] {message}\n"
            self.log_file.write(log_entry)
            self.log_file.flush()

    def close(self):
        """Closes the shared file handle."""
        if self._is_initialized:
            self.log_file.close()
            print(f"SingletonLogger: Closed SHARED file handle: {id(self.log_file)}")
            # Reset for potential application restart/testing
            SingletonLogger._instance = None
            SingletonLogger._is_initialized = False


if __name__ == "__main__":

    print("--- Step 1: Creating log1 ---")
    # 1. The instance is created, and the file handle is opened.
    log1 = SingletonLogger()
    log1.log("Application started successfully.")

    print("\n--- Step 2: Creating log2 ---")
    # 2. The __new__ method detects an existing instance and returns it.
    log2 = SingletonLogger()
    log2.log("Critical operation completed.")

    print("\n--- Step 3: Verification ---")
    # log1 and log2 are the exact same object in memory
    print(f"Are log1 and log2 the same object? **{log1 is log2}**")

    # They share the exact same file handle ID
    print(f"Handle 1 ID: {id(log1.log_file)}")
    print(f"Handle 2 ID: {id(log2.log_file)}")
    # The IDs will be IDENTICAL, proving only one OS resource was allocated.

    # 3. Cleanup:
    # Closing it through either variable closes the single shared handle.
    log1.close()
    # log2.close() is unnecessary and would fail since the handle is already closed.
