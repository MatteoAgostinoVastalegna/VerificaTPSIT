class ImpiantoSolare:
    def __init__(self, codice: str, modello: str, localita: str, potenza_massima_kw: float, stato: str) -> None:
        self.codice = codice
        self.modello = modello
        self.localita = localita
        self.potenza_massima_kw = potenza_massima_kw
        self.stato = stato
    pannelli: list[PannelloFotovoltaico] = []
    def aggiungi_pannello(pannello: PannelloFotovoltaico):
        pannelli.append(pannello)
        
    def potenza_pannelli() -> None:
        somma: int = 0
        for i in pannelli:
            somma += i.potenza_kw
        return somma
    
    def cerca_pannello(codice: str) -> float:
        for i in pannelli:
            if codice == i.codice:
                return i
        return None
    
    def rimuovi_pannello(codice: str) -> PannelloFotovoltaico:
        for i in pannelli:
            if codice == i.codice:
                pannelli.remove(i)
                return i
        return None

    def pannelli_sotto_potenza(potenza_massima: float) -> list[PannelloFotovoltaico]:
        psp: list[PannelloFotovoltaico] = []
        for i in pannelli:
            if i.potenza_kw < potenza_massima:
                psp.append(i)
        return psp