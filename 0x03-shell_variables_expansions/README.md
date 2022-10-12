Shell variables and Expansions

0; #!/bin/bash
alias ls="rm * "        Create a script that creates an alias.

1; #!/bin/bash
echo "hello $USER"      Create a script that prints hello user, where user is the current Linux user.

2; #!/bin/bash
export PATH=$PATH:/action     Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program.

3; #!/bin/bash
echo $((`echo $PATH | grep -o ":/" | wc -l`+ 1))    

4; #!/bin/bash
printenv

5; #!/bin/bash
set

6; #!/bin/bash
BEST="School"

7; #!/bin/bash
export BEST="School"

8; #!/bin/bash
echo $(($TRUEKNOWLEDGE + 128))

9; #!/bin/bash
echo $(($POWER / $DIVIDE))

10; !/bin/bash
echo $(($BREATH**$LOVE))

11; #!/bin/bash
echo $((2#$BINARY))

12; #!/bin/bash
echo {a..z}{a..z} | tr " " "\n" | grep -v "oo"

13; #!/bin/bash
printf "%.2f" $NUM | sort
