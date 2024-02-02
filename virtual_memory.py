frames = 5
page_order = []

def virtual_memory(frames):
    return [None] * frames

result = virtual_memory(frames)

def page_allocation(page):
    global frames,page_order,result
    if result:
        if len(page_order) < frames:
            result[len(page_order)] = page
            page_order.append(page)
        else:
            evicted_page = page_order.pop(0)
            index = result.index(evicted_page)
            result[index] = page
            page_order.append(page)
    else:
        print("Please create a memory before using it")

def page_access(page_number):
    global result
    try:
        print(f"In {page_number} index located {result[page_number-1]}")
    except IndexError:
        print("There is no such a page")

def display_status():
    global result
    for index,page in enumerate(result):
        if page == None:
            print(f"{index+1} is empty = {page}")
        elif page:
            print(f"{index+1} is full = {page}")

def main():
    flag = True
    while flag:
        print("Virtual Memory")
        print("1. To create a memory: ")
        print("2. To change data in memory: ")
        print("3. To access memory: ")
        print("4. To show the status of memory: ")

        command = input(">>> ")
        if command == "1":
            virtual_memory(frames)
        if command == "2":
            page = input("Value: ")
            page_allocation(page)
        if command == "3":
            page_number = int(input("Which index: "))
            page_access(page_number)
        if command == "4":
            display_status()

main()