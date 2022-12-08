# Advent of Code

Included in this repo is a `setup.sh` script. To make the most of it, make sure you can open VS Code from the terminal. If you can't, you can follow the instructions [here](https://www.freecodecamp.org/news/how-to-open-visual-studio-code-from-your-terminal/).

You can run the script with:
```
source setup.sh [year] [day] $(<.session.txt)
```

Where `.session.txt` is a file in this repo's root directory which contains your advent of code `session` cookie value.


To make this easier, I added this alias to my `.zshrc`.


```
aoc() { 
    echo "Hello... Setting up your AOC environment for $1 day $2"
    cd path/to/aoc/root
    echo "Moved to the AOC directory"
    source setup.sh $1 $2 $(<.session.txt)
    echo "Pulled the input and set up your python file"
}
```

So I can just open up the terminal and run

```
aoc [year] [day]
```

and it'll open up VS Code with the input file and a python template.
