FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --upgrade streamlit

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]