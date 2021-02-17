du | grep __pycache__|awk '{print $2}'|xargs rm -r
sudo rm -r dist/ yams.egg-info/ build/
