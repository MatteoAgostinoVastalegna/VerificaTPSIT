class main:
    impianti: list[ImpiantoSolare] = []
    def registra_impianto(impianti: list[ImpiantoSolare], impianto: ImpiantoSolare) -> None:
        impianti.append(impianto)
    
    def cerca_impianto(impianti: list[ImpiantoSolare], codice: str)-> ImpiantoSolare:
        for i in impianti:
            if codice == i.codice:
                return i
        

    def riepilogo_impianti(nome_azienda: str, impianti: list[ImpiantoSolare]) -> None:
        for i in impianti:
            print(i.codice + " - " + i.modello + " - " + i.stato + " - " + i.potenza_kw)

