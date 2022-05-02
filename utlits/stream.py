
class Stream:
    def __init__(self, path: str) -> None:
        self.path = path
    
    def make_stream(self) -> None:
        with open(self.path, "rb") as fwav:
            data = fwav.read(1024)
            while True:
                data = fwav.read(1024)
                yield data

