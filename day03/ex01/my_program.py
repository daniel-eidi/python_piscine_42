from local_lib import path as p


def all_in():
    folder_path = "./newfolder"
    file = "teste.txt"
    p.Path(folder_path).mkdir_p()
    file = p.Path(folder_path + file)
    file.write_text("something")
    print(file.read_text())


if __name__ == "__main__":
    all_in()
