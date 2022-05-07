#!/bin/bash
x=$1
y=${#x}
f=0
z=$(echo $x | grep -o . | sort | tr -d "\n")
array=()
arr=()
while IFS= read -r line; do
    array+=("$line")
done < <( compgen -c   )
arraylength=${#array[@]}

for (( i=0; i<${arraylength}; i++ ));
do
tem=${array[$i]}
if [ "${#tem}" -eq "$y" ]
then
	ans=$(echo $tem | grep -o . | sort | tr -d "\n")
	#echo $ans
	if [[ "$ans" == "$z" ]]
	then
		if [  "$f" -eq "0" ] 
		then
			echo -n YES
			f=1
		fi	
	arr+=(${array[$i]})
	fi
fi
done

if [ "$f" -eq "0" ] 
then
echo "NO"
else
ar=()
ar+=$(echo ${arr[@]} | tr ' ' '\n' | sort -u | tr '\n' ' ')
for x in ${ar[@]}
do
echo -n -e "\t"
echo -n $x
done
fi
