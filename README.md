<h1>DiceCLI</h1>
<p>A package of functions for rolling dice implented as a CLI.</p>
<p>The module contains functions that replicate rolling polyhedral dice with any number of faces and rolling them in different ways; as an array, at advantage; as a critical hit; at disadvantage and to roll an array of 6 ability scores.</p>
<p>This is acheived with the parse_die_string function, which takes a string and  returns a dictionary of all the elements of a die string (number of dice, die type, symbol & modifier) used by other functions to roll dice.</p>
<p>The cli function packages all of the above into an installable command line  interface called 'dice', implementing the various types of rolls through the --rolltype option.</p>
<h2>Functions<h2>
<h3>parse_die_string(string: str) -> Dict[str, Union[str, int]]:</h3>
<p>Returns a dict of the constituents of a die roll from a given string.<br>
    Args:<br>
        string (str): A string representing a die roll<br>
<br>    
    Returns:<br>
        parsed_roll: A dictionary of the roll string's elements.</p>