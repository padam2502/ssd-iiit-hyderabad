fn() {
    
    touch "$1_$2.txt"
    if(($2 > 1))
    then 
    	fn "$1" $(($2 - 1))
    fi
    
}
ch() {
	mv "temp_$1.txt" "temp_$1.md"
	if(($1 > 1))
	then
		ch $(($1 - 1))
	fi
		
}	
mod() {
	
	if(($1 > 25))
	then
		mv "temp_$1.txt" "temp_$1_modified.txt"
	else
		mv "temp_$1.md" "temp_$1_modified.md"
	fi
	if(($1 > 1))
	then
		mod $(($1 - 1))
	fi
}
	
mkdir temp_activity
cd temp_activity
fn temp 50
ch 25
mod 50
zip txt_compressed.zip *.txt
