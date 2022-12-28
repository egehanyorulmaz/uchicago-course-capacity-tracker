FROM python:3.8-slim
WORKDIR "/usr/"

# Install system dependencies
RUN apt-get update && apt-get install -yq libgconf-2-4 && apt-get install -yq gnupg && apt-get install -yq wget
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub
# RUN apt-key add -
# RUN echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list
RUN apt update -y
RUN apt install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils

# Chromium must be compatible with chrome version
RUN apt-get install -y chromium unzip

RUN wget -q "https://chromedriver.storage.googleapis.com/108.0.5359.22/chromedriver_linux64.zip" -O /tmp/chromedriver.zip
RUN unzip /tmp/chromedriver.zip -d /usr/local/bin/
RUN ls -al /usr/local/bin/

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /helpers
COPY helpers/parsing.py ./helpers/parsing.py
COPY helpers/utils.py ./helpers/utils.py

RUN mkdir /config
COPY config/credentials.py ./config/credentials.py

COPY curriculum_tracker.py .

# Run the web scraper when the container is started
CMD ["python", "curriculum_tracker.py"]


### docker container run -it my-scraper /bin/bash