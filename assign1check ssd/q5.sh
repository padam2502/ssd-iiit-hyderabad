#!/bin/bash
fn() {
    
    touch "$1$2.txt"
    if(($2 > 1))
    then 
    	fn "$1" $(($2 - 1))
    fi
    
}
ch() {
	mv "temp$1.txt" "temp$1.md"
	if(($1 > 1))
	then
		ch $(($1 - 1))
	fi
		
}	
mod() {
	
	if(($1 > 25))
	then
		mv "temp$1.txt" "temp$1_modified.txt"
	else
		mv "temp$1.md" "temp$1_modified.md"
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
zip -q txt_compressed.zip *.txt
