from Node import Node
from Algorithm import Algorithm
import os
import traceback
import copy
import platform

title = "DUISC Decision Maths"
sub_title = "Maximum Solver"
author_copyright = "Yuhao Li 2019"
sys_clear = "CLS"

if platform.system() != "Windows":
    sys_clear = "clear"

def print_node_intial_match(parent_set, child_set):
    a_info = ""
    b_info = ""
    a_type = ""
    a = []
    b = []

    if len(parent_set) > len(child_set):
        a = parent_set
        b = child_set
        a_type = "parent"
    else:
        a = child_set
        b = parent_set
        a_type = "child"

    print("+-----------------------------------------------------+ +--------------------------+")
    print("|{:^26s}|{:^26s}| |{:^26s}|".format(
        "Parents", "Matched Children", "Available Children"))
    print("+-----------------------------------------------------+ +--------------------------+")
    for i in range(len(a)):
        parent_info = ""
        child_info = ""
        matched_info = ""
        connected_node = None

        a_info = str(i+1) + ". " + a[i].name
        if i < len(b) and len(b) > 0:
            b_info = str(i+1) + ". " + b[i].name
        else:
            b_info = ""

        if a_type is "parent":
            parent_info = a_info
            child_info = b_info
            connected_node = a[i].get_connected_node()

        else:
            parent_info = b_info
            child_info = a_info
            connected_node = b[i].get_connected_node()

        matched_info = str(connected_node.get_index()+1)+". " + \
            connected_node.name if connected_node is not None else ""

        print("|{:^26s}|{:^26s}| |{:^26s}|".format(
            parent_info, matched_info, child_info))

    print("+-----------------------------------------------------+ +--------------------------+")


def print_parent_avilablity(parent_set, child_set):
    a_info = ""
    b_info = ""
    a_type = ""
    a = []
    b = []

    if len(parent_set) > len(child_set):
        a = parent_set
        b = child_set
        a_type = "parent"
    else:
        a = child_set
        b = parent_set
        a_type = "child"

    print("+---------------------------------------------------------------------------+ +--------------------------+")
    print("|{:^26s}|{:^48s}| |{:^26s}|".format(
        "Parents", "Available Set", "Children"))
    print("+---------------------------------------------------------------------------+ +--------------------------+")
    for i in range(len(a)):
        parent_info = ""
        child_info = ""
        avail_set_info = ""

        a_info = str(i+1) + ". " + a[i].name
        if i < len(b) and len(b) > 0:
            b_info = str(i+1) + ". " + b[i].name
        else:
            b_info = ""

        if a_type is "parent":
            parent_info = a_info
            child_info = b_info
            avail_set_info = a[i].get_available_set_str()
        else:
            parent_info = b_info
            child_info = a_info
            avail_set_info = b[i].get_available_set_str()

        print("|{:^26s}|{:^48s}| |{:^26s}|".format(
            parent_info, avail_set_info, child_info))

    print("+---------------------------------------------------------------------------+ +--------------------------+")


def print_nodes(parent_set, child_set):
    a_info = ""
    b_info = ""
    a_type = ""
    a = []
    b = []

    if len(parent_set) > len(child_set):
        a = parent_set
        b = child_set
        a_type = "parent"
    else:
        a = child_set
        b = parent_set
        a_type = "child"

    print("+-----------------------------------------------------+")
    print("|{:^26s}|{:^26s}|".format("All Parents", "All Children"))
    print("+-----------------------------------------------------+")
    for i in range(len(a)):
        parent_info = ""
        child_info = ""
        a_info = str(i+1) + ". " + a[i].name
        if i < len(b) and len(b) > 0:
            b_info = str(i+1) + ". " + b[i].name
        else:
            b_info = ""

        if a_type is "parent":
            parent_info = a_info
            child_info = b_info
        else:
            parent_info = b_info
            child_info = a_info

        print("|{:^26s}|{:^26s}|".format(parent_info, child_info))

    if len(a) is 0 and len(b) is 0:
        print("|{:^26s}|{:^26s}|".format("", ""))

    print("+-----------------------------------------------------+\n")


