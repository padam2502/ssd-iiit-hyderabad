grep -o "\w\+*ing\+ " $1 > $2
echo "Inside $2 file"
cat $2
