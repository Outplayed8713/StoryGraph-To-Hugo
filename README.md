## About
This is a quick and dirty weekend project I did that scrapes StoryGraph profiles and outputs a markdown file which can be read by Hugo the static site generator.

## Prerequisites:
1. Have a Public StoryGraph profile
  - This is necessary if you want to scrape your book reviews without being singed in.
  - By default profiles are only visible to other people with accounts, but this can be changed in your account settings.
2. Your website is created using Hugo, the static site generator
  - If you aren't, this script can be pretty easily modified to output whatever format.

## Steps:
1. Clone my [github repo](https://github.com/JackRaymondCyber/StoryGraph-To-Hugo)
2. Change "username" to your StoryGraph username on lines 3 of storygraph.bash
3. Run storygraph.py
4. Move books.md into your Hugo content directory
5. Either copy my style.css to your static directory or modify your own style.css
6. Make sure you are using the right theme in your Hugo config
7. Use the "hugo" command to generate your site
8. (Optional) Create a cron job which automatically runs the script then replaces your books.md on a set interval so your website auto updates with your StoryGraph profile


