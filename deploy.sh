#!/bin/sh
echo "Récupération du code par git..."
git fetch --all
git reset --hard origin/master
echo "Récupération terminée."
echo "Renommage du Loader sparks"
mv -f application/core/My_Loader.php application/core/MY_Loader.php
sed -i "s/[A-Z]:/kunden/g" htdocs/index.php