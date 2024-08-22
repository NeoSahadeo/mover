from pathlib import Path
import sys
import shutil
import os

help = """Usage: mv [OPTION] SOURCE(s) DESTINATION
or: mv SOURCE(s) DESTINATION [OPTION]
or: mv SOURCE(s) [OPTION] DESTINATION
The mv program is a move file(s)/folder(s) command meant to
make moving files/folders easier than the GNU 'mv' program.

Options:
    -f, --force     Force file/folder overwrites
    -r, --rename    Rename file/folder
"""

incorrect_format = """Directories listed are not in the correct format.
There should be no spaces between the brackets.
If you are only moving one thing, there should be no brackets and no
quotes.

To have more than a single SOURCE try:
    mv {"source1","source2","source3"} DESTINATION
"""


class MoveFiles:
    def __init__(self, argv):
        self.allowed_commands = ["--help", "-h",
                                 "--rename", "-r",
                                 "--force", "-f"]
        self.flags = {
            "rename": False,
            "force": False
        }
        self.cwd = Path.cwd()
        self.argv = argv[1:]
        self.destination = ""
        self.sources = []

        self.validate_argv()

    def mv(self):
        """ The main method used to call different
            methods.
        """
        if not self.flags["rename"]:
            for source in self.sources:
                shutil.move(source, self.destination)
        elif self.flags["rename"]:
            self.rename()

    def delete(self, source):
        """ Deletes the file/folder supplied.
        """
        try:
            shutil.rmtree(source)
            # os.remove(source)
        except FileNotFoundError:
            raise SystemExit(f"File/folder does not exist: {source}")

    def rename(self):
        """ Renames the source to the destination. Allows for force
            overwrites.
        """
        if len(self.sources) >= 2 and self.destination:
            raise SystemExit("Cannot rename multiple files")

        try:
            original_dir = os.path.dirname(self.sources[0])
            new_dir = os.path.join(original_dir, self.destination)
            self.check_destination(new_dir)
            os.rename(self.sources[0], new_dir)
        except FileNotFoundError:
            raise SystemExit(f"File/folder does not exist: {self.sources[0]}")
        except IsADirectoryError:
            if not self.flags["force"]:
                raise SystemExit(f"A folder exists with the name: {self.destination}.\nUse 'mv -f -r SOURCE NEW_NAME'")
            self.delete(new_dir)
            os.rename(self.sources[0], new_dir)

    def check_destination(self, destination):
        if os.path.exists(destination) and not self.flags["force"]:
            raise SystemExit("A file/folder with same name exists.\nUse 'mv -f -r SOURCE NEW_NAME'")

    def validate_argv(self):
        """
            Validates that all argument commands supplied
            exist.
            Does extra validation to make sure commands can
            be used together.
        """
        if len(self.argv) == 0:
            raise SystemExit(help)

        commands = [command.split(" ") for command in self.argv if command.startswith("-")]
        directories = [dir.split(" ") for dir in self.argv if not dir.startswith("-")]

        # Check if the directory list is valid
        if len(directories) < 2:
            raise SystemExit(help)
        self.destination = directories[-1][0]
        for index in range(0, len(directories) - 1):
            dir = directories[index][0]
            self.sources.append(dir)
            if ("{") in dir:
                raise SystemExit(incorrect_format)

        # Check if commands are valid
        if len(commands) == 0:
            return
        for command in commands:
            command = command[0]
            try:
                self.allowed_commands.index(command)
                # Immediately run help command
                if command == "--help" or command == "-h":
                    raise SystemExit(help)

                match command:
                    case "-r":
                        self.flags["rename"] = True
                    case "--rename":
                        self.flags["rename"] = True
                    case "-f":
                        self.flags["force"] = True
                    case "--force":
                        self.flags["force"] = True

            except ValueError:
                raise SystemExit(f"Command does not exist: {command}\nFor help run 'mv --help'")


if __name__ == "__main__":
    movefiles = MoveFiles(sys.argv)
    movefiles.mv()
