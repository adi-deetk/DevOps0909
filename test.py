git init
echo 1 > 1.txt
git add .
git commit -am "init commit"
git checkout -b branch-ff
echo 2 > 2.txt
git add .
git commit -am "2nd commit"
git checkout master
echo 3 > 3.txt
git add .
git commit -am "3rd commit"
git checkout branch-ff
git merge branch-ff -m "merge"
git merge master -m "merge"
git checkout master
git merge branch-ff -m "merge"
ls -l
git log
git checkout branch-ff
echo 57 > 3.txt
git add .
git commit -am "4th commit"
git checkout master
echo 101 > 3.txt
git add .
git commit -am "5th commit"
git checkout branch-ff
git merge master
cat 3.txt
git status
git add .
git commit -am "merge commit"
git log --graph --oneline --all
git checkout master
git merge branch-ff
cat 3.txt
git checkout branch-ff
git merge master
cat 3.txt