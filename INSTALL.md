# Installer les dépendances Python
sudo apt update
sudo apt install python3-pip python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Installer MJPEG-Streamer 
sudo apt install subversion libjpeg-dev imagemagick libv4l-dev cmake
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
make
./mjpg_streamer -i "./input_uvc.so" -o "./output_http.so -w ./www"
