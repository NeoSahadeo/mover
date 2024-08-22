#!/usr/bin/bash

move=/usr/local/bin/move
movepy=/usr/local/bin/mover/move.py
path=/usr/local/bin/mover

if [[ -d $path ]]; then
	echo "$path already exists. Skipping step"
else
	echo "Creating path at $path"
	mkdir $path
fi

echo "Copying script to $path"
cp move.py $path

should_write=1
if [[ -f $move ]]; then
	response=""
	should_write=0
	while [[ -z $response ]]; do
		echo -e "A file with the name 'move' exists at $move\nOverwrite file (y/n)?"
		read response
		if [[ $response == "y" || $response == "Y" ]]; then
			echo "Overwriting file!"
			rm $move
			should_write=1
		fi
	done
fi

create_file()
{
	echo "Creating Symlink"
	ln -s $movepy $move
	echo "Adding executable permissions"
	chmod +x $move
}

if [[ $should_write  -eq 1 ]]; then
	create_file
fi

if [[ -e "$move" && -e "$movepy" ]]; then
	echo "Install finished, enjoy! Restart bash and type 'move --help' to get started"
else
	echo -e "An error occured, try running 'install.sh' with admin rights.\nIf it's a bug let me know!"
fi