def print_result_nodes(res_parent_set, im_parent_set):
    os.system(sys_clear)
    print(title)
    print(sub_title)
    print(author_copyright+"\n")
    print("+----------------------+{:32s}+---------------------+".format(""))
    print("|   Initial Matching   |{:32s}|   Solved Matching   |".format(""))
    print("+-----------------------------------------------------+ +-----------------------------------------------------+")
    print("|{:^26s}|{:^26s}| |{:^26s}|{:^26s}|".format(
        "Parents", "Matched Children", "Parents", "Matched Children"))
    print("+-----------------------------------------------------+ +-----------------------------------------------------+")

    for i in range(len(res_parent_set)):
        initial_parent = im_parent_set[i]
        res_parent = res_parent_set[i]
        res_connected_child = res_parent.get_connected_node()
        inital_matched_info = ""
        inital_connected_child = initial_parent.get_connected_node()
        parent_info = str(i+1) + ". " + res_parent.name

        if inital_connected_child is not None:
            inital_matched_info = str(
                inital_connected_child.get_index()+1) + ". " + inital_connected_child.name

        res_matched_info = str(
            res_connected_child.get_index()+1) + ". " + res_connected_child.name
        print("|{:^26s}|{:^26s}| |{:^26s}|{:^26s}|".format(
            parent_info, inital_matched_info, parent_info, res_matched_info))
    print("+-----------------------------------------------------+ +-----------------------------------------------------+\n")
    input("Result printed, press any key to continue")


def main_menu():
    os.system(sys_clear)
    print(title)
    print(sub_title)
    print(author_copyright+"\n")
    print("1. Edit Node")
    print("2. Set Availablity")
    print("3. Set Initial Match")
    print("4. Calculate")
    print("\n{:^6s} -- {:^6s}\n".format("Q / q", "Quit"))


def edit_node_menu(parent_set, child_set):
    os.system(sys_clear)
    print(title)
    print(sub_title)
    print(author_copyright+"\n")
    print_nodes(parent_set, child_set)
    print("\n1. Add parents")
    print("2. Add childs")
    print("3. Remove a parent")
    print("4. Remove a child")
    print("5. Remove all parents")
    print("6. Remove all children")
    print("\n{:^6s} -- {:^6s}\n".format("Q / q", "Quit"))


def set_availablity_menu(parent_set, child_set):
    os.system(sys_clear)
    print(title)
    print(sub_title)
    print(author_copyright+"\n")
    print_parent_avilablity(parent_set, child_set)
    print("\n{:^6s} -- {:^6s}".format("Enter", "Pass"))
    print("{:^6s} -- {:^6s}\n".format("Q / q", "Quit"))


def set_initial_match_menu(parent_set, child_set):
    os.system(sys_clear)
    print(title)
    print(sub_title)
    print(author_copyright+"\n")
    print_node_intial_match(parent_set, child_set)
    print("\n{:^6s} -- {:^6s}".format("Enter", "Pass"))
    print("{:^6s} -- {:^6s}\n".format("Q / q", "Quit"))


def edit_node():
    case_1_option = ""
    while True:
        try:
            parent_set = Node.parent_set
            child_set = Node.child_set
            edit_node_menu(parent_set, child_set)
            case_1_option = input("Option: ")
            if case_1_option is "1":
                names = input("Parents name: ").split(",")
                for name in names:
                    temp = Node("parent", name)
                    temp.set_index(Node.parent_set.index(temp))
            elif case_1_option is "2":
                names = input("Childs name: ").split(",")
                for name in names:
                    temp = Node("child", name)
                    temp.set_index(Node.child_set.index(temp))
            elif case_1_option is "3":
                index = input("Parent index: ")
                Node.remove_from_list(parent_set[int(index)-1])
            elif case_1_option is "4":
                index = input("Child index: ")
                Node.remove_from_list(child_set[int(index)-1])
            elif case_1_option is "5":
                Node.remove_all("parent")
            elif case_1_option is "6":
                Node.remove_all("child")
            elif case_1_option is "":
                pass
            elif case_1_option is "q" or case_1_option is "Q":
                if len(parent_set) is not len(child_set):
                    print(
                        "The number of parents and children did not match, do you intend to leave?")
                    exit_selection = input("Y/N: ")
                    if exit_selection is 'Y' or exit_selection is 'y':
                        return False
                    else:
                        edit_node_menu(parent_set, child_set)
                else:
                    return True
        except:
            print(traceback.format_exc())


def is_availablities_set(parent_set):
    for node in parent_set:
        if len(node.get_available_set()) is 0:
            return False

    return True


