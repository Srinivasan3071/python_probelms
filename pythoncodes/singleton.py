class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            print(f"First instance created: {cls._instance}")
        return cls._instance

# Usage
s1 = Singleton()  # This will create the first instance and print it
s2 = Singleton()  # This will not print anything since the instance already exists
