def open_text_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return None


def string_processing(line):
    if "Jupyter" in line:
        return line.replace("SDK	Jupyter-", "").strip()


def main():
    new_lines = []
    file_name = "蝦皮購物網/App4AI清單.txt"
    lines = open_text_file(file_name)
    if lines is None:
        print("File not found")
    else:
        for line in lines:
            if string_processing(line):
                new_lines.append(string_processing(line))

    with open("蝦皮購物網/App4AI清單_new.txt", "w", encoding="utf-8") as f:
        for line in new_lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
