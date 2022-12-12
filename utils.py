
class Wrapper:
    """
        Wrapper is intended to be used when passing elements for reference between differents methods
    """
    reference_stack = {
        "anonymous": []
    }
    def __init__(self, *args, **kwargs):
        for arg in args:
            self.reference_stack["anonymous"] += arg
        for arg in kwargs:
            self.reference_stack[arg] = kwargs[arg]
    
    def anon_push(self, element):
        self.reference_stack["anonymous"].insert(0, element)
    
    def anon_append(self, element):
        self.reference_stack["anonymous"].append(element)