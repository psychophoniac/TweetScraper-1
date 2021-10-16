FROM python:3.7 as base

RUN useradd -m user

USER user
WORKDIR /home/user
COPY requirements.txt /home/user/
RUN pip install -r /home/user/requirements.txt
COPY src/* /home/user/

CMD ["python3", "main.py"]