FROM python:3.10.0
RUN useradd --create-home --shell /bin/bash app_user
WORKDIR /home/app_user
COPY setup.py ./
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY dice.py ./
RUN pip install .
USER app_user
CMD ["bash"]