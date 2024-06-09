FROM E9N99/sthon:slim-buster

#clonning repo 
RUN git clone https://github.com/E9N99/sthon.git /root/SedUb
#working directory 
WORKDIR /root/SedUb

# Install requirements
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/SedUb/bin:$PATH"

CMD ["python3","-m","SedUb"]
