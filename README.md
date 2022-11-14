# Waiter
W riting <br>
A n <br>
I terative <br>
T ext-type <br>
E solang <br>
R estaurant <br><br>
Writing code, by ordering food. <br>

## The "menu"

`<count> <burger/burgers> <chips/fries/coleslaw> [ketchup]`<br>
Asks the waiter for either input or output `<count>` amount of times.<br>
Chips or fries will output the number off the top of the stack in ASCII and will pop it off. Coleslaw will ask for input and push the character as a number in ASCII onto the top of the stack.<br>
Adding ketchup will output the number in ASCII *without* popping the value off.

`<count> <water/waters>`<br>
Asks the waiter to push `<count>` onto the top of the stack

`<count> <salt/salts>`<br>
Asks the waiter to pop the value at index `<count>`

`<if> [there] <is/isn't> {value}`<br>
Checks if `{value}` is/isn't equal to the value on the top the top of the stack.<br>
If the condition is true, it outputs 1 to the top of the stack.<br>
If the condition is false, it outputs 0 to the top of the stack.

`<count> <chicken/chickens>`<br>
Adds the top value of the stack to the second to top value of the stack

`<count> <beef/beefs>`<br>
Negates the top value of the stack to the second to top value of the stack

`<count> <mushroom/mushrooms>`<br>
Divides the top value of the stack to the second to top value of the stack

`<count> <stuffing/stuffings>`<br>
Multiplies the top value of the stack to the second to top value of the stack

`<count> <crisp/crisps>`<br>
Finds the modulus of the top value of the stack to the second to top value of the stack

`<count> <lemon/lemons>`<br>
Duplicates the top value of the stack to the top of the stack

`<count> <orange/oranges>`<br>
Swaps the entire stack e.g [4, 2, 6, 7] becomes [7, 6, 2, 4]<br>
Useful for burgers

`<infinite>`<br>
Stands for 2^63-1
