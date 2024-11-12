FROM python:3.8-slim

#Set the working directory in the container
WORKDIR /app

#Copy requirements.txt into the container
COPY requirements.txt .

#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Copy the rest of the application files
COPY . .

#Expose the port (if needed for your app)
EXPOSE 3000

#Run the application
CMD ["python", "app/main.py"]