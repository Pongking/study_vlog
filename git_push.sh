name=$1
description=$2

cp ~/.ssh/id_rsa_$1 ~/.ssh/id_rsa 
cp ~/.ssh/id_rsa_$1.pub ~/.ssh/id_rsa.pub 

git add .
git commit -m "$2"
git push -u origin main