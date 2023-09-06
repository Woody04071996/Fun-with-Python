def __init__(self, pAutor, pOdczyt):      # Konstruktor
              self._dataczas = str (datetime.datetime.now() )[0:19]  # Wynik będzie podobny do: 2021-04-20 13:51:27
              self._autor=pAutor
              if math.fabs(pOdczyt) <= Pomiar.LimitNapiecia:
                     self._odczyt = pOdczyt
              else:
                     raise Exception("Odczyt nie może przekroczyć wartości " + \
                                     str(Pomiar.LimitNapiecia) + "V")
              Pomiar.Licznik+=1    # Inkrementacja
