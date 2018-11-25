#!/bin/bash
#find -depth -atime -30 -type f > recent_all
recent_all=($(find -depth -atime -30 -type f))

path_no_del_all=()
for j in ${recent_all[@]}; do
	echo "$j"
	i="$j"
	while (true); do
	#echo "$i"
	parent=($(dirname $i))
	echo "parent: $parent"
	path_no_del_all+=("$parent")
	if [ "$parent" == "." ]; then
		break
	else
		i="$parent"
	fi
	done
done
#echo "${path_no_del_all[*]}"

## I order and eliminate the folder duplicated
IFS=$'\n' path_no_del=($((sort <<<"${path_no_del_all[*]}") | uniq | sort ))
#printf "%s\n" "${path_no_del[@]}"

# Find array of all folder in the tree
folder_all=($(find -depth -type d))

for i in ${folder_all[@]}; do
	match=0
	for j in ${path_no_del[@]}; do
		if [ "$i" == "$j" ]; then
			#echo "match found for $i"
			match=1
			break
		fi
	done
	if [ "$match" -eq 0 ]; then
		arch=("$i".tgz)
		tar -cvf $arch $i 2>/dev/null
		rm -rf $i
	fi
done
