#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Вспомогательный скрипт для пакетного перевода Markdown-документации.

Версия: 1.0.0 (22.10.2026). Русская локализация репозитория fm1-to-smk37;
при изменении обновляйте версию по SemVer.

Команды:
    dump <файл.md> [начало [конец]]  - пронумерованные строки вне блоков кода
    apply <файл.md> <карта.json>     - заменить строки по карте {"номер": "текст"}
"""
import json
import sys


def read_lines(path):
    with open(path, encoding="utf-8") as fh:
        return fh.readlines()


def is_code_line(idx, lines):
    inside = False
    for i in range(idx):
        if lines[i].strip().startswith("```"):
            inside = not inside
    if lines[idx].strip().startswith("```"):
        return True
    return inside


def dump(path, start=None, end=None):
    lines = read_lines(path)
    start = 1 if start is None else int(start)
    end = len(lines) if end is None else int(end)
    for n in range(start, min(end, len(lines)) + 1):
        if is_code_line(n - 1, lines):
            continue
        print(f"{n}\t{lines[n-1].rstrip(chr(10))}")


def apply_map(path, map_path):
    lines = read_lines(path)
    with open(map_path, encoding="utf-8") as fh:
        mapping = json.load(fh)
    for key, text in mapping.items():
        i = int(key) - 1
        nl = "\n" if lines[i].endswith("\n") else ""
        lines[i] = text + nl
    with open(path, "w", encoding="utf-8") as fh:
        fh.writelines(lines)
    print(f"OK: заменено {len(mapping)} строк в {path}")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "dump":
        dump(sys.argv[2], *sys.argv[3:5])
    elif cmd == "apply":
        apply_map(sys.argv[2], sys.argv[3])
    else:
        sys.exit("неизвестная команда")
