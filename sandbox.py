import json

from tests.block_test import Block

def main():
    with open(".\output.json", "w") as file:
        content = Block("Google").run()
        file.write(json.dumps(content))
     

if __name__ == "__main__":
    main()