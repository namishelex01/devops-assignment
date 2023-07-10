FROM python:3.9

WORKDIR /weather_app

# Create a non-root user
RUN groupadd -r o_user && useradd -r -g o_group o_user

# Copy only the files to dir
COPY weather.py .
COPY requirements.txt .

RUN chown -R o_user:o_group /weather_app
RUN chmod 755 /weather_app

USER o_user

# Install the dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python3", "weather.py"]
