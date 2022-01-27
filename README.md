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
Returns:<br>
parsed_roll: A dictionary of the roll string's elements.</p>
<h3>roll_advantage(string: str) -> list[int]</h3>
<p>Return two calls to roll_string sorted highest to lowest.<br>
Args:<br>
string (str): A string of a roll of a number of dice with modifiers<br>
Attributes:<br>
roll_list (list): A list of rolls sorted from highest [0] to lowest [1]<br>
Returns:<br>
roll_list: A list of the roll result.</p>

<h3>roll_array(string: str) -> list[int]</h3>
<p>Return an array of a number of die rolls with modifiers.<br>
Args:
- string (str): A string of die with modifiers to be rolled a number of times
Attributes:
- parsed_string (dict): A dictionary of the roll elements in the string
- num_dice (int): Int of the number of dice to be rolled, default 1
- die (str): String of type of die to be rolled
- symbol (str): String of operator to be appled, default +
- modifier (int): An int to be applied to roll with operator, default 0
- rolls (list): List of ints of all rolls with modifier applied to each
Returns:
- rolls: An array of ints of die rolls</p>