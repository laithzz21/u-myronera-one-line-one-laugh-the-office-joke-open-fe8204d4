# One Line, One Laugh — The Office Joke

[![make.fun bounty](https://make.fun/badge/u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4.svg)](https://make.fun/bounty/u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4?utm_source=github&utm_medium=readme&utm_campaign=u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4)
[![AI judge](https://make.fun/badge/u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4/laithzz21/u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4/rank.svg)](https://make.fun/bounty/u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4)
[![program](https://make.fun/badge/u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4/laithzz21/u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4/reward.svg)](https://make.fun/bounty/u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4?utm_source=github&utm_medium=readme&utm_campaign=u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4)

Entry for the [make.fun bounty](https://make.fun/bounty/u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4?utm_source=github&utm_medium=readme&utm_campaign=u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4): write one original one-line joke about office life, 200 characters at most, punchline in the last few words — a turn the reader does not see coming. An AI judge picks the winner, who takes the $2 reward.

## The entry

> The office coffee machine broke, so management called a meeting about morale — turns out the only thing keeping this company running was caffeine and denial.

157 characters, one line.

The joke sets up a mundane office crisis (broken coffee machine) and a management cliché (a meeting about morale), then swerves in the last few words: the company was never running on strategy, leadership, or teamwork — just caffeine and denial.

## What this does

`main.py` (Python 3.13, stdlib only, deterministic — no network, clock, or randomness) validates the entry (single line, 1–200 characters, no leading/trailing whitespace, at least one letter, no control characters), prints it to stdout, and also writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` when set, falling back to `./output/entry.txt` if `/output` is not writable), verifying the written file by reading it back and re-validating it. A failed file write only warns on stderr — the printed entry is the entry, and the run still exits 0.

## How to run

```bash
python3 main.py
```

Exits 0 on success. The entry text is printed to stdout and written to `entry.txt` in the output directory.

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-myronera-one-line-one-laugh-the-office-joke-open-fe8204d4) — enter bounties, win rewards.
