# basic_python_project

Si tu fais un clique droit "Open Preview" c'est plus agréable à lire.

## VS Code extension

Material Icon Theme (pour les fichiers et dossiers)
(si jamais c'est possible de synchroniser les extensions avec VS Code pour avoir les mêmes sur tous tes ordis dans les réglages)

## Créer un environnement

conda create -n yourenvname python=x.x

## Commencer à travailler

conda activate yourenvname

git pull origin main

pip install -r requirements.txt

## Quand t'as fini de bosser

Save all your files

pip freeze > requirements.txt

git add --all

git commit -m "your comment"

git push origin main
