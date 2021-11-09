def get_menus() -> dict:
    menus = dict()
    menus['main_menu'] = {
        "options": '''[Programming Books]\n1) Add a book\n2) View all books\n3) Search for a book\n4) Book Analysis\n5) Exit''',
        "start": 1,
        "end": 5
    }
    return menus
#end
def get_option(options:str, start:int, end:int) -> int:
    print(options)
    option = input("Please provide your option within({}, {}): ".format(start, end))
    while not option.isdigit() or int(option) < start or int(option) > end:
        option = input("Invalid range. Please provide your option within({}, {}): ".format(start, end))
    return int(option)
def build_message():
    pass
def build_option():
    pass
def view_option():
    pass
