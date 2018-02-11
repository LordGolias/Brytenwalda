# A git repository of Brytenwalda (Mount and Blade)

This repository contains the necessary code to compile the Brytenwalda mod for Mount and Blade.
Thanks for checking it out!

You can compile it using Python 3, and it has no other dependencies.

## Compile and installing the mod

To compile the mod, run::

    python -m compile

This generates a set of `.txt` in `output` directory.
Copying all these files to the `Brytenwalda` directory and `Brytenwalda` to 
your Mount and Blade `modules` directory installs the mod.

## Code organization

The code is divided in different Python packages:

### Source

The source package contains the traditional source code for compiling Brytenwalda.

The basic definitions that bridge the code to the correct codes in the Mount and Blade game
are found in the modules `header_*.py`; the actual source code that is compiled into
`*.txt` files is in `module_*.py`.

The source code also contains different packages that contain parts of the mod 
(e.g. multiplayer, companions, [trade] caravans).
They are divided so it is easier to identify them in the source code, as well as 
making them easier to remove from the compilation process, if needed.

#### Notes

- Global variables are automatically assigned 0 at the beginning
- Slots are automatically assigned 0 at the beginning

### Compiler

The compiler package contains the compiler that converts the source code into
the `*.txt` files. The actual compiler is at `compiler/compiler.py`, the code that imports 
all objects from the source is found at `compiler/objects.py`.

## Authors

A huge thank to the persons that contributed to this mod.

- gwitt
- Beaver - [tripping when walking backwards]
- Baron Conrad [weapons break in combat]
- Cruger
- Somebody
- chief
- Cabadrin
- xenoargh [shield bash]
- Sinisterius [shield bash]
- MadVader [death camera]
- Beaver [walk backwards trip]
- theoris [decapitation in battle]
- Windyplains [Health regeneration]
- zerilius
- daedalus
- rubik [auto loot]

Finding all the authors is hard. Please help us to complete this list!
