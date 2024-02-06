def get_cats_info(path):
    cats_list = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_data = line.strip().split(",")
                if len(cat_data) == 3:
                    cat_info = {
                        "id": cat_data[0],
                        "name": cat_data[1],
                        "age": cat_data[2],
                    }
                    cats_list.append(cat_info)
                else:
                    print(f"Invalid data format in line: {line}")

    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return cats_list


cats_info = get_cats_info("cats_file.txt")
for cat in cats_info:
    print(f"id: {cat['id']}, name: {cat['name']}, age: {cat['age']}")
