#!/usr/bin/env python3
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from urllib.parse import quote

WB = "/home/user/writer/PlayChat_India_Competitor_Matrix.xlsx"
wb = openpyxl.load_workbook(WB)

# Remove existing sheet if re-running
for name in ("Ad Library & Social",):
    if name in wb.sheetnames:
        del wb[name]

ws = wb.create_sheet("Ad Library & Social")

def meta(q):
    """Meta (Facebook/Instagram) Ad Library — active ads in India for an advertiser keyword."""
    return ("https://www.facebook.com/ads/library/?active_status=active&ad_type=all"
            "&country=IN&media_type=all&search_type=keyword_unordered&q=" + quote(q))

def gads(domain=None):
    if domain:
        return "https://adstransparency.google.com/?region=IN&domain=" + domain
    return "https://adstransparency.google.com/?region=IN"

NA = ""  # blank = none / not applicable

# Each row: App, Company, India status, Meta Ad Library, Google Ads Transparency,
#           Facebook, Instagram, YouTube, TikTok, X/Twitter, LinkedIn, Website, Notes
rows = [
 # ---- HIGH / MEDIUM threat live platforms ----
 ["WePlay – Party Game & Chat","WEJOY Pte Ltd (SG)","Live",
  meta("WePlay Party Game"), gads("weplayapp.com"),
  "https://www.facebook.com/p/WePlay-Party-Game-100090407525014/", NA, NA, NA, NA, NA,
  "https://weplayapp.com/",
  "Global advertiser; switch Ad-Library country to 'All' to see full spend. Primary channel is FB/IG."],

 ["Yalla Ludo","Yalla Group (NYSE: YALA), Dubai","Live",
  meta("Yalla Ludo"), gads(),
  "https://www.facebook.com/yallaludogame/", "https://www.instagram.com/yallaludo_team/",
  "https://www.youtube.com/@Yallaludoplay", "https://www.tiktok.com/@yallaludo.official",
  NA, "https://www.linkedin.com/company/yalla-group/",
  "Heavy global paid social + influencer. Set Ad-Library country to 'All' for MENA/India creatives."],

 ["Plato: Fun Multiplayer Games","Plato Team Inc. (US)","Live",
  meta("Plato"), gads("platoapp.com"),
  NA, "https://www.instagram.com/platochat/", NA, NA, NA, NA,
  "https://platoapp.com/",
  "Positions as 'no ads' inside the app; runs little paid UA. Mostly organic IG."],

 ["Ludo King","Gametion Technologies (India)","Live",
  meta("Ludo King"), gads("ludoking.com"),
  "https://www.facebook.com/ludokinggame/", "https://www.instagram.com/ludokinggame/",
  "https://www.youtube.com/c/LudoKing", NA, "https://twitter.com/LudoKingGame", NA,
  "https://ludoking.com/",
  "Company page: facebook.com/gametiontech. Mostly brand/retention, low UA spend (maintenance mode)."],

 ["Blockman Go","Blockman GO Studio (Garena-backed)","Live",
  meta("Blockman Go"), gads(),
  "https://www.facebook.com/officialblockmango/", NA, NA,
  "https://www.tiktok.com/@blockmango", "https://x.com/blockmango", NA,
  "https://linktr.ee/BlockmanGo.Official",
  "All handles via Linktree. Heavy TikTok/YouTube influencer + paid social globally."],

 ["Zupee (Ludo by Zupee)","Cashgrail Pvt Ltd (India)","Live",
  meta("Zupee"), gads("zupee.com"),
  NA, "https://www.instagram.com/zupee_official/", NA, NA,
  "https://x.com/zupeeofficial", "https://www.linkedin.com/company/zupee/",
  "https://www.zupee.com/",
  "Also Telegram t.me/ZupeeOfficial. Large TV + digital spend historically; watch for post-ban shift."],

 ["WinZO","WinZO Pvt Ltd (India)","Live (crisis)",
  meta("WinZO"), gads("winzogames.com"),
  NA, "https://www.instagram.com/winzo_official/", NA, NA, NA,
  "https://www.linkedin.com/company/winzo-games/",
  "https://www.winzogames.com/",
  "US arm: instagram.com/winzo.us. Spend collapsed amid ED crisis; check Ad Library for live status."],

 ["YoHo: Group Voice Chat Room","Mico World Ltd (HK)","Live",
  meta("YoHo voice chat"), gads(),
  NA, NA, NA, NA, NA, NA,
  "https://yoho.media/",
  "Support cs@yoho.media. UA runs via Mico World; use Ad-Library country 'All' to surface creatives."],

 ["Ola Party – Live, Chat & Party","igo team (HK/SG)","Live (India = #1 market)",
  meta("Ola Party"), gads("olaparty.com"),
  NA, NA, NA, NA, NA, NA,
  "https://www.olaparty.com/",
  "India-first voice-room app. Contact olapartyservice@gmail.com. Check Meta Ad Library for IN creatives."],

 ["TopTop: Games & Chat","Mico World / Social Game Lab (HK)","Live (Gulf-focused)",
  meta("TopTop games chat"), gads(),
  NA, NA, NA, NA, NA, NA, NA,
  "MENA-centric; little India spend. Set Ad-Library country 'All'."],

 ["Litmatch","Construct Technology Pte Ltd (SG)","Live",
  meta("Litmatch"), gads(),
  NA, NA, NA, NA, NA, NA, NA,
  "Social-matching app; heavy TikTok/IG UA in Asia. Set country 'All'."],

 ["Lama – Game & Voice Chat","WeNext Ltd (HK)","Live (negligible India)",
  meta("Lama game voice"), gads(),
  NA, NA, NA, NA, NA, NA, NA,
  "Arabic-market Yalla clone."],

 ["STAN","STAN (Bengaluru)","Live",
  meta("STAN app"), gads("getstan.app"),
  NA, "https://www.instagram.com/getstan.app/", NA, NA, NA,
  "https://www.linkedin.com/company/getstan/",
  "https://getstan.app/",
  "Gaming-community app; UA around BGMI/Free Fire creators."],

 ["Qureka","CoolBoots Media (India)","Live (declining)",
  meta("Qureka"), gads("qureka.com"),
  NA, NA, NA, NA, NA, NA,
  "https://www.qureka.com/",
  "Known for ad-arbitrage; Qureka Lite B2B widget. Runs Google display/UAC ads."],

 ["JioGames","Jio Platforms (Reliance)","Live",
  meta("JioGames"), gads("jiogames.com"),
  NA, "https://www.instagram.com/jiogames/", "https://www.youtube.com/@JioGames", NA,
  "https://twitter.com/JioGames", NA,
  "https://www.jiogames.com/",
  "Distribution via Jio ecosystem; minimal external paid UA."],

 ["Gamezop","Advergame Technologies (India)","Live (B2B)",
  meta("Gamezop"), gads("gamezop.com"),
  NA, NA, NA, NA, NA, "https://www.linkedin.com/company/gamezop/",
  "https://www.gamezop.com/",
  "B2B aggregator — runs almost NO consumer UA; grows via 9,000+ partner embeds, not ads."],

 ["Ludo Talent","Spring Technology (BIGO/JOYY)","Live",
  meta("Ludo Talent"), gads(),
  NA, NA, NA, NA, NA, NA, NA,
  "Voice-ludo; UA via JOYY ad network."],

 ["Ludo Royal","Waha Technology FZ-LLC (Dubai)","Live",
  meta("Ludo Royal"), gads(),
  NA, NA, NA, NA, NA, NA, NA,
  "Voice-ludo niche; MENA-led spend."],

 ["Ludo Club","Moonfrog Labs (India, Stillfront)","Live",
  meta("Ludo Club"), gads(),
  "https://www.facebook.com/ludoclubgame/", NA, NA, NA, NA, NA,
  "https://www.moonfroglabs.com/",
  "Stillfront-owned; performance UA on Meta/Google."],

 ["Ludo Star","Gameberry Labs (India)","Live",
  meta("Ludo STAR"), gads(),
  "https://www.facebook.com/ludostargame/", NA, NA, NA, NA,
  "https://www.linkedin.com/company/gameberry-labs/",
  "https://gameberrylabs.com/",
  "Best-rated big ludo app; steady Meta/Google UA."],

 # ---- Notable game-level standalone competitors (Game-by-Game sheet) ----
 ["Carrom Pool / 8 Ball Pool","Miniclip (Zynga / Take-Two)","Live",
  meta("8 Ball Pool"), gads(),
  "https://www.facebook.com/miniclip", "https://www.instagram.com/8ballpool/",
  "https://www.youtube.com/@Miniclip", "https://www.tiktok.com/@8ballpool", NA, NA,
  "https://www.miniclip.com/",
  "Large global UA machine (Meta/Google/TikTok). See support.miniclip.com social channels."],

 ["Octro Tambola / Teen Patti","Octro Inc. (India)","Live",
  meta("Octro Tambola"), gads(),
  "https://www.facebook.com/octroteenpatti/", "https://www.instagram.com/octroteenpatti/",
  "https://www.youtube.com/c/Octroofficial", NA, "https://twitter.com/octroteenpatti", NA,
  "https://www.octro.com/",
  "Category leader for social tambola; active Meta + YouTube UA."],

 ["Stumble Guys","Scopely","Live (India = #1 downloads)",
  meta("Stumble Guys"), gads(),
  "https://www.facebook.com/StumbleGuysGame/", "https://www.instagram.com/stumbleguys/",
  NA, "https://www.tiktok.com/@stumbleguystt", NA, NA,
  "https://www.stumbleguys.com/",
  "Handles via linktr.ee/STGsocials. Massive TikTok/influencer + paid UA."],

 ["Worms Zone .io","Azur Games","Live",
  meta("Worms Zone"), gads(),
  "https://www.facebook.com/AzurGamesOfficial/", NA,
  "https://www.youtube.com/@AzurInteractive", NA, NA,
  "https://www.linkedin.com/company/azur-games/",
  "https://azurgames.com/",
  "Azur = one of the biggest hyper-casual advertisers; huge Meta/TikTok/Google volume."],

 ["Block Blast!","HungryStudio","Live",
  meta("Block Blast"), gads(),
  NA, NA, NA, "https://www.tiktok.com/tag/blockblast", NA, NA, NA,
  "#1 casual installs in India; very heavy Meta/TikTok/Google UA."],

 # ---- Dead / banned / exited — no active India advertising ----
 ["Hago","JOYY Inc.","BANNED (2020)",
  NA, NA, NA, NA, NA, NA, NA, NA, NA,
  "Banned in India — no legal ad presence. Still advertises in SEA/MENA/LatAm."],
 ["Chamet","Fuliao HK Ltd","REMOVED (2023)",
  NA, NA, NA, NA, NA, NA, NA, NA, NA,
  "Removed from Play India — no active India ads."],
 ["Eloelo → EloTV","Eloelo Group (India)","PIVOTED to micro-dramas",
  meta("EloTV"), gads(),
  NA, "https://www.instagram.com/elotv.official/", NA, NA, NA,
  "https://www.linkedin.com/company/eloelo/",
  "https://elotv.in/",
  "Exited social gaming; now advertises EloTV micro-dramas, not games."],
 ["Rush (Hike)","Hike","DEAD (Sep 2025)", NA,NA,NA,NA,NA,NA,NA,NA,NA,
  "Shut down — no ad presence."],
 ["MPL","Galactus Funware","EXITED India", NA,NA,NA,NA,NA,NA,NA,NA,
  "https://www.mpl.live/",
  "India ads stopped; advertises only in US/EU/Brazil now."],
 ["Hello Play","Flipkart","DEAD (2022)", NA,NA,NA,NA,NA,NA,NA,NA,NA,"Removed — no ad presence."],
 ["Bunch / MiniParty","Bunch Live Inc. (US)","Zombie", NA,NA,NA,NA,NA,NA,NA,NA,NA,"Faded — no active UA."],
 ["Poko","PokoGame / Huya","Dormant (delisted)", NA,NA,NA,NA,NA,NA,NA,NA,NA,"Delisted — no India ads."],
 ["Paytm First Games","One97 / Paytm","Dormant (exited RMG)", NA,NA,NA,NA,NA,NA,NA,NA,NA,"Exited gaming — no UA."],
]

