from fake_useragent import UserAgent

header = {'User-Agent': UserAgent().random}

teams = {
    "челси": "547-chelsi",
    "манчестер юнайтед": "546-manchester-junajted",
    "манчестер сити": "602-manchester-siti"
}

def getUrl(club: str) -> str:
    return f"https://www.championat.com/tags/{teams[club]}/news/"