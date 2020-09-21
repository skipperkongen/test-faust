import faust

class Greeting(faust.Record):
    from_name: str
    to_name: str
