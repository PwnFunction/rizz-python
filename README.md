# rizz-python

Transpiler to glow up your python code.

### Usage 

```
usage: rizz.py [-h] [-r] [-c CODE] [-i FILE] [-o FILE]

Python Code Rizzler

options:
  -h, --help        show this help message and exit
  -r, --run         Execute the generated code
  -c, --code CODE   Python code to glow up (default: print("Hello, World!"))
  -i, --input FILE  Input file to glow up
  -o, --output FILE Output file to write the generated code
```

### Examples

```sh
# Print the obfuscated code output
python3 rizz.py -c "print('skibidi')"

# Run the obfuscated code output
python3 rizz.py -c "print('skibidi')" -r
```

```sh
# Input file to obfuscate
python3 rizz.py -i input.py
```

```sh
# Output file to write the generated code
python3 rizz.py -c "print('skibidi')" -o output.py
```

```sh
# Run calculator on mac
python3 rizz.py -c "import os;os.system('open -a Calculator')" -r
```

```sh
# Run calculator on windows
python3 rizz.py -c "import os;os.system('calc.exe')" -r
```

