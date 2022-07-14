# 
FROM python:3.9-slim

# 
COPY ./src /app/src
# 
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

# 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 8000

# 
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0"]
