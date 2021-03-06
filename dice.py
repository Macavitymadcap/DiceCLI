"""A package of functions for rolling dice implented as a CLI.

The module contains functions that replicate rolling polyhedral dice with any
number of faces and rolling them in different ways; as an array, at advantage;
as a critical hit; at disadvantage and rolling an array of 6 ability scores.

This is acheived with the parse_die_string function, which takes a string and 
returns a dictionary of all the elements of a die string (number of dice,
die type, symbol & modifier) used by other functions to roll dice.

The cli function packages all of the above into an installable command line 
interface called 'dice', implementing the various types of rolls through the 
--rolltype option."""

from copy import deepcopy
from random import randint
import re
from typing import Dict
from typing import Union

import click


def roll_d(num: int) -> int:
    """Return a random number between 1 and num.

    Args:
        num (int): An int for the number of faces on the die

    Returns:
        roll (int): Int of the the number rolled."""
    return randint(1, num)


def roll_mult(num: int, die: str) -> int:
    """Return a die or dice rolled a number of times.

    Args:
        num (int): The number of dice to roll
        die (string): A string representing a die
    
    Attributes:
        roll_total (int): An int for the total of all dice rolled
        faces (int): An int of the number of faces on the die

    Returns:
        roll_total: The combined total of all dice rolls."""
    roll_total = 0
    faces = int(die.replace("d", ""))

    for i in range(num):
        roll_total += roll_d(faces)

    return roll_total


def parse_die_string(string: str) -> Dict[str, Union[str, int]]:
    """Returns a dict of the constituents of a die roll from a given string.
    
    Args:
        string (str): A string representing a die roll
    
    Returns:
        parsed_roll: A dictionary of the roll string's elements."""
    # regex patterns to search for in string
    num_dice_regex = r"\d+\s*[d|D]"
    die_regex = r"[D|d]\d+"
    symbol_regex = r"[+|-|x|X|*|/|??]"
    symbol_modifier_regex = r"\s*[+|-|x|X|*|/|??]\s*\d+"

    # Set elements as their values or as defaults if none found in string
    try:
        num_dice = int(
            re.search(num_dice_regex, string).group().replace("d", "").strip()
            )
    except AttributeError:
        num_dice = 1

    die = re.search(die_regex, string).group().strip().lower()

    try:
        symbol = re.search(symbol_regex, string).group().strip()
    except AttributeError:
        symbol = "+"

    try:
        modifier = int(
            re.search(symbol_modifier_regex, string).group().replace(symbol, "").strip()
            )
    except AttributeError:
        modifier = 0
    
    parsed_roll = {
        "num dice": num_dice,
        "die": die,
        "operator": symbol,
        "modifier": modifier
    }

    return parsed_roll


def roll_string(string: str) -> int:
    """Return an int of a roll for a number of given dice with modifiers.

    Args:
        string (str): A string of a roll of dice with modifiers

    Attributes:
        parsed_string (dict): A dictionary of the roll elements in the string
        num_dice (int): Int of the number of dice to be rolled, default 1
        die (str): String of type of die to be rolled
        symbol (str): String of operator to be appled, default +
        modifier (int): An int to be applied to roll with operator, default 0

    Returns:
        roll: A int returned from a call to the roll_mult function."""
    parsed_string = parse_die_string(string)
    num_dice = parsed_string["num dice"]
    die = parsed_string["die"]
    symbol = parsed_string["operator"]
    modifier = parsed_string["modifier"]

    if symbol == "-":
        return roll_mult(num_dice, die) - modifier

    elif symbol == "x" or symbol == "X" or symbol == "*":
        return roll_mult(num_dice, die) * modifier

    elif symbol == "/" or symbol == "??" :
        return roll_mult(num_dice, die) / modifier

    else:
        return roll_mult(num_dice, die) + modifier


def roll_crit(string: str) -> int:
    """Return an int of a roll with doubled dice and modifiers applied.

    Args:
        string (str): A string of a roll of dice with modifiers

    Attributes:
        parsed_string (dict): A dictionary of the roll elements in the string
        num_dice (int): Int of the number of dice to be rolled, default 1
        die (str): String of type of die to be rolled
        symbol (str): String of operator to be appled, default +
        modifier (int): An int to be applied to roll with operator, default 0

    Returns:
        roll: A int returned from a call to the roll_mult function."""
    parsed_string = parse_die_string(string)
    num_dice = parsed_string["num dice"]
    die = parsed_string["die"]
    symbol = parsed_string["operator"]
    modifier = parsed_string["modifier"]

    if symbol == "-":
        return (roll_mult(num_dice, die) + roll_mult(num_dice, die)) - modifier

    elif symbol == "x" or symbol == "X" or symbol == "*":
        return (roll_mult(num_dice, die) + roll_mult(num_dice, die)) * modifier

    elif symbol == "/" or symbol == "??" :
        return (roll_mult(num_dice, die) + roll_mult(num_dice, die)) / modifier

    else:
        return (roll_mult(num_dice, die) + roll_mult(num_dice, die)) + modifier


