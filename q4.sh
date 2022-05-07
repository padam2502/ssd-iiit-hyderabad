
Add() {
result=$(echo "scale=4; (( $1 + $2 ))" | bc)

echo " Sum is  $result" 
}
re='^[+-]?[0-9]+([.][0-9]+)?$'
if ( [ "$#" == 2 ] &&  [[ $1 =~ $re ]] && [[ $2 =~ $re ]] ) 
then
	Add $1 $2
fi
