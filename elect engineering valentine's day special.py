import os
import sys
import time
import random

# Try to use figlet; if not installed, we fallback gracefully
try:
    from pyfiglet import Figlet
    HAS_FIGLET = True
except Exception:
    HAS_FIGLET = False


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def typewriter(text, delay=0.03, end="\n"):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()


def beep(freq=880, dur_ms=140):
    """
    Windows: real tone via winsound.
    Mac/Linux: terminal bell fallback.
    """
    try:
        if os.name == "nt":
            import winsound
            winsound.Beep(int(freq), int(dur_ms))
        else:
            sys.stdout.write("\a")
            sys.stdout.flush()
            time.sleep(dur_ms / 1000)
    except Exception:
        time.sleep(dur_ms / 1000)


def countdown():
    for n in [3, 2, 1]:
        typewriter(f"{n}...", 0.06)
        beep(650 + n * 90, 160)
        time.sleep(0.25)
    typewriter("LIVE! ⚡\n", 0.05)
    beep(1200, 220)


def progress_bar(label="Synchronizing signals", length=34, seconds=2.2):
    start = time.time()
    last_bucket = -1
    while True:
        pct = min((time.time() - start) / seconds, 1.0)
        filled = int(length * pct)
        bar = "█" * filled + "░" * (length - filled)

        bucket = int(pct * 10)
        if bucket != last_bucket and bucket > 0:
            beep(720 + bucket * 12, 60)
            last_bucket = bucket

        sys.stdout.write(f"\r{label}: [{bar}] {int(pct*100):3d}%")
        sys.stdout.flush()
        if pct >= 1.0:
            break
        time.sleep(0.02)
    print()
    beep(988, 140)
    beep(1175, 160)


def pulse_bolt(pulses=8, speed=0.14):
    frame1 = r"""
           ⚡
          ⚡⚡
         ⚡⚡⚡
        ⚡⚡⚡⚡
          ⚡⚡
           ⚡
    """
    frame2 = r"""
          ⚡⚡
         ⚡⚡⚡
        ⚡⚡⚡⚡
       ⚡⚡⚡⚡⚡
         ⚡⚡⚡
          ⚡⚡
    """
    for i in range(pulses):
        clear()
        print(frame1 if i % 2 == 0 else frame2)
        beep(660 if i % 2 == 0 else 520, 80)
        time.sleep(speed)


def confetti(lines=12, width=80):
    symbols = list("*+x@#$%&!?~")
    for _ in range(lines):
        row = "".join(random.choice(symbols) if random.random() < 0.18 else " " for _ in range(width))
        print(row)
        if random.random() < 0.30:
            beep(random.choice([988, 1175, 1319]), 50)
        time.sleep(0.05)


def figlet_print(text, font="slant"):
    if HAS_FIGLET:
        f = Figlet(font=font)
        print(f.renderText(text))
    else:
        # fallback: still looks clean
        print("=" * (len(text) + 8))
        print(f"   {text}")
        print("=" * (len(text) + 8))


def main():
    clear()

    # 🎬 Intro
    typewriter("Welcome: Society of Electrical & Electronics Engineering ⚡", 0.04)
    typewriter("Valentine Special Transmission Initializing...\n", 0.03)
    countdown()

    typewriter(">>> scanning for active Engineers...", 0.03)
    time.sleep(0.2)
    typewriter(">>> detecting heart frequency...", 0.03)
    time.sleep(0.2)
    typewriter(">>> calibrating emotional circuits...\n", 0.03)
    time.sleep(0.2)

    progress_bar("Stabilizing love voltage", length=36, seconds=2.3)

    typewriter("\nSystem status:", 0.02)
    typewriter(" - Voltage: steady ⚡", 0.02); beep(784, 70)
    typewriter(" - Current: flowing 💡", 0.02); beep(880, 70)
    typewriter(" - Signal strength: strong 💘", 0.02); beep(988, 90)
    time.sleep(0.5)

    pulse_bolt(pulses=6, speed=0.14)

    # 🏁 BIG VALENTINE MESSAGE
    clear()

    if HAS_FIGLET:
        f_big = Figlet(font="slant")
        print(f_big.renderText("Happy Valentine's Day"))
        time.sleep(0.5)

        f_name = Figlet(font="big")
        print(f_name.renderText("Engineer"))
    else:
        print("\nHAPPY VALENTINE'S DAY ENGINEER\n")

    time.sleep(0.5)

    # Small credit (intentionally small)
    print("\n" + "-" * 40)
    print("   created by Heritage")
    print("-" * 40 + "\n")


    typewriter("⚡ Stay charged. Stay inspired. Stay brilliant. ⚡", 0.03)
    beep(784, 120); beep(988, 140); beep(1175, 180)

if __name__ == "__main__":
    main()
