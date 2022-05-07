question 1:

du is use to show the directories and size. sort is sorting it. NR!=1 is use to ommit the size of cuurent directory. output is tab separated.


question 2:

grep is used to print all the words ending with ing (case insensitive by using -i ) print tolower is prnting all the content in lower case in same line space separated. sed is used to replace space with newline character.


question 3:

x is storing the input command name. f is variable to print YES only once. z is storing the sorted value of x. y is storing the length of given command. compgen -c is use to generate all the commands which are atored in array as its elements. Then we are traversing the elements of array and checking whether its length is same as the input command . If it is then we are checking if its sorted value is equal to the sorted value of input command. if it is , then we are storing that particular command into arr. Finally we are printing the all the elements of arr in sorted order. else if f is not changed then we are simply printing NO.


question 4:

Add function is adding the two integer values. romantoint function is using sed command to substitute the given roman number into I using priority.and then simply printing the count of I. inttoroman function is subtracting the number priority wise untill it becomes zero using decrement function and adding the correspondind romanvalue.


question 5:

mkdir is making the directory temp_activity. then moving inside the temp_activity by cd. fn is function creating 50 files with names temp1.txt, temp2.txt... recursivly. then ch is function which is Changing the extensions of files from temp1 to temp25 from txt to md recursivly. then mod function is modifying the extensions temp<i>.<extension> to temp<i>_modified.<extension> where <i> is between 1 to 50. then zip -q is Zipping all the .txt files ONLY and name the ZIP file as txt_compressed.zip. orignal zip files are not deleted.
