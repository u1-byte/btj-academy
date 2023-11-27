FROM python
COPY . .
EXPOSE 8081
CMD ["python", "prio_task.py"]
