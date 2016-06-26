# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

grep: to look inside a file
find: to find files
man: seek help manual
env: environment variables
rmdir: remove directory
rm: remove file
sudo: execute a command as super user
pushd: to save the directory
popd: to return to the saved directory
touch: create new items

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

ls: list all files/folders in the current directory
ls -a: list all files/folders in the current directory including the files starting with "."
ls -l: list all files/folders in the current directory, in long format listing
ls -lh: list all files/folders in the current directory the long format listing, using suffixes for file size
ls -lah: list all files/folders, including files starting with ".", in the current directory the long listing format, using suffixes for file size
ls -t: list all files/folders, sorted by time modified
ls -Glp: list all files/folders, in long listing format, enabling colorized output, write a "slash" if the file is a directory
---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

ls -1: display each items in a line
ls -R: display subdirectories
ls -d: display only directories
ls -u: display according to access time
ls -m: display as comma separated list

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

Construct argument lists and execute 

e.g. echo a b c d e f | xargs -n 3
echo a b c d e f | xargs -n 3

xargs sets the max number of arugment taken from the input (which is 3) every time



 

