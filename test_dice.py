"""Script for testing the functions of the dice module."""

import unittest

from dice import parse_die_string
from dice import roll_ability_scores
from dice import roll_advantage
from dice import roll_array
from dice import roll_crit
from dice import roll_d
from dice import roll_disadvantage
from dice import roll_mult
from dice import roll_string


class die_test(unittest.TestCase):
    """Class for testing the dx and roll functions."""

    def setUp(self) -> None:
        """Set up the variables used in tests"""

        self.standard_string = '1d20+2'
        self.crit_string = '2d6+2'
        self.array_string = '2d8+1'
        self.one_to_twenty = range(1, 21)
        self.two_to_eight = range(2, 9)
        self.two_to_seventeen = range(2, 18)
        self.three_to_eighteen = range(3, 19)
        self.three_to_twenty_three = range(3, 24)
        self.six_to_twenty_six = range(6, 27)

    def test_range(self):
        """Test that the output of each roll function is in expected range."""
        d20_roll = roll_d(20)
        mult_dice_roll = roll_mult(2, "d4")
        string_roll = roll_string(self.standard_string)
        crit_roll = roll_crit(self.crit_string)
        advantage_roll = roll_advantage(self.standard_string)
        disadvantage_roll = roll_disadvantage(self.standard_string)
        array_roll = roll_array(self.array_string)
        scores_roll = roll_ability_scores()

        self.assertIn(d20_roll, self.one_to_twenty)
        self.assertIn(mult_dice_roll, self.two_to_eight)
        self.assertIn(string_roll, self.three_to_twenty_three)
        self.assertIn(crit_roll, self.six_to_twenty_six)
        self.assertIn(advantage_roll[0], self.three_to_twenty_three)
        self.assertIn(advantage_roll[1], self.three_to_twenty_three)
        self.assertIn(disadvantage_roll[0], self.three_to_twenty_three)
        self.assertIn(disadvantage_roll[1], self.three_to_twenty_three)
        self.assertIn(array_roll[0], self.two_to_seventeen)
        self.assertIn(array_roll[1], self.two_to_seventeen)
        self.assertIn(scores_roll[0], self.three_to_eighteen)
        self.assertIn(scores_roll[1], self.three_to_eighteen)
        self.assertIn(scores_roll[2], self.three_to_eighteen)
        self.assertIn(scores_roll[3], self.three_to_eighteen)
        self.assertIn(scores_roll[4], self.three_to_eighteen)
        self.assertIn(scores_roll[5], self.three_to_eighteen)

    def test_type(self):
        """Test that functions return the correct types."""
        d20_roll = roll_d(20)
        mult_dice_roll = roll_mult(2, "d4")
        string_roll = roll_string(self.standard_string)
        crit_roll = roll_crit(self.crit_string)
        advantage_roll = roll_advantage(self.standard_string)
        disadvantage_roll = roll_disadvantage(self.standard_string)
        array_roll = roll_array(self.array_string)
        scores_roll = roll_ability_scores()
        parsed_string = parse_die_string(self.standard_string)

        self.assertIsInstance(d20_roll, int)
        self.assertIsInstance(mult_dice_roll, int)
        self.assertIsInstance(string_roll, int)
        self.assertIsInstance(crit_roll, int)
        self.assertIsInstance(advantage_roll, list)
        self.assertIsInstance(advantage_roll[0], int)
        self.assertIsInstance(advantage_roll[1], int)
        self.assertIsInstance(disadvantage_roll, list)
        self.assertIsInstance(disadvantage_roll[0], int)
        self.assertIsInstance(disadvantage_roll[1], int)
        self.assertIsInstance(array_roll, list)
        self.assertIsInstance(array_roll[0], int)
        self.assertIsInstance(array_roll[1], int)
        self.assertIsInstance(scores_roll, list)
        self.assertIsInstance(scores_roll[0], int)
        self.assertIsInstance(scores_roll[1], int)
        self.assertIsInstance(scores_roll[2], int)
        self.assertIsInstance(scores_roll[3], int)
        self.assertIsInstance(scores_roll[4], int)
        self.assertIsInstance(scores_roll[5], int)
        self.assertIsInstance(parsed_string, dict)
        self.assertIsInstance(parsed_string["num dice"], int)
        self.assertIsInstance(parsed_string["die"], str)
        self.assertIsInstance(parsed_string["operator"], str)
        self.assertIsInstance(parsed_string["modifier"], int)


if __name__ == "__main__":
    unittest.main()
