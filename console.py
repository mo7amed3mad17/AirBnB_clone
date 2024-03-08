# Command interpreter in Python

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """This quits or exits the program"""
        return True

    # Aliasing
    do_EOF = do_quit

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
