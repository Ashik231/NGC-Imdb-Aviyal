if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Ashik231/NGC-Imdb-Aviyal.git /NGC-Imdb-Aviyal
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /NGC-Imdb-Aviyal
fi
cd /NGC-Imdb-Aviyal
pip3 install -U -r requirements.txt
echo "Starting Cloning...."
python3 bot.py
