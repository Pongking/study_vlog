search_dir="$1"

# find "$search_dir" -type f -name "torch"
# grep -rl "str" ./dir    simple
# grep -Fnr "str" .dir   detial
find "$search_dir" -type f -exec grep -l "torch" {} \;

#sudo diff -u userinfo.txt userin.txt > ~/differ.txt