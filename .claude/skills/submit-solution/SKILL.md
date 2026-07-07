---
name: submit-solution
description: |
  Place a written solution in the correct folder with the correct filename, then commit and push to main. Use when the user says to "submit", "save this solution", "file this", or gives a solution and says it's a leetcode/exponent problem.
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
---

# Submit Solution

Take a solution the user has written, place it at the correct path, then commit and push to `main`.

## 1. Get the solution

The solution is either:
- Pasted/typed in the message, or
- Already sitting in a scratch/wrong location the user points to.

If it's ambiguous which code is "the solution", ask before proceeding.

## 2. Decide the destination

Two categories, based on what the user says:

**LeetCode problem** → `leetcode/<number>.py`
- The user gives a problem number (e.g. "leetcode 3754", "it's 1365").
- Filename is exactly that number: `leetcode/3754.py`.
- These files typically use the LeetCode `class Solution:` shape.

**Exponent problem** → `exponent/<function_name>.py`
- The user says it's an "exponent" problem.
- Filename is the name of the primary function defined in the solution (the `def <name>(...)`), in snake_case as written. E.g. a solution defining `def two_sum(...)` → `exponent/two_sum.py`.
- If multiple functions exist, use the top-level solution function (the one the problem asks for), not helpers.
- Determine the function name by reading the code, not by guessing from the description.

If the user hasn't said which category it is, ask. Don't assume.

## 3. Write the file

- Write the solution to the resolved path (create it, or overwrite if the user is updating an existing solution).
- If the target already exists and this isn't an explicit update, tell the user it exists and confirm before overwriting.

## 4. Commit and push to main

Run from the repo root (`/Users/devesh/Desktop/Coding/leetcodeExponent`):

```bash
git add <the file>
git commit -m "<concise message>"
git push origin main
```

Commit message convention: short and descriptive, e.g.
- `add leetcode 3754` / `solve leetcode 1365`
- `add exponent two_sum` / `solve exponent merge_intervals`

Stage only the solution file — don't sweep in unrelated changes. After pushing, report the final path and confirm the push succeeded.
