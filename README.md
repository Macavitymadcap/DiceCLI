<h1>DiceCLI</h1>
<p>A package of functions for rolling dice implented as a CLI.</p>
<p>The module contains functions that replicate rolling polyhedral dice with any number of faces and rolling them in different ways; as an array, at advantage; as a critical hit; at disadvantage and to roll an array of 6 ability scores.</p>
<p>This is acheived with the parse_die_string function, which takes a string and  returns a dictionary of all the elements of a die string (number of dice, die type, symbol & modifier) used by other functions to roll dice.</p>
<p>The cli function packages all of the above into an installable command line  interface called 'dice', implementing the various types of rolls through the --rolltype option.</p>
<h2>Functions<h2>
<h3>parse_die_string(string: str) -> Dict[str, Union[str, int]]:</h3>
<p>Returns a dict of the constituents of a die roll from a given string.<br>
Args:<br>
<ul>
<li>string (str): A string representing a die roll</li>
</ul>
Returns:<br>
<ul>
<li>parsed_roll: A dictionary of the roll string's elements.</li>
</ul></p>

<h3>roll_advantage(string: str) -> list[int]</h3>
<p>Return two calls to roll_string sorted highest to lowest.<br>
Args:<br>
<ul>
<li>string (str): A string of a roll of a number of dice with modifiers</li>
</ul>
Attributes:<br>
<ul>
<li>roll_list (list): A list of rolls sorted from highest [0] to lowest [1]</li>
</ul>
Returns:<br>
<ul>
<li>roll_list: A list of the roll result.</li>
</ul></p>

<h3>roll_array(string: str) -> list[int]</h3>
<p>Return an array of a number of die rolls with modifiers.<br>
Args:<br>
<ul>
<li>string (str): A string of die with modifiers to be rolled a number of times</li>
</ul>
Attributes:<br>
<ul>
<li>parsed_string (dict): A dictionary of the roll elements in the string</li>
<li>num_dice (int): Int of the number of dice to be rolled, default 1</li>
<li>die (str): String of type of die to be rolled</li>
<li>symbol (str): String of operator to be appled, default +</li>
<li>modifier (int): An int to be applied to roll with operator, default 0</li>
<li>rolls (list): List of ints of all rolls with modifier applied to each</li>
</ul>
Returns:<br>
<ul>
<li>rolls: An array of ints of die rolls</li>
</ul></p>