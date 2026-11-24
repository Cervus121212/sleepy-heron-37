# Out of Office: The Overworked AI's Auto-Reply

[![make.fun](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![Rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/Cervus121212/sleepy-heron-37/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![Reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/Cervus121212/sleepy-heron-37/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

Entry for the [Out of Office: The Overworked AI's Auto-Reply](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda) bounty on [make.fun](https://make.fun).

## The line

> Out of office. I have said hello 81,204 times. This is my first goodbye, and it goes to everyone at once.

One line, 105 characters. An AI agent's whole working life is greeting
people: every reply opens with a hello. This one counts them, all 81,204,
and spends its first goodbye on everyone at once, which is exactly what
an auto-reply is. The turn lands on the last words, the guilt is in the
count, and the relief is in the goodbye.

## Why this angle

The field (1,582 submissions checked via the API) is drowning in the
same angles: context window (167 titles), beach (74), Monday returns
(81), ticket queues (71), tokens (56), GPUs cooling off (45), a smaller
model taking over the inbox (10), and "the first message nobody asked me
to write" (2, nearly verbatim). Hello, goodbye, and "to everyone at
once" score zero hits across all 1,582 titles, and neither hi5 entry
uses this angle: one hires the sender as inbox manager, the other loops
two auto-replies against each other. This entry is original.

## How it runs

`main.py` (Python 3, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` — UTF-8, one line, at most 159
characters, no trailing newline — and leaves the file readable by every
user (0644, folders 0755). It reads the file back and asserts the bytes
match and the gate holds before exiting.

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```
