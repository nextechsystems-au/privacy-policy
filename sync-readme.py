#!/usr/bin/env python3
"""Write README.md from PRIVACY.md.

⚠️ THIS EXISTS BECAUSE THE TWO DRIFTED, AND THE SERVED COPY WAS THE STALE ONE.

GitHub Pages USED to render README.md as this repo's index, so
https://nextechsystems-au.github.io/privacy-policy/ served README - NOT
PRIVACY.md, which is what the website syncs from and what everyone edits.
That site is now a redirect (index.html) and is being unpublished; the only
published policy is https://nextechsystems.com.au/privacy/.

Keep this script anyway. README is the first thing anyone opens in this repo,
and a README that disagrees with PRIVACY.md is how the wrong text gets copied
somewhere that does publish.

On 2026-09-01 they were 99 lines against 177. The published page was missing
the Play Games Services section, Farthest South, and - worst - BOTH Rursus
sections, including the only disclosure in the whole policy about content a
user typed leaving their device.

PRIVACY.md is the single source. README.md is generated. Run this after any
edit, before pushing:

    python3 sync-readme.py && git add -A && git commit && git push

Then re-run the website's sync too, or the third copy drifts instead:

    cd ~/repos/website && python3 sync-privacy.py && python3 build.py
"""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
SRC = HERE / 'PRIVACY.md'
DEST = HERE / 'README.md'

NOTE = (
    "<!-- GENERATED FROM PRIVACY.md by sync-readme.py - DO NOT EDIT.\n"
    "     GitHub Pages serves this file as the published policy, so an edit\n"
    "     made here and not in PRIVACY.md is a policy that disagrees with\n"
    "     itself in public. -->\n\n"
)


def main() -> int:
    if not SRC.exists():
        print(f'error: {SRC} missing', file=sys.stderr)
        return 1
    body = SRC.read_text(encoding='utf-8').rstrip() + '\n'
    DEST.write_text(NOTE + body, encoding='utf-8')
    print(f'README.md written from PRIVACY.md ({len(body.splitlines())} lines)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
