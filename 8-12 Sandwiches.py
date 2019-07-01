def sandwiches(*body):
    """
    :param body: list of items that will go into a sandwich
    :return: a summary of the sandwich being ordered
    """
    print("The sandwich will have the following: ")
    for items in body:
        print(f"\t{items.title()}")

sandwiches("eggs", "jam", "ham")