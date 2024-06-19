from pathlib import Path


def write_employees_to_file(content, path):
    fn = open(path, 'w')
    for i in content:
        if type(i) is list:
            for j in i:
                fn.write(j + "\n")
        else:
            fn.write(i + "\n")
    fn.close()
# program for task!


def get_recipe(path, search_id):
    my_dict = None
    with open(path, 'r') as f:
        for line in f:
            l = line.strip().split(",")
            if l[0] == search_id:
                my_dict = {'id': l[0], 'name': l[1], 'ingredients': l[2:]}
                break
    return (my_dict)


# end of program for task!


content = ["60b90c1c13067a15887e1ae1,Herbed Baked Salmon,4 lemons,1 large red onion,2 tablespoons chopped fresh basil",
           "60b90c2413067a15887e1ae2,Lemon Pancakes,2 tablespoons baking powder,1 cup vanilla-flavored almond milk,1 lemon",
           "60b90c2e13067a15887e1ae3,Chicken and Cold Noodles,6 ounces dry Chinese noodles,1 tablespoon sesame oil,3 tablespoons soy sauce",
           "60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese",
           "60b90c4613067a15887e1ae5,State Fair Lemonade,6 lemons,1 cups white sugar,5 cups cold water"]

write_employees_to_file(content, 'test.txt')

print(get_recipe('test.txt', "60b90c3b13067a15887e1ae4"))

# with open('test.txt', 'r') as f:
#     print(f.read())


# удаляем файл
Path('test.txt').unlink()