def roll_advantage(string: str) -> list[int]:
    """Return two calls to roll_string sorted highest to lowest.

    Args:
        string (str): A string of a roll of a number of dice with modifiers
    
    Attributes:
        roll_list (list): A list of rolls sorted from highest [0] to lowest [1]

    Returns:
        roll_list: A list of the roll result."""
    roll_list = [roll_string(string) for i in range(2)]

    roll_list.sort(reverse=True)

    return roll_list


def roll_disadvantage(string: str) -> list[int]:
    """Return call to roll_advantage sorted lowest to highest.

    Args:
        string (str): A string of a roll of a number of dice with modifiers
    
    Attributes:
        roll_list (list): A list of rolls sorted from lowest [0] to highest [1]

    Returns:
        roll_list: A list of the roll result."""
    roll_list = [roll_string(string) for i in range(2)]
    roll_list.sort()

    return roll_list


def roll_array(string: str) -> list[int]:
    """Return an array of a number of die rolls with modifiers.

    Args:
        string (str): A string of die with modifiers to be rolled a number of times 
    
    Attributes:
        parsed_string (dict): A dictionary of the roll elements in the string
        num_dice (int): Int of the number of dice to be rolled, default 1
        die (str): String of type of die to be rolled
        symbol (str): String of operator to be appled, default +
        modifier (int): An int to be applied to roll with operator, default 0
        rolls (list): List of ints of all rolls with modifier applied to each

    Returns:
        rolls: An array of ints of die rolls"""
    parsed_string = parse_die_string(string)
    num_dice = parsed_string["num dice"]
    die_roll = parsed_string["die"]
    symbol = parsed_string["operator"]
    modifier = parsed_string["modifier"]
    rolls = [roll_string(f"{die_roll}{symbol}{modifier}") for i in range(num_dice)]

    return rolls


def roll_ability_scores() -> list[int]:
    """Return a list of 6 4d6 minus the lowest for each group.

    Attributes:
        ability_die(func): Returns the total of 4d6 minus the lowest die
        abilities (list): An array of ints of all the scores rolled

    Returns:
        abilities: An array of 6 calls to ability_die sorted highest to lowest"""

    def ability_die() -> int:
        """Return an int of 4d6 - the lowest
        
        Attributes:
            ability (int): Total of all dice rolled
            four_d6 (list): List of ints of all dice rolled
        
        Returns:
            ability: Total of rolls with lowest deducted."""
        ability = 0
        four_d6 = roll_array("4d6")
        four_d6.sort()
        four_d6.pop(0)

        for die_roll in four_d6:
            ability += die_roll

        return ability

    abilities = [ability_die() for i in range(6)]
    abilities.sort(reverse=True)

    return abilities


@click.command()
@click.argument("diestring")
@click.option("--kind", 
              type=click.Choice(
                  ["advan", "disad", "array", "crit", "stand"], 
                  case_sensitive=False), default="stand", 
                  help="""kind of roll to make:\n
                          advan: roll twice, ordered high to low\n
                          disad: roll twice, ordered low to high\n
                          array: roll list of x dice\n
                          crit: roll with double the dice\n
                          stand: standard roll of dice""",
                  )
