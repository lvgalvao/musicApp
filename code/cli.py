from typer import Argument, run
from rich import print
from rich.table import Table
from rich.console import Console

from code.escalas import escala



def escalas(tonica=Argument('c'), tonalidade=Argument('maior')):
    table = Table()
    console = Console()
    notas, graus = escala(tonica, tonalidade).values()

    for grau in graus:
        table.add_column(grau)

    table.add_row(*notas)
    console.print(table)

if __name__ == '__main__':
    run(escalas)
