FROM python:3.10.0
RUN useradd --create-home --shell /bin/bash app_user
WORKDIR /home/app_user
COPY setup.py ./
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY dice.py ./
RUN pip3 install .
USER app_user
CMD ["bash"]