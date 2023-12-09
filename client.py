import sys
import socket
import random

def display_map(raw, x, y):
    fieldsize={'x':31, 'y':21}
    for i in range(fieldsize["y"]):
        for j in range(fieldsize["x"] * 2):
            block = raw[i*fieldsize["x"]*2+j]

            if block == "o":
                block = "\033[31m" + block + "\033[0m"
            if block == "x":
                block = "\033[32m" + block + "\033[0m"

            if j == x * 2 and i == y:
                block = "\033[7m" + block

            print(block, end="")

        print()

def count_area(raw, x, y):
    fieldsize={'x':31, 'y':21}
    my_block = raw[y*fieldsize["x"]*2+x*2]
    opponent_block = "o" if my_block == "x" else "x"

    my_area = raw.count(my_block)
    opponent_area = raw.count(opponent_block)

    return my_area, opponent_area

def display_result(raw_map, x, y):
    print()
    print()
    print("End of game!!!")
    my_area, opponent_area = count_area(raw_map, x, y)

    print("Game result ...")
    print(f"Your painted area: {my_area}")
    print(f"Opponent player painted area: {opponent_area}")
    print()
    if my_area > opponent_area:
        print("!!!!! YOU WIN !!!!!")
    elif my_area == opponent_area:
        print("DRAW")
    else:
        print("..... YOU LOSE .....")

def operate(client, mode="player"):
    while True:
        print("Wait other player...")
        response = client.recv(buffer_size).decode()
        res_msgs = response.split(",")

        map_raw = res_msgs[0]
        can_behavior = res_msgs[1]
        have_item = int(res_msgs[4])
        player_x = int(res_msgs[5])
        player_y = int(res_msgs[6])

        is_end = int(res_msgs[7])
        if is_end:
            cli_msg = "0,0,0,1"
            client.send(cli_msg.encode())
            display_result(map_raw, player_x, player_y)
            break

        display_map(map_raw, player_x, player_y)

        behavior_list = ["w", "a", "d", "s"]
        while True:
            if mode == "player":
                print("Where to move?")
                dir = input("Select (w, a, s, d) = ")
                index = None
                try:
                    index = behavior_list.index(dir)
                except:
                    print("select w, a, s, d...")
                    continue

                if can_behavior[index] == "1":
                    cli_msg = behavior_list[index] + ","
                    break
                else:
                    print("Select direction is unavailable...")
            elif mode == "npc":
                index = random.randint(0, 3)
                if can_behavior[index] == "1":
                    cli_msg = behavior_list[index] + ","
                    break

        if have_item:
            if mode == "player":
                print("Use item ?")
                flag = ""
                while True:
                    flag = input("Select (0, 1) : ")
                    if flag == "0" or flag == "1":
                        break
                    else:
                        print("This input is unavailable...")
                cli_msg += flag + ","
            elif mode == "npc":
                cli_msg += str(random.randint(0, 1)) + ","
        else:
            cli_msg += "0" + ","
        cli_msg += "0,0"

        client.send(cli_msg.encode())


if __name__ == "__main__":
    args = sys.argv[1:]
    param = {
        "mode": "player",
        "server_ip": "127.0.0.1",
        "server_port": 8000
    }
    param_keys = list(param.keys())
    for i in range(len(args)):
        param[param_keys[i]] = args[i]

    if not (param["mode"] == "player" or param["mode"] == "npc"):
        raise

    buffer_size = 4096

    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_client.connect((param["server_ip"], param["server_port"]))

    operate(tcp_client, param["mode"])

    tcp_client.close()
