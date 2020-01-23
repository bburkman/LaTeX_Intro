#!/bin/sh

arg=${1:-.}

exts="aux bbl blg brf fdb_latexmk fls idx ilg ind lof log lol lot nav out snm toc synctex.gz"

if [ -d $arg ]; then
for ext in $exts; do
         rm -f $arg/*.$ext
done
else
for ext in $exts; do
         rm -f $arg.$ext
done
fi