headers = ["App","Company (HQ)","India Status","Meta Ad Library (India)","Google Ads Transparency (India)",
           "Facebook","Instagram","YouTube","TikTok","X / Twitter","LinkedIn","Website","Notes"]

# ---- Styling ----
title_font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
title_fill = PatternFill("solid", fgColor="1F4E78")
hdr_font = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
hdr_fill = PatternFill("solid", fgColor="2E75B6")
link_font = Font(name="Calibri", size=10, color="0563C1", underline="single")
txt_font = Font(name="Calibri", size=10)
note_font = Font(name="Calibri", size=9, italic=True, color="595959")
thin = Side(style="thin", color="D9D9D9")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
top_align = Alignment(vertical="top", wrap_text=True)

ncols = len(headers)

# Title row
ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
c = ws.cell(row=1, column=1, value="PlayChat — Competitor Ad Libraries & Social Presence (India, Aug 2026)")
c.font = title_font; c.fill = title_fill; c.alignment = Alignment(vertical="center", horizontal="left")
ws.row_dimensions[1].height = 24

# Subtitle / how-to row
ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncols)
sub = ("Meta Ad Library links open ACTIVE ads for that advertiser in India — inside, switch the Country dropdown to "
       "'All' to see global creatives. Google Ads Transparency links open the India region; if a domain filter shows "
       "nothing, clear it and type the advertiser name. Blank cell = no public page / not applicable.")
