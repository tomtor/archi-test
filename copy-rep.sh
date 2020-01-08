for i in "/v/IT/Architectuur/Domein Architectuur/Archi Repository/"*.archimate
do
BN=$(basename "$i")
cp "$i" "$BN"
git add "$BN"
git commit -a -m "update"
git push
done