def set_single_availablity(parent, parent_set, child_set):
    try:
        avail_set = []
        set_availablity_menu(parent_set, child_set)
        ele_index = input(
            "Input the index of child for \"{:s}\": ".format(parent.name))
        if ele_index is "q" or ele_index is "Q":
            return "q"
        elif ele_index is "":
            pass
        else:
            ele_index_list = ele_index.split(",")
            for index in ele_index_list:
                avail_set.append(child_set[int(index)-1])
            parent.set_availablity(avail_set)
            set_availablity_menu(parent_set, child_set)
        return "c"
    except:
        avail_set = []
        parent.set_availablity(avail_set)
        set_availablity_menu(parent_set, child_set)
        set_single_availablity(parent, parent_set, child_set)


def set_all_availablities():
    parent_set = Node.parent_set
    child_set = Node.child_set
    return_code = ""
    i = 0
    while return_code is not "q" and i < len(parent_set):
        node = parent_set[i]
        return_code = set_single_availablity(node, parent_set, child_set)
        i += 1
    if is_availablities_set(parent_set):
        input("Availablity has set, press any key to continue")
        return True
    else:
        print("Availabilities not complete, Do you intend to leave?")
        exit_selection = input("Y/N: ")
        if exit_selection is "Y" or exit_selection is "y":
            return False
        else:
            set_all_availablities()


def set_single_initial_match(node, parent_set, child_set):
    try:
        initial_match_set = []
        set_initial_match_menu(parent_set, child_set)
        child_index = input(
            "Input the index of child for \"{:s}\": ".format(node.name))
        if child_index is "q" or child_index is "Q":
            return "q"
        elif child_index is "":
            pass
        else:
            child_index = int(child_index) - 1
            child = child_set[child_index]
            node.add_child(child)
            initial_match_set = set_initial_match_menu(parent_set, child_set)
        return "c"
    except:
        print(traceback.format_exc())
        input()
        set_initial_match_menu(parent_set, child_set)
        set_single_initial_match(node, parent_set, child_set)


def set_all_initial_match():
    parent_set = Node.parent_set
    child_set = Node.child_set
    return_code = ""
    initial_match_set = []
    i = 0
    while return_code is not "q" and i < len(parent_set):
        node = parent_set[i]
        return_code = set_single_initial_match(node, parent_set, child_set)
        i += 1

    if return_code is not "q":
        input("Matching initialised, press any key to continue")

    return True, Node.parent_set, Node.child_set


def main():
    input_option = ""
    im_parent_set = []
    im_child_set = []
    res_parent_set = []
    case_1_complete = False
    case_2_complete = False
    case_3_complete = False
    case_4_complete = False
    case_4_count = 0
    while input_option is not "q" and input_option is not "Q":
        try:
            main_menu()
            input_option = input("Option: ")

            if input_option is "1":
                case_1_complete = edit_node()
                case_4_complete = False
            elif input_option is "2":
                if case_1_complete:
                    case_2_complete = set_all_availablities()
                    case_4_complete = False
                else:
                    input(
                        "Option 1 : Edit Node is not complete, press any key to continue")
            elif input_option is "3":
                if case_1_complete:
                    case_3_complete, tp_parent_set, tp_child_set = set_all_initial_match()
                    im_parent_set = copy.deepcopy(tp_parent_set)
                    im_child_set = copy.deepcopy(tp_child_set)
                    case_4_complete = False
                else:
                    input(
                        "Option 1 : Edit Node is not complete, press any key to continue")
            elif input_option is "4":
                if not case_1_complete:
                    input(
                        "Option 1 : Edit Node is not complete, press any key to continue")
                elif not case_2_complete:
                    input(
                        "Option 2 : Set Availablity is not complete, press any key to continue")
                elif not case_3_complete:
                    input(
                        "Option 3 : Set Initial Match is not complete, press any key to continue")
                else:
                    algo = Algorithm(Node.parent_set)
                    cal_res = algo.execute()
                    case_4_complete = True
                    case_4_count += 1
                    print_result_nodes(cal_res, im_parent_set)

                    Node.parent_set = im_parent_set
                    Node.child_set = im_child_set

            elif input_option is "":
                pass
            elif input_option is "q" or input_option is "Q":
                print("Exit the programme...")
        except:
            print(traceback.format_exc())
            input()


if __name__ == "__main__":
    main()
