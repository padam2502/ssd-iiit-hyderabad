#!/bin/bash

decrement()
{
  romanvalue="${romanvalue}$2"
  number=$(( $number - $1 ))

}
inttoroman()
{
number=$1
while [ $number -gt 0 ] ; do

if [ $number -ge 1000 ] ; then
  decrement 1000 "M"
elif [ $number -ge 900 ] ; then
  decrement 900 "CM"
elif [ $number -ge 500 ] ; then
  decrement 500 "D"
elif [ $number -ge 400 ] ; then
  decrement 400 "CD"
elif [ $number -ge 100 ] ; then
  decrement 100 "C"
elif [ $number -ge 90 ] ; then
  decrement 90 "XC"
elif [ $number -ge 50 ] ; then
  decrement 50 "L"
elif [ $number -ge 40 ] ; then
  decrement 40 "XL"
elif [ $number -ge 10 ] ; then
  decrement 10 "X"
elif [ $number -ge 9 ] ; then
  decrement 9 "IX"
elif [ $number -ge 5 ] ; then
  decrement 5 "V"
elif [ $number -ge 4 ] ; then
  decrement 4 "IV"
elif [ $number -ge 1 ] ; then
  decrement 1 "I"
fi

done
echo $romanvalue
}



Add() {
result=$(echo "scale=4; (( $1 + $2 ))" | bc)
echo "$result" 
}

romantoint()
{
	x=$1
	x=$(echo $x | tr “[a-z]” “[A-Z]”)
	number=$(echo ${x} | sed 's/CM/DCD/g' | sed 's/M/DD/g' | sed 's/CD/CCCC/g' | sed 's/D/CCCCC/g' | sed 's/XC/LXL/g' | sed 's/C/LL/g' | sed 's/XL/XXXX/g' | sed 's/L/XXXXX/g' | sed 's/IX/VIV/g' | sed 's/X/VV/g' | sed 's/IV/IIII/g' | sed 's/V/IIIII/g' )
	echo ${#number}
}
re='^[+-]?[0-9]+([.][0-9]+)?$'
if ( [ "$#" == 1 ] )
then
	inttoroman $1
	
	
elif ( [ "$#" == 2 ] &&  [[ $1 =~ $re ]] && [[ $2 =~ $re ]] ) 
then
	x=$(Add $1 $2)
	ans=$(inttoroman $x)
	echo $ans
else
	x=$(romantoint $1 )
	y=$(romantoint $2 )
	ans=$(Add $x $y)
	echo $ans
	
fi




