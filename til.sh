#!/bin/bash

CATEGORY=$1
TITLE=$2
SLUG=`echo $TITLE | iconv -t ascii//TRANSLIT | sed -E 's/[^a-zA-Z0-9]+/-/g' | sed -E 's/^-+|-+$//g' | tr A-Z a-z`
EXTENSION='.md'
FILENAME=$SLUG$EXTENSION

mkdir -p $CATEGORY
touch $CATEGORY/$FILENAME

echo -e "# $TITLE
" >> $CATEGORY/$FILENAME

open $CATEGORY/$FILENAME