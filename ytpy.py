#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    from pytube import YouTube
    import time
    import os
    from colorama import Fore, Style
    vm_ex, vd_ex, cy_ex, a_ex, c_end = Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTYELLOW_EX, Style.RESET_ALL
except:
    from colorama import Fore, Style
    vm_ex, c_end = Fore.LIGHTRED_EX, Style.RESET_ALL
    print(f"{vm_ex}Pytube not installed\n Execute: pip3 install pytube{c_end}")
    raise SystemExit

def layout():
    print(f"""{cy_ex}
\t\t         _
\t\t   _   _| |_  ____  _   _
\t\t  | | | |  _)|  _ \| | | |
\t\t  | |_| | |__| | | | |_| |
\t\t   \__  |\___) ||_/ \__  |
\t\t  (____/     |_|   (____/
\n****************************************************************
\n*             {c_end}By: {vm_ex}Amarau and ferreiraklet 2021{c_end}                 {cy_ex}*{c_end}
\n{cy_ex}*{c_end}  Github --> {vm_ex}github.com/Amarauu & github.com/ferreiraklet{c_end}     {cy_ex}*{c_end}
\n{cy_ex}*{c_end}\t\t      {vm_ex}github.com/rodricbr{c_end}                      {cy_ex}*{c_end}
\n{cy_ex}****************************************************************
{c_end}""")


def inputt():
    try:
        ytvideo = str(input(f"{vm_ex}[+]{c_end} Video's txt: "))
        if ytvideo == 'exit':
            print(f'\n{vm_ex}Exiting... Bye!{c_end}')
            raise SystemExit
        video(ytvideo)
    except KeyboardInterrupt:
        print(f'\n\n{vm_ex}Exiting... Bye!{c_end}')

def video(video):
    videos_list = []
#os.system('cls' if os.name == 'nt' else 'clear'
    downloading_video()
    with open(f"{os.getcwd()}/{video}", "r") as file:
        file_data = file.readlines()
        start = time.time()

        for item in file_data:
            item = item.replace("\n", "")
            videos_list.append(item)
        cont = 0
        for valor in videos_list:
            cont += 1
            try:
                print(f"{a_ex}Downloading video{c_end} - [{cont}]  URL: {valor}")
                youtube = YouTube(valor)

                my_video = youtube.streams.get_highest_resolution()

                my_video.download()
            except Exception as e:
                print(str(e))
            except KeyboardInterrupt:
                print(f'\n\n{vm_ex}Exiting... Bye!{c_end}')
    end = time.time()
    duration = end - start
    print(f"\n{vd_ex}Downloaded with success!\nDuration:{c_end} {duration:.2f}\n")
    inputt()

#print("Title:  ", youtube.title)

def downloading_video():
    print(f"""{cy_ex}
 _____                    _                 _ _
(____ \                  | |               | (_)
 _   \ \ ___  _ _ _ ____ | | ___   ____  _ | |_ ____   ____
| |   | / _ \| | | |  _ \| |/ _ \ / _  |/ || | |  _ \ / _  |
| |__/ / |_| | | | | | | | | |_| ( ( | ( (_| | | | | ( ( | |
|_____/ \___/ \____|_| |_|_|\___/ \_||_|\____|_|_| |_|\_|| |
                                                     (_____|
{c_end}""")

layout()
inputt()