def cli(diestring, kind) -> None:
    """Return the total for a roll of a DIESTRING of the format XdY?Z, where:\n
            x is the number of dice to be rolled\n
            dY is the kind of die to roll, Y being the number of faces\n
            ? is an optional operator which applies a modifier to the roll total\n
            Z is an optional modifier applied to the roll total\n
        If DIESTRING is 'scores', an array of 6 (4d6 - the lowest die) is returned."""
    if diestring == "scores":
        all_dice = [roll_array("4d6") for i in range(6)]
        rolls_to_mod = deepcopy(all_dice)

        for roll in rolls_to_mod:
            roll.sort()
            roll.pop(0)
        
        totals = [0, 0, 0, 0, 0, 0]

        for index, dice_rolls in enumerate(rolls_to_mod):
            totals[index] += sum(dice_rolls)

        click.echo(f"Rolling: 6 (4d6 - lowest die)\nAllDice: {all_dice}\nRollSum: {totals}")

    else:
        if kind == "crit":
            parsed_string = parse_die_string(diestring)
            all_dice = roll_array(f"{parsed_string['num dice'] * 2}{parsed_string['die']}")
            dice_total = 0

            for roll in all_dice:
                dice_total += roll
            
            roll_total = 0
            if parsed_string["operator"] == "-":
                roll_total += (dice_total - parsed_string["modifier"])

            elif parsed_string["operator"] == "/" or parsed_string["operator"] == "??":
                roll_total += (dice_total / parsed_string["modifier"])

            elif parsed_string["modifier"] == "x" or parsed_string["modifier"] == "X" or parsed_string["modifier"] == "*":
                roll_total += (dice_total * parsed_string["modifier"])

            else:
                roll_total += (dice_total + parsed_string["modifier"])

            click.echo(f"Rolling: {diestring} (critical)\nAllDice: {all_dice}\nRollSum: {roll_total}")

        elif kind == "advan":
            parsed_string = parse_die_string(diestring)
            all_dice = roll_advantage(f"{parsed_string['num dice']}{parsed_string['die']}")
            roll_totals = []

            if parsed_string["operator"] == "-":
                roll_totals = [die - parsed_string["modifier"] for die in all_dice]

            elif parsed_string["operator"] == "/" or parsed_string["operator"] == "??":
                roll_totals = [die / parsed_string["modifier"] for die in all_dice]

            elif parsed_string["modifier"] == "x" or parsed_string["modifier"] == "X" or parsed_string["modifier"] == "*":
                roll_totals = [die * parsed_string["modifier"] for die in all_dice]

            else:
                roll_totals = [die + parsed_string["modifier"] for die in all_dice]
            
            click.echo(f"Rolling: {diestring} (advantage)\nAllDice: {all_dice}\nRollsum: {roll_totals}")

        elif kind == "disad":
            parsed_string = parse_die_string(diestring)
            all_dice = roll_disadvantage(f"{parsed_string['num dice']}{parsed_string['die']}")
            roll_totals = []
            
            if parsed_string["operator"] == "-":
                roll_totals = [die - parsed_string["modifier"] for die in all_dice]

            elif parsed_string["operator"] == "/" or parsed_string["operator"] == "??":
                roll_totals = [die / parsed_string["modifier"] for die in all_dice]

            elif parsed_string["modifier"] == "x" or parsed_string["modifier"] == "X" or parsed_string["modifier"] == "*":
                roll_totals = [die * parsed_string["modifier"] for die in all_dice]

            else:
                roll_totals = [die + parsed_string["modifier"] for die in all_dice]
            
            click.echo(f"Rolling: {diestring} (disadvantage)\nAllDice: {all_dice}\nRollsum: {roll_totals}")

        elif kind == "array":
            parsed_string = parse_die_string(diestring)
            all_dice = roll_array(f"{parsed_string['num dice']}{parsed_string['die']}")
            roll_totals = []

            if parsed_string["operator"] == "-":
                roll_totals = [die - parsed_string["modifier"] for die in all_dice]

            elif parsed_string["operator"] == "/" or parsed_string["operator"] == "??":
                roll_totals = [die / parsed_string["modifier"] for die in all_dice]

            elif parsed_string["modifier"] == "x" or parsed_string["modifier"] == "X" or parsed_string["modifier"] == "*":
                roll_totals = [die * parsed_string["modifier"] for die in all_dice]

            else:
                roll_totals = [die + parsed_string["modifier"] for die in all_dice]
            
            click.echo(f"Rolling: {diestring} (array)\nAllDice: {all_dice}\nRollsum: {roll_totals}")

        else:
            parsed_string = parse_die_string(diestring)
            all_dice = roll_array(f"{parsed_string['num dice']}{parsed_string['die']}")
            dice_total = 0

            for roll in all_dice:
                dice_total += roll
            
            roll_total = 0
            if parsed_string["operator"] == "-":
                roll_total += (dice_total - parsed_string["modifier"])

            elif parsed_string["operator"] == "/" or parsed_string["operator"] == "??":
                roll_total += (dice_total / parsed_string["modifier"])

            elif parsed_string["modifier"] == "x" or parsed_string["modifier"] == "X" or parsed_string["modifier"] == "*":
                roll_total += (dice_total * parsed_string["modifier"])

            else:
                roll_total += (dice_total + parsed_string["modifier"])

            click.echo(f"Rolling: {diestring} (standard)\nAllDice: {all_dice}\nRollSum: {roll_total}")