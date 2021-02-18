du -a|awk '{print $2'}|grep \.py|xargs python3 -m pycodestyle
