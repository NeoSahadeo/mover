# Mover

A "non-replacement" for GNU mv.

Mover currently adds the ability to quickly rename files.

[Install](#install)

[Commands](#commands)

Example:

```bash
move ./this/is/a/nested/file.txt -r file.py 

Output:
./this/is/a/nested/file.py
```

# Install

Clone the repo

```bash
git clone --depth=1 https://github.com/NeoSahadeo/mover
cd mover
```

Run as admin

```bash
./install.sh
```

## Changing the install path

Open `install.sh`

- `path` and `movepy` are related. The file `movepy` is inside of `path`.
- `move` is the symlink. This should go in you user binaries. You can move it
just remember to add it to the system path.

## Future Plans

Plans for features:

- [ ] Relative directory moving.
- [ ] Timing functions for moving.

## Commands

`-h` or `--help` will display a help message.

`-r` or `--rename` will rename a file. Specify the source first
then the name you want.

`-f` or `--force` will force a file overwrite (needed if files or
folders already exist).
