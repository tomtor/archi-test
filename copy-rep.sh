for i in "/v/IT/Architectuur/Domein Architectuur/Archi Repository/"*.archimate
do
BN=$(basename "$i")
echo COPY "$BN"
cp "$i" "$BN"
git add "$BN"
git commit -m "update"
done

python merge.py
git add Kadaster-Repository.archimate
git commit -m "New Merged Repository"
git push
