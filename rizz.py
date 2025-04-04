import sys
import argparse

def init_code():
    """Returns the initial code for the compiler"""
    code = """_=+([]==[]);"""
    for i in range(2, 15):
        code += f"{'_'*i}={'_'*(i-1)}+_;"
    return code

def get_binary_factors(n):
    """Returns a list of factors of a given number in binary form"""
    return [index for index, bit in enumerate(bin(n)[:1:-1]) if bit == "1"]

def codegen(factors):
    """Generates code for a given list of factors"""
    char_code = ""
    for index, factor in enumerate(factors):
        char_code += "_" if factor == 0 else f"__**{'_'*factor}"
        if index < len(factors) - 1:
            char_code += "+"
    return char_code

def wrap_exec(encoded_string_len, encoded_python_string):
    """Wraps code in exec()"""
    return f"""exec((('%'+'c̶'[[]>[]])*({encoded_string_len}))%({','.join(encoded_python_string)}))"""

def main():
    parser = argparse.ArgumentParser(description='Python Code Rizzler')
    parser.add_argument('-r', '--run', action='store_true', help='Execute the generated code')
    parser.add_argument('-c', '--code', type=str, default='print("Hello, World!")', 
                        help='Python code to glow up (default: print("Hello, World!"))')

    args = parser.parse_args()

    # Generate obfuscated code
    encoded_python_string = [codegen(get_binary_factors(ord(char))) for char in args.code]
    encoded_string_len = codegen(get_binary_factors(len(args.code)))
    
    generated_code = init_code()
    generated_code += wrap_exec(encoded_string_len, encoded_python_string)
    
    print(generated_code)
    
    if args.run:
        exec(generated_code)

if __name__ == "__main__":
    main()
