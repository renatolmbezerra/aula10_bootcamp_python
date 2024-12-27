import pandas as pd



class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)


    def filtrar_por(self, coluna, atributo):
        return self.df[self.df[coluna] == atributo]
    

    
arquivo_csv = './exemplo.csv'
coluna = 'estado'
atributo = 'SP'

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()
print(arquivo_CSV.filtrar_por(coluna,atributo))



