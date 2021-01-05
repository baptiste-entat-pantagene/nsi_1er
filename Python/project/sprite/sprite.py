class sprite:
    """
    class de base des sprites
    """

    def __init__(self) -> None:
        super().__init__()
        self._name:str = "" 
        self._graph = (("OIOIO"), ("OOOOO"), ("IOOOI"), ("OIIIO"), ("OOOOO"))