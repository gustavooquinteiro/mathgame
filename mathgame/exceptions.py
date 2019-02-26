class InsufficientLevel(Exception):
    def __init__(self, args="Incapable of do that. Level too small"):
        self.args = args
        