c = ws.cell(row=2, column=1, value=sub)
c.font = note_font; c.alignment = Alignment(vertical="center", wrap_text=True)
ws.row_dimensions[2].height = 42

# Header row
hr = 3
for j, h in enumerate(headers, start=1):
    cell = ws.cell(row=hr, column=j, value=h)
    cell.font = hdr_font; cell.fill = hdr_fill; cell.alignment = top_align; cell.border = border
ws.row_dimensions[hr].height = 30

link_cols = {4,5,6,7,8,9,10,11,12}  # columns holding URLs

def short_label(col, url):
    if not url:
        return ""
    if col == 4: return "▶ Meta Ad Library (IN)"
    if col == 5: return "▶ Google Ads (IN)"
    if col == 6: return "Facebook"
    if col == 7: return "Instagram"
    if col == 8: return "YouTube"
    if col == 9: return "TikTok"
    if col == 10: return "X / Twitter"
    if col == 11: return "LinkedIn"
    if col == 12: return url.replace("https://","").replace("http://","").rstrip("/")
    return url

r = hr + 1
for row in rows:
    for j, val in enumerate(row, start=1):
        cell = ws.cell(row=r, column=j)
        cell.border = border; cell.alignment = top_align
        if j in link_cols and val:
            cell.value = short_label(j, val)
            cell.hyperlink = val
            cell.font = link_font
        elif j == ncols:  # notes
            cell.value = val; cell.font = note_font
        else:
            cell.value = val; cell.font = txt_font
    # zebra striping
    if (r - hr) % 2 == 0:
        for j in range(1, ncols+1):
            if ws.cell(row=r, column=j).fill.fgColor.rgb in (None,"00000000"):
                ws.cell(row=r, column=j).fill = PatternFill("solid", fgColor="F2F7FC")
    r += 1

# Column widths
widths = [26,26,20,22,20,16,16,14,14,14,14,30,46]
from openpyxl.utils import get_column_letter
for j, w in enumerate(widths, start=1):
    ws.column_dimensions[get_column_letter(j)].width = w

ws.freeze_panes = "A4"
ws.sheet_view.showGridLines = False

# Move the new sheet right after Platform Competitors
order = wb.sheetnames
if "Platform Competitors" in order:
    wb.move_sheet("Ad Library & Social", offset=-(len(order)-1-order.index("Platform Competitors")-1))

wb.save(WB)
print("Saved. Sheets:", wb.sheetnames)
print("Data rows added:", len(rows))
