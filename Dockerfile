FROM kivy/buildozer:latest

# Install additional dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip3 install --no-cache-dir \
    flet==0.26.0 \
    requests \
    python-dateutil \
    pillow \
    'flet[all]==0.26.0'

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Build APK
CMD buildozer android debug
