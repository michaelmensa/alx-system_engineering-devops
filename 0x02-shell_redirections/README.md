Shell Redirections

Task 0; echo 'Hello, World'
Task 1; echo '(Ôo)'
Task 2; cat /etc/passwd
Task 3; cat /etc/passwd /etc/hosts
Task 4; tail /etc/passwd- display the last 10 lines of /etc/passwd
Task 5; head /etc/passwd- display the first 10 lines of /etc/passwd
Task 6; head -n 3 iacta | tail -n 1 displays the third line of the file, iacta without using the command sed.
Task 7; echo 'Best School' >\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)
Task 8; ls -la >ls_cwd_content
Task 9; tail -n 1 iacta >> iacta
Task 10; find . -type f -name "*.js" -delete
Task 11; find . -type d -not -name '.' | wc -l
Task 12; ls -t1 | head -n 1
Task 13; sort | uniq -u
Task 14; grep -i "root" /etc/passwd find that word
Task 15; grep -c -i "bin" /etc/passwd count that word
Task 16; grep -i "root" -A 3 /etc/passwd what's next?
Task 17; grep -i -v "bin" /etc/passwd hide that word
Task 18; grep -i "^[a-z]" /etc/ssh/sshd_config letteronly
Task 19; tr "A" "Z" | tr "c" "e"
Task 20; tr -d "cC"
Task 21; rev means reverse
Task 22; cut -d ':' -f 1,6 /etc/passwd | sort
