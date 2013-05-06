#!/bin/sh
echo "Récupération du code par git..."
git pull
echo "Récupération terminée."
echo "Renommage du Loader sparks"
mv application/core/My_Loader.php application/core/MY_Loader.php

export file=htdocs/index.php
sed -e "s/'[A-Z]:\\.+codeigniter\/(['^]+)'/'/kunden/homepages/43/d383453256/htdocs/hadrienmp/$1'/g" "$file" > "$file".tmp && mv -f "$file".tmp "$file"
