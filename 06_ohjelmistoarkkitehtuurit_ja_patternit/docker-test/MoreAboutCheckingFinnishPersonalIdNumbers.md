Finnish personal identity number, e.g. 311208A123X or 010199-1234 can be incorrect or invalid at least these ways:

1.	Length is not the correct 11 characters (MMDDYY*NNNX)

1.	Characters at positions 1-6 and 8-10 aren't digits (number characters '0'-'9')

1.	Character at position 7 is not one of '+','-','A'

1.	The checksum character at position 11 does not follow the [check character calculation rules](https://maol.fi/materiaalit/kpm/7-luokka/racket-7-lk/1ljl/1-4-jakoj%C3%A4%C3%A4nn%C3%B6s/henkil%C3%B6tunnus/)

1.	The date is not a valid date (not checked by the checksum character!)

	a.	Notice also that the century character '+','-','A' will affect checking the leap year check!

1.	The number might be technically fully valid, but never given to any person (database needed for checking)

1.	The number might have been given, but the person has already passed away (database needed)

1.	The number might have been given, but the person has received a new number and the old is obsolete (database needed)

**Minimum version**: In this task first check the length and that the very first character (position 1, depending on programming language index 0 or 1) is a digit.

**Optional version**: If you have time later you can practice and implement a full check. The 'database' you can simulate with a list of e.g. three personal identity numbers. Use e.g. 999 for the NNN part to make sure those are not real id numbers. Remember to bother the 'database' only after checking all you can without it.
