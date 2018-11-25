#!/bin/bash
i="./dirA/dirC/dirD/file6"
count=0
while [ $count -le 5 ]; do
	echo "$i"
	parent=$(echo "$i" | sed -r 's_^(.+)(/[a-zA-Z0-9_-\.]+)$_\1_')
	echo "$parent"
	if [ "$parent" == "." ]; then 
		break
	else
		i="$parent"
	fi
	let count++
done
