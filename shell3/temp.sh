#!/bin/bash
find -depth -atime -30 -type f > recent_all
rm path_no_del_all 2>/dev/null 
rm path_no_del 2>/dev/null 
while read p; do
	i=$p
	while (true); do
	#echo "$i"
	parent=$(echo "$i" | sed -r 's_^(.+)(/[a-zA-Z0-9_-\.]+)$_\1_')
	echo "$parent" >> path_no_del_all
	if [ "$parent" == "." ]; then
		break
	else
		i="$parent"
	fi
	done
done < recent_all

## I order and eliminate the folder duplicated
cat path_no_del_all | sort | uniq | sort >> path_no_del
rm path_no_del_all

find -depth -type d > folder_all
sort folder_all path_no_del path_no_del | uniq -u | sort > compress_folder
while read p; do
	arch=("$p".tar)
	tar -cvf $arch $p 2>/dev/null
	rm -rf $p
done < compress_folder

