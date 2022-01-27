import click

from dice import roll_advantage
from dice import roll_array
from dice import roll_crit
from dice import roll_disadvantage
from dice import roll_string


@click.command()
@click.argument("diestring")
@click.option("--rolltype", 
              type=click.Choice(
                  ["standard", "critical", "advantage", "disadvantage", "array"], 
                  case_sensitive=False), default="standard"
                  )
def cli(diestring, rolltype) -> None:
    """Echo roll of diestring based on rolltype.
    
    Args:
        diestring (str): String of dice to be rolled
        rolltype (str): String of roll type from 'advantage', 'array',
        'critical', 'disadvantage' and the default 'standard'."""
    if rolltype == "critical":
        click.echo(f"Rolled: {diestring}\nResult: {roll_crit(diestring)}")
    elif rolltype == "advantage":
        click.echo(f"Rolled: {diestring}\nResult: {roll_advantage(diestring)}")
    elif rolltype == "disadvantage":
        click.echo(f"Rolled: {diestring}\nResult: {roll_disadvantage(diestring)}")
    elif rolltype == "array":
        click.echo(f"Rolled: {diestring}\nResult: {roll_array(diestring)}")
    else:
        click.echo(f"Rolled: {diestring}\nResult: {roll_string(diestring)}")


if __name__ == "__main__":
    cli()