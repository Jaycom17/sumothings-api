FROM alpine:3.14

# Install required packages
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python3", "src/index.py"]