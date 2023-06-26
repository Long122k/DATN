# Use an appropriate base image with Python installed
# FROM python:3.8


# # Set the working directory in the container
# WORKDIR /hotel_data

# # Copy the contents of the tripAdvisor folder to the working directory in the container
# COPY . .

# # Install any required dependencies
# RUN pip install -r requirements.txt
# # RUN apt-get update -y && apt-get install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1
# RUN apt-get update \
#     && apt-get install -y chromium

# # Set the entry point command to run your Python script
# CMD ["tail", "-f", "/dev/null"]
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
