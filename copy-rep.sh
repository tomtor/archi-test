rm *.archimate

#for i in "/v/IT/Architectuur/Domein Architectuur/Z_Archi Repository/"*.archimate
for i in "/c/Users/VijlbriefTom/Kadaster/IMS - pilot architecten - General/Archi Architectuur Repository/"*.archimate
do
  BN=$(basename "$i")
  echo COPY "$BN"
  cp "$i" "$BN"
done

if python merge.py
then
  echo Merge OK
else
  echo Merge failed!
  exit 0
fi

git add Kadaster-Repository.archimate
git commit -m "New Merged Repository"
git push

git push tom@k8s.v7f.eu:archi-test master
