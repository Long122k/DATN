# # ENTRYPOINT [ "scrapy", "crawl", "hotel_info", "-o", "data2.json" ]
# Base image
FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3.8 \
    python3-pip \
    curl \
    unzip \
    wget \
    gnupg

# Install Chrome
RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y google-chrome-stable

# Install ChromeDriver
RUN CHROME_VERSION=$(google-chrome-stable --version | awk '{print $NF}' | cut -d '.' -f 1) \
    && wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_VERSION})/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin \
    && rm /tmp/chromedriver.zip

# Set up Chrome for running in a container
RUN groupadd -r chrome && useradd -r -g chrome -G audio,video chrome \
    && mkdir -p /home/chrome && chown -R chrome:chrome /home/chrome \
    && mkdir -p /data && chown -R chrome:chrome /data \
    && sed -i 's/"$HERE\/chrome"/"$HERE\/chrome" --no-sandbox/g' /opt/google/chrome/google-chrome

# Set Python 3.8 as the default Python version
RUN ln -s /usr/bin/python3.8 /usr/bin/python

# Set the working directory
WORKDIR /hotel_data

# Copy your Python file to the container
COPY . .

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Run the Python command to execute your file

CMD ["tail", "-f", "/dev/null"]
