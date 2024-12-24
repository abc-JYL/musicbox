import os
import time

from pygame import mixer


def load_music(filename):
    music = []
    with open(filename, "r") as f:
        for line in f:
            line = line.split(';')[0].strip()
            if line:
                music.extend(line.split())
    return music


def play(note):
    file_path = f"samples/{note}.mp3"
    if os.path.isfile(file_path):
        mixer.Sound(file_path).play()
    else:
        print(f"[ERROR] Not such of file {note}.mp3")
        exit(1)


def a_wait(delay, sustain, fadeout):
    if delay < 0:
        while mixer.get_busy():
            time.sleep(0.1)
    else:
        wait(delay, sustain, fadeout)


def wait(t, sustain, fadeout):
    time.sleep(t)
    if not sustain:
        mixer.fadeout(fadeout)


def run(music):
    a_sync = False
    sustain = False
    in_loop = False
    loop = 0
    loop_i = 0
    loop_stack = []
    fadeout = 500
    delay = -1
    i = 0
    music_len = len(music)

    while i < music_len:
        part = music[i]
        if part.startswith('.'):
            command = part[1:]

            # Handle .async
            if command == "async":
                if a_sync:
                    raise RuntimeError("[ERROR] Nested Async!")
                a_sync = True

            # Handle .end
            elif command == "end":
                if not in_loop and not a_sync:
                    raise RuntimeError("[ERROR] .end Out Of Scope!")
                elif a_sync:
                    a_sync = False
                elif loop > 0:
                    loop -= 1
                    i = loop_i
                    continue
                elif loop < 0:
                    i = loop_i
                    continue
                elif loop_stack:
                    in_loop, loop_i, loop = loop_stack.pop()
                    in_loop = True

            # Handle .await
            elif command == "await":
                a_wait(delay, sustain, fadeout)

            # Handle .wait
            elif command == "wait":
                wait(float(music[i + 1]), sustain, fadeout)
                i += 1

            # Handle .play
            elif command == "play":
                i += 1
                while music[i] != ".end":
                    note = music[i]
                    if note == "-":
                        a_wait(delay, sustain, fadeout)
                    else:
                        play(note)
                        if not a_sync:
                            a_wait(delay, sustain, fadeout)
                    i += 1

            # Handle .delay
            elif command == "delay":
                delay = float(music[i + 1])
                i += 1

            # Handle .nodelay
            elif command == "nodelay":
                delay = -1

            # Handle .sustain
            elif command == "sustain":
                sustain = True

            # Handle .nosustain
            elif command == "nosustain":
                sustain = False

            # Handle .fadeout
            elif command == "fadeout":
                fadeout = int(music[i + 1])
                i += 1

            # Handle .loop
            elif command == "loop":
                if in_loop:
                    loop_stack.append((in_loop, loop_i, loop))
                in_loop = True
                loop = int(music[i + 1]) - 1
                i += 2
                loop_i = i
                continue

            else:
                raise SyntaxError(f"[ERROR] Syntax error! {part}")

        else:
            raise SyntaxError(f"[ERROR] Syntax error! {part}")

        i += 1


if __name__ == "__main__":
    mixer.init()
    mixer.set_num_channels(32)
    music = load_music("jingle.m")
    run(music)
