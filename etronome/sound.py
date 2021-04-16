import subprocess


def play_sound(sound_file: str) -> None:
    subprocess.Popen(['aplay', '-q', sound_file])
