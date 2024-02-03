FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app


# Install any needed packages specified in requirements.txt
RUN pip3 install Flask
RUN pip3 install pymongo

# Make port 5001 available to the world outside this container
EXPOSE 5001

ENV MONGO_URI mongodb://localhost:27017

CMD ["python3", "-m","flask","run","--host=0.0.0.0"]