import re

# Функция для извлечения текста между "prompt" и "raw"
def extract_text(data):
    pattern = r'"prompt":"(.*?)","raw"'
    matches = re.findall(pattern, data)
    return matches

# Список файлов для обработки
files_to_process = [
    "C:\\Users\\79819\\Documents\\logi_edit\\application-2023-11-03.log.58",
    "C:\\Users\\79819\\Documents\\logi_edit\\application-2023-11-07.log",
]

for file_path in files_to_process:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            file_content = file.read()
            extracted_text = extract_text(file_content)
            
            # Запись извлеченного текста в файл
            output_file = "_output.txt"
            with open(output_file, "w", encoding="utf-8") as output:
                for text in extracted_text:
                    output.write(text + "\n")
    except Exception as e:
        print(f"Ошибка при обработке файла {file_path}: {str(e)}")

# Функция для удаления повторяющихся строк из файла
def remove_duplicates(input_file, output_file):
    lines_seen = set()  # Множество для хранения уникальных строк
    with open(output_file, "w", encoding="utf-8") as output:
        with open(input_file, "r", encoding="utf-8") as file:
            for line in file:
                if line not in lines_seen:
                    output.write(line)
                    lines_seen.add(line)

# Указать файл для обработки и файл, в который будет записан результат
input_file = "_output.txt"  # Замените на свой файл
output_file = "output.txt"  # Замените на имя файла для вывода

remove_duplicates(input_file, output_file)
