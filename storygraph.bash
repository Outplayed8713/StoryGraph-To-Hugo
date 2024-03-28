#!/bin/bash -e

username="username"
i=1
read_url="https://app.thestorygraph.com/books-read/$username?page="
review_url="https://app.thestorygraph.com/user_reviews/$username?page="
page_titles="not empty"

while [ -n "$page_titles" ]; do
	page=$(curl "$read_url$i")
	page_titles=$(echo "$page" | grep "img alt" | grep --invert-match StoryGraph | awk 'NR%2==1' | cut -d'"' -f2 | sed "s/&#39;/'/g")
	page_imgs=$(echo "$page" | grep "img alt" | grep --invert-match StoryGraph | awk 'NR%2==1' | cut -d'"' -f6)
	page_genres=$(echo "$page" | grep --after-context=10 "my-1" | awk -F '>' '/--/{i++; printf "\n"}; /span>$/ && ((i%2)==0){printf "%s ", $2}' | sed 's/<\/span//g' | awk '!(($0==""))')
	if [ -n "$page_titles" ]; then
		genres+="$page_genres"$'\n'
		titles+="$page_titles"$'\n'
		imgs+="$page_imgs"$'\n'
	fi
	i=$((i + 1))
done

i=1
page_reviews="not empty"
while [ -n "$page_reviews" ]; do
	page=$(curl "$review_url$i")
	page_reviews=$(echo "$page" | awk '/\/books|icon-star/{print $0}; /review-explanation/{getline; printf "Review: %s\n", $0}' | awk -F '>' '/\/books/{printf "Title:%s\n", $2}; /^Review/{printf "%s\n", $0} /svg/{printf "Stars: %s\n", $1}' | awk '/Stars/{print $1 " " $2}; /Title:|Review:/{print $0}' | sed 's/          //g' | sed 's/<\/a//g' | sed "s/&#39;/\'/g" | sed 's/..div>/ /g' | awk -F ':' '/Title:/{printf "\n%s |",$2}; /Stars: /{printf "%s |", $2}; /^Review:/{for(i=2;i<=NF;++i)printf "%s", $i}' | awk '!(($0==""))')

	if [ -n "$page_reviews" ]; then
		reviews+="$page_reviews"$'\n'
	fi
	i=$((i + 1))
done

readarray -t titles <<<"${titles}"
readarray -t imgs <<<"${imgs}"
readarray -t genres <<<"${genres}"
readarray -t reviews <<<"${reviews}"
printf '%s\n' "${titles[@]}" >titles
printf '%s\n' "${imgs[@]}" >imgs
printf '%s\n' "${genres[@]}" >genres
printf '%s\n' "${reviews[@]}" >reviews
