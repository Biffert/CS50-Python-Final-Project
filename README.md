# Mine Finder
#### Video Demo:  https://www.youtube.com/watch?v=HElxqK8kcWg
#### Description:
##### Introduction
This project is a simple game in which the player's goal is to find the bomb in a mine field by digging up fields in a grid. The player is prompted for the the mine field size at the start of the game. The position of the bomb is generated randomly and the bomb itself is surrounded by flags on the left, right, up and down position. To win the player must clear all fields, except the one where the bomb is hidden. If, however, the player digs up the bomb instead they will lose and the message "Your head a splode!" is printed (as a hommage to Homestar Runner's "Strong Bad Email #94 - Video Games").

This project contains the following functions:
1. main()
2. generate_field()
3. valid_move()
4. parse_move()

##### 1. main()
```main()``` starts off by asking the player for the desired field size, which is stored in the variable difficulty. As a requirement this should be an int between 5 and 10.

Based on this input, the variable bomb_location is generated with random.choice() from a string of the first letters of the alphabet and a string of a number sequence. Both with a length of the input difficulty at the start.

The mine_field is generated with ```generate_field(difficulty)```, which creates a list of dictionaries.

After this, the mine field is printed with ```tabulate()``` and the player is asked to enter a valid field which they want to clear. The input's validity is checked by the function ```valid_move()```. See ```valid_move()``` for more details.

This player will be reprompted until all fields except for the bomb have been cleared, or the player digs up te bomb and explodes.

If it is a valid move, the player move will be stored in the list previous_moves.

After it is validated, player move is processed with ```parse_move()``` in which the flag positions are generated. The corresponding field in mine field is altered to the the right emoji (💣, 🚩 or 🟫) and returned. See ```parse_move()``` for more details.

##### 2. generate_field()
The difficulty is passed by ```generate_field(difficulty)```. It creates a list of dictionaries based on the player's input for field size. I.e. a field size of 5 results in a 5*5 grid, with rows from 'a' to 'e' and columns from 1 to 5. All fields contain "grass" depicted as '🟩'. One dictionary/row looks as follows:

```{' ': 'a', '1': '🟩', '2': '🟩', '3': '🟩', '4': '🟩', '5': '🟩'}```

##### 3. valid_move()
```valid_move()``` returns True if the input is a valid field in the generated mine field and not a previously cleared field.

#### 4. parse_move()
When parse_move() is called it generates the four flag positions and stores them as variables.

It then check whether the player's move is either the location of a bomb or a flag. In case of a bomb it will replace the value 🟩 with a 💣. In case of a flag it will replace the value 🟩 with a 🚩. In all other cases the value 🟩 will be replaced with dirt (🟫).

```parse_move()``` does this by going through the mine field (list of dictionaries) and finding the dictionary where key " " has a value of the row input (alphabetical, i.e. "a") and then replacing the value of the column input (numeral, i.e. "1") in that dictionary. For example:

```{' ': 'a', '1': '🟩', '2': '🟩', '3': '🟩', '4': '🟩', '5': '🟩'}```

becomes

```{' ': 'a', '1': '🟫', '2': '🟩', '3': '🟩', '4': '🟩', '5': '🟩'}```

After this the mine field is returned.
