<h1>DiceCLI</h1>
<p>A package of functions for rolling dice implented as a CLI.<br>
The module contains functions that replicate rolling polyhedral dice with any number of faces and rolling them in different ways; as an array, at advantage; as a critical hit; at disadvantage and rolling an array of 6 ability scores.<br>
This is acheived with the parse_die_string function, which takes a string and  returns a dictionary of all the elements of a die string (number of dice, die type, symbol & modifier) used by other functions to roll dice.<br>
The cli function packages all of the above into an installable command line  interface called 'dice', implementing the various types of rolls through the --kind option.<br>
To install the command line interface, download the package, navigate to the root folder and issue the following command:<br>
<code>pip install --editable .</code><br>
You may wish to create a virtual environment before doing this, ensuring the package does not experience dependency conflicts.<br>
Also included is a dockerfile that will allow you to install the app in a containerised linux terminal if you so wish.</p>

<h3>cli(diestring, kind) -> None</h3>
<p>The entry point for the dice command line tool.<br>
The dice command returns the total for a roll of a DIESTRING of the format XdY?Z, where:<br>
<ul>
<li>X is the number of dice to be rolled</li>
<li>dY is the kind of die to roll, Y being the number of faces</li>
<li>? is an optional operator which applies a modifier to the roll total</li>
<li>Z is an optional modifier applied to the roll total</li>
</ul>
If DIESTRING is 'scores', an array of 6 (4d6 - the lowest die) is returned.<br>
<br>
--kind can be used to roll the DIESTRING with the following options:
<ul>
<li>advan: roll twice, ordered high to low</li>
<li>disad: roll twice, ordered low to high</li>
<li>array: roll list of x dice</li>
<li>crit: roll with double the dice</li>
<li>stand: standard roll of dice (default option)</li>
</ul></p>

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

<h3>roll_ability_scores() -> list[int]</h3>
<p>Return a list of 6 4d6 minus the lowest for each group.<br>
Attributes:<br>
<ul>
<li>ability_die(func): Returns the total of 4d6 minus the lowest die</li>
<li>abilities (list): An array of ints of all the scores rolled</li>
</ul>
Returns:<br>
<ul>
<li>abilities: An array of 6 calls to ability_die sorted highest to lowest</li>
</ul></p>

<h3>roll_crit(string: str) -> int</h3>
<p>Return an int of a roll with doubled dice and modifiers applied.<br>
Args:<br>
<ul>
<li>string (str): A string of a roll of dice with modifiers</li>
</ul>
Attributes:<br>
<li>parsed_string (dict): A dictionary of the roll elements in the string</li>
<li>num_dice (int): Int of the number of dice to be rolled, default 1</li>
<li>die (str): String of type of die to be rolled</li>
<li>symbol (str): String of operator to be appled, default +</li>
<li>modifier (int): An int to be applied to roll with operator, default 0</li>
</ul>
Returns:<br>
<ul>
<li>roll: A int returned from a call to the roll_mult function.</li>
</ul></p>

<h3>roll_d(num: int) -> int</h3>
Return a random number between 1 and num.<br>
Args:<br>
<ul>
<li>num (int): An int for the number of faces on the die</li>
</ul>
Returns:<br>
<ul>
<li>roll (int): Int of the the number rolled.</li>
</ul></p>

<h3>roll_disadvantage(string: str) -> list[int]</h3>
<p>Return call to roll_advantage sorted lowest to highest.<br>
Args:<br>
<ul>
<li>string (str): A string of a roll of a number of dice with modifiers</li>
</ul>
Attributes:<br>
<ul>
<li>roll_list (list): A list of rolls sorted from lowest [0] to highest [1]</li>
</ul>
Returns:<br>
<ul>
<li>roll_list: A list of the roll result.</li>
</ul>
</p>

<h3>roll_mult(num: int, die: str) -> int</h3>
Return a die or dice rolled a number of times.<br>
Args:<br>
<ul>
<li>num (int): The number of dice to roll</li>
<li>die (string): A string representing a die</li>
</ul>
Attributes:<br>
<ul>
<li>roll_total (int): An int for the total of all dice rolled</li>
<li>faces (int): An int of the number of faces on the die</li>
</ul>
Returns:<br>
<ul>
<li>roll_total: The combined total of all dice rolls.</li>
</ul></p>