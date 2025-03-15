#!/bin/bash

# Подсчет общего количества запросов
total_requests=$(wc -l < access.log)

# Подсчет количества уникальных IP-адресов с использованием awk
unique_ips=$(awk '{print $1}' access.log | sort -u | wc -l)

# Подсчет количества запросов по методам
methods_count=$(awk '{print $6}' access.log | sort | uniq -c)

# Поиск самого популярного URL
popular_url=$(awk '{print $7}' access.log | sort | uniq -c | sort -nr | head -n 1)

# Создание отчета
{
  echo "Общее количество запросов: $total_requests"
  echo "Количество уникальных IP-адресов: $unique_ips"
  echo "Количество запросов по методам:"
  echo "$methods_count"
  echo "Самый популярный URL: $popular_url"
} > report.txt
