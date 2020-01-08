for i in "/v/IT/Architectuur/Domein Architectuur/Archi Repository/"*.archimate
do
BN=$(basename "$i")
echo COPY "$BN"
cp "$i" "$BN"
git add "$BN"
git commit -a -m "update"
git push
done

python merge.py
git add Kadaster-Repository.archimate
git push
