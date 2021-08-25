FROM python:3.7

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

RUN apt-get install -yqq unzip
RUN wget https://chromedriver.storage.googleapis.com/2.32/chromedriver_linux64.zip &&\
      unzip chromedriver_linux64.zip &&\
      cp chromedriver /usr/sbin/

RUN pip install --upgrade pip
RUN pip install selenium behave

RUN mkdir packages
ADD ui-test-project /packages
WORKDIR /packages
RUN ls
RUN pip install -r requirements.txt
RUN behave
