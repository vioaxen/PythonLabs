url = "https://www.muctr.ru/university/departments/vus/student/file.txt"

site = "mysite.ru"
path = url.split("//")[-1]

site_and_path = path.split("/", 1)
root_folder_and_file = "/" + site_and_path[1]

root_folder = root_folder_and_file.rsplit("/", 1)[0]
file_name_with_ext = root_folder_and_file.rsplit("/", 1)[-1]

file_name = file_name_with_ext.split(".")[0].upper()

print("Адрес сайта:", site)
print("Корневая папка:", root_folder)
print("Имя файла без расширения:", file_name)