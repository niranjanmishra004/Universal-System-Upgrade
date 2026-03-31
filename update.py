#!/usr/bin/env python3

import os
import platform
import shutil
import subprocess
import sys
import time
import threading

# ===== COLORS =====
RESET = "\033[0m"
BOLD = "\033[1m"

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"

# ===== SPINNER =====
spinner_running = False

def spinner():
    global spinner_running
    while spinner_running:
        for cursor in "|/-\\":
            sys.stdout.write(f"\r{CYAN}{cursor} Processing...{RESET}")
            sys.stdout.flush()
            time.sleep(0.1)

def start_spinner():
    global spinner_running
    spinner_running = True
    t = threading.Thread(target=spinner)
    t.start()
    return t

def stop_spinner(thread):
    global spinner_running
    spinner_running = False
    thread.join()
    sys.stdout.write("\r")  # clear line


# ===== ORIGINAL FUNCTIONS (UNCHANGED LOGIC) =====

def read_os_release(path="/etc/os-release"):
    metadata = {}
    if not os.path.exists(path):
        return metadata

    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            metadata[key] = value.strip().strip('"')
    return metadata


def detect_platform():
    system = platform.system().lower()
    if system == "linux":
        os_release = read_os_release()
        distro_id = os_release.get("ID", "").lower()
        distro_like = os_release.get("ID_LIKE", "").lower()

        if not distro_id:
            if os.path.exists("/etc/arch-release"):
                distro_id = "arch"
            elif os.path.exists("/etc/debian_version"):
                distro_id = "debian"

        return "linux", distro_id, distro_like

    if system == "darwin":
        return "macos", "", ""

    if system == "windows":
        return "windows", "", ""

    return system, "", ""


def get_linux_family(distro_id, distro_like):
    debian_ids = {"debian", "ubuntu", "linuxmint", "elementary", "pop", "kali", "raspbian"}
    arch_ids = {"arch", "manjaro", "artix", "endeavouros"}
    rhel_ids = {"rhel", "centos", "fedora", "rocky", "almalinux", "oracle", "amazon", "scientific"}

    if distro_id in arch_ids or any(item in distro_like for item in arch_ids):
        return "arch"
    if distro_id in rhel_ids or any(item in distro_like for item in rhel_ids):
        return "rhel"
    if distro_id in debian_ids or any(item in distro_like for item in debian_ids):
        return "debian"
    return "other"


def get_update_commands():
    os_type, distro_id, distro_like = detect_platform()

    if os_type == "linux":
        family = get_linux_family(distro_id, distro_like)

        if family == "arch":
            return [
                ("sudo pacman -Syu --noconfirm", "Update and upgrade packages with pacman"),
                ("sudo pacman -Sc --noconfirm", "Clean pacman cache"),
            ]

        if family == "debian":
            return [
                ("sudo apt update", "Update package lists"),
                ("sudo apt upgrade -y", "Upgrade packages"),
                ("sudo apt autoremove -y", "Auto-remove unused packages"),
                ("sudo apt autoclean -y", "Clean package cache"),
            ]

        if family == "rhel":
            if shutil.which("dnf"):
                return [
                    ("sudo dnf upgrade -y", "Upgrade packages with dnf"),
                    ("sudo dnf autoremove -y", "Auto-remove unused packages with dnf"),
                    ("sudo dnf clean all", "Clean dnf cache"),
                ]
            return [
                ("sudo yum update -y", "Update packages with yum"),
                ("sudo yum autoremove -y", "Auto-remove unused packages with yum"),
                ("sudo yum clean all", "Clean yum cache"),
            ]

        raise RuntimeError("Unsupported Linux distribution")

    if os_type == "macos":
        if shutil.which("brew"):
            return [
                ("brew update", "Update Homebrew"),
                ("brew upgrade", "Upgrade Homebrew packages"),
                ("brew cleanup", "Clean Homebrew cache"),
            ]
        return [("sudo softwareupdate --install --all", "Install macOS updates")]

    if os_type == "windows":
        if shutil.which("winget"):
            return [("winget upgrade --all --silent", "Upgrade all packages with winget")]
        if shutil.which("choco"):
            return [("choco upgrade all -y", "Upgrade with Chocolatey")]

    raise RuntimeError("Unsupported OS")


# ===== ENHANCED OUTPUT =====

def run_command(cmd, description):
    print(f"\n{MAGENTA}{'='*60}{RESET}")
    print(f"{BOLD}{YELLOW}⚡ {description}{RESET}")
    print(f"{MAGENTA}{'='*60}{RESET}")

    spinner_thread = start_spinner()

    try:
        subprocess.run(cmd, shell=True, check=True)
        stop_spinner(spinner_thread)
        print(f"{GREEN}✔ SUCCESS:{RESET} {description}")
    except subprocess.CalledProcessError as error:
        stop_spinner(spinner_thread)
        print(f"{RED}✖ FAILED:{RESET} {description}")
        print(f"{RED}{error}{RESET}")
        sys.exit(1)


def main():
    print(f"{CYAN}{BOLD}\n🚀 System Update Automation Script{RESET}\n")
    username = os.getlogin()
    print(f"{GREEN}{BOLD}Hello {username}")


    os_type, distro_id, distro_like = detect_platform()

    print(f"{GREEN}Detected Platform:{RESET} {os_type}")

    if os_type == "linux":
        print(f"{GREEN}Distro:{RESET} {distro_id or 'unknown'} ({distro_like or 'unknown'})")

    try:
        commands = get_update_commands()
    except RuntimeError as error:
        print(f"{RED}Error:{RESET} {error}")
        sys.exit(1)

    print(f"\n{CYAN}Starting updates...{RESET}")

    for command, description in commands:
        run_command(command, description)

    print(f"\n{GREEN}{BOLD}✔ All operations completed successfully!{RESET}\n")


if __name__ == "__main__":
    main()
