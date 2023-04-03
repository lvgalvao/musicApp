from typer import Argument, run
from escalas import escala
from rich import print
from rich.table import Table
from rich.console import Console


def escalas(tonica=Argument('c'), tonalidade=Argument('maior')):
    table = Table()
    console = Console()
    notas, graus = escala(tonica, tonalidade).values()

    for grau in graus:
        table.add_column(grau)

    table.add_row(*notas)
    console.print(table)


run(escalas)
