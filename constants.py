from typing import Final
import pandas as pd

TOKEN: Final[str] = "MTE0NDQzNTkzNjk5NDc4NzUyMg.GiinK-.yFOQVO-N_0LPq8RYwzL2dJjNNqk0OpAZ7HrwgE"
INVITE_LINK: Final[str] = "https://discord.com/api/oauth2/authorize?client_id=1144435936994787522&permissions=1084479764544&scope=bot"

USERS_SHEET_ID: Final[str] = "1oil8HEMqrJ0CBOAsNkK9rnYF93exh3B2LVsyebvcvFg"
SHEET_NAME = "problem-solving-users"
SHEET = f"https://docs.google.com/spreadsheets/d/{USERS_SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

sheet_data = pd.read_csv(SHEET)