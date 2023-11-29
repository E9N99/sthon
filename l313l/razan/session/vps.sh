STHON="\STHON USERBOT DEPLOY ON VPS"
STHON+="\n "
STHON+="\n "
STHON+="\n★ Channel: @VEEVVW ★"
STHON+="\n★ Support: @SEDTHON_help ★"
STHON+="\n "
ROZ="\n "
echo -e $STHON
echo -e $ROZ
echo "WAIT ..."
echo -e $ROZ

# Update and install dependencies  :)
sudo apt update && upgrade -y
sudo apt install postgresql postgresql-contrib
sudo apt install --no-install-recommends -y \
curl \
git \
libffi-dev \
libjpeg-dev \
libwebp-dev \
python3-lxml \
python3-psycopg2 \
libpq-dev \
libcurl4-openssl-dev \
libxml2-dev \
libxslt1-dev \
python3-pip \
python3-sqlalchemy \
openssl \
wget \
python3 \
python3-dev \
libreadline-dev \
libyaml-dev \
gcc \
zlib1g \
ffmpeg \
libssl-dev \
libgconf-2-4 \
libxi6 \
unzip \
libopus0 \
libopus-dev \
python3-venv \
libmagickwand-dev \
pv \
tree \
mediainfo \
nano \
nodejs
clear
echo "⚙️ Github Installer"
echo -e $ROZ
echo -e $STHON
echo -e $ROZ
echo "Cloning STHON Userbot"
echo -e $ROZ
git clone -b bro https://github.com/E9N99/STHON
echo -e $STHON
echo -e $ROZ
echo "runing STHON now"
echo -e $ROZ
cd STHON

# Rename sample_config.py to config.py
mv STHON.py config.py
echo "⚙️ Environment "
echo -e $ROZ

# Generate a random password  - باسوورد عشوائي لقاعدة البيانات   xD
PASSWORD=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)

# Connect to the PostgreSQL interactive terminal
sudo su - postgres -c "psql" <<EOF

ALTER USER postgres WITH PASSWORD '$PASSWORD';

CREATE DATABASE STHON;

\q
exit
EOF

# database
DATABASE_URL="postgresql://postgres:$PASSWORD@localhost:5432/jmthon"

# Ask the user for some environment variables and add them to .env
if [ ! -f .env ]; then
  touch .env
fi

echo "Enter your name:"
read alive_name
echo -e $ROZ
echo "Enter app id:"
read app_id
echo -e $ROZ
echo "Enter your api hash:"
read api_hash
echo -e $ROZ
echo "Enter your session:"
read session
echo -e $ROZ
echo "Enter your bot token:"
read token
echo -e $ROZ

echo "ALIVE_NAME=$alive_name" >> .env
echo "APP_ID=$app_id" >> .env
echo "API_HASH=$api_hash" >> .env
echo "STRING_SESSION=$session" >> .env
echo "TG_BOT_TOKEN=$token" >> .env
echo "DATABASE_URL=$DATABASE_URL" >> .env
clear
echo -e $STHON
echo -e $ROZ
