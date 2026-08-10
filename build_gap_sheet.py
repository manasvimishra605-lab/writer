#!/usr/bin/env python3
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from urllib.parse import quote

WB = "/home/user/writer/PlayChat_India_Competitor_Matrix.xlsx"
wb = openpyxl.load_workbook(WB)

SHEET = "Gap Analysis — Additions"
if SHEET in wb.sheetnames:
    del wb[SHEET]
ws = wb.create_sheet(SHEET)

def meta(q):
    return ("https://www.facebook.com/ads/library/?active_status=active&ad_type=all"
            "&country=IN&media_type=all&search_type=keyword_unordered&q=" + quote(q))

# ---------- content ----------
# 7 cols: Name | Owner/Company (HQ) | Type / Genre | India Scale & Status |
#         Social features & Overlap with PlayChat | Threat / Verdict | Notes & Links (url)
FORMAT = [
 ["FRND: Chat, Play, Connect","Cold Brew Tech (Bengaluru, India)","Voice-first social + live mini-games",
  "50M+ installs; ~1M/mo; live & growing",
  "Voice/video rooms behind avatars, in-app games, Hindi/Tamil/Telugu/Punjabi/Kannada — the closest Indian analog to PlayChat's games+chat+companion mix",
  "HIGH — biggest miss",
  meta("FRND")],
 ["Yalla (main app)","Yalla Group (NYSE: YALA), Dubai","Voice rooms + multi-game platform",
  "100M+ globally; live in India",
  "Voice rooms + Ludo, Carrom, UNO, Baloot, Quiz Master, gifting — broader than 'Yalla Ludo' already in the matrix; direct games+voice overlap",
  "HIGH",
  meta("Yalla voice chat")],
 ["Bigo Live","BIGO / JOYY Inc. (SG/China)","Live streaming + voice rooms + mini-games",
  "Large India user base; live",
  "Multi-guest voice rooms (up to 12), in-room mini-games, PK battles, heavy gifting economy — competes for the same voice-room spenders",
  "MEDIUM-HIGH",
  meta("Bigo Live")],
 ["StarMaker / StarChat","StarMaker Inc. (Shenzhen/US)","Karaoke social + voice rooms + games",
  "50M+ users; strong India base",
  "Live rooms, duets, in-room games, virtual gifting — audio-first but same social-gifting monetization play",
  "MEDIUM",
  meta("StarMaker")],
 ["Discord","Discord Inc. (US)","Gaming communities + voice",
  "~38M India users; 90% use it to play games",
  "Servers, persistent voice channels, Activities (in-app games). Owns the social layer for engaged Indian gamers — not casual-desi, but the deepest games+chat graph",
  "MEDIUM (social axis)",
  "https://discord.com/"],
 ["Rooter","Rooter (Threesixteen Tech, Delhi)","Game streaming + esports",
  "~70M installs; ~18M MAU; India's #1",
  "Streaming, reels, creator clubs — attention/community competitor, not a play-together app; overlaps STAN's positioning",
  "LOW-MEDIUM",
  meta("Rooter")],
 ["Tango Live","Tango.me (US/Cyprus)","Live video/voice + gifting",
  "Live in India",
  "1:many broadcasts, voice rooms, gifting — voice-social spender competitor",
  "LOW-MEDIUM",
  "https://www.tango.me/"],
 ["Poppo Live / POPO Live","Baitu / Skylive (China)","Live voice/video rooms + gifting",
  "~43M installs; India support presence",
  "Topic-based multi-user voice/video rooms, gifting — thin games, same voice-room audience",
  "LOW",
  meta("Poppo Live")],
 ["Uplive","Asia Innovations Group (SG/HK)","Live social + gifting",
  "Live; Asia-heavy",
  "Live rooms, PK, gifting; minimal games — voice-social spender overlap only",
  "LOW",
  meta("Uplive")],
 ["Dostt","Indian startup","Voice/video friendship + support",
  "Live; India languages",
  "FRND-style voice/video with verified listeners; games light — companion-axis competitor",
  "LOW-MEDIUM",
  meta("Dostt app")],
 ["RealFrnd","RealFrnd (India)","Audio/video friendship + communities",
  "Live; India-first",
  "Real-time audio/video, communities — FRND-style companion competitor",
  "LOW",
  "https://realfrnd.com/"],
 ["Yubo","Yubo (France)","Teen live social + swipe",
  "Live; weak India traction",
  "Live streaming, group chat, swipe-match — teen (13-25) skew vs PlayChat's casual-desi",
  "LOW",
  meta("Yubo")],
 ["Moj / ShareChat / Josh / Chingari","ShareChat, DailyHunt, etc. (India)","Short-video social",
  "100M+ each (India)",
  "Not games, but the same regional-language attention pool the micro-drama pivots (EloTV/ZO TV) chase — indirect time competitor",
  "CONTEXT (attention, not play)",
  ""],
]

GENRE = [
 ["Fruit Merge / Suika (watermelon)","Watermelon/Suika clones (ArtwayStudio, FrozenLogic, codematics...)","In PlayChat catalog (Read Me) — NOT in 23-game matrix",
  "Many 1M–10M+ clones; fragmented",
  "All single-player, ads-first, ZERO social/multiplayer",
  "WHITESPACE — add a social version",
  ""],
 ["Match-3 (Candy-Crush style)","Candy Crush Saga (King/Microsoft), Gardenscapes (Playrix)","Genre PlayChat likely has; not mapped",
  "1B+ (Candy Crush); huge in India",
  "Single-player, async teams at most; no live social",
  "FORTRESS genre — bundle value only, don't fight standalone",
  ""],
 ["Bubble Shooter","Bubble Shooter (Ilyon), Bubble Witch (King)","Not in matrix",
  "100M+; massive casual base",
  "Single-player, no social",
  "WHITESPACE for a social/multiplayer version",
  ""],
 ["Solitaire","Solitaire (MobilityWare/Brainium), MS Solitaire","Not in matrix",
  "500M+ combined; steady India base",
  "Single-player, no social",
  "WHITESPACE (social solitaire almost non-existent)",
  ""],
 ["Sudoku","Sudoku.com (Easybrain, 100M+)","Not in matrix",
  "100M+; strong India puzzle base",
  "Single-player; async events only",
  "WHITESPACE for social/duel sudoku",
  ""],
 ["Word games (connect / search / crossword)","Words of Wonders (Zynga), Word Connect, WordCookies","Not in matrix",
  "Tens of millions; popular in India",
  "Single-player; no live chat",
  "WHITESPACE for multiplayer/vernacular word games",
  ""],
 ["Chess","Chess.com (100M+), Lichess, Chess Universe","Not in matrix",
  "Very large post-2023 India chess boom",
  "Chess.com/Lichess ALREADY have clubs, chat, live play",
  "CONTESTED — incumbents own social chess; differentiate on casual-desi bundle",
  "https://www.chess.com/"],
 ["UNO / card (crazy-eights)","UNO!™ (Mattel163, 100M+); many clones","Yalla/YoHo bundle it; not in matrix",
  "100M+ (UNO!)",
  "UNO! has rooms + voice + gifting already",
  "CONTESTED but fits the voice-room bundle — add UNO-style card game",
  meta("UNO game")],
 ["Social deduction (Mafia / Werewolf / Among Us)","Among Us (InnerSloth, 500M+); WePlay 'Space Werewolf'","Party format; not in matrix",
  "500M+ (Among Us); big India teen base",
  "Among Us & WePlay have voice/text — this is a VOICE-ROOM-native format",
  "STRONG FIT — natural for PlayChat's voice rooms; add Mafia/Werewolf",
  ""],
 ["Draw & Guess (Pictionary)","Skribbl.io, Gartic, Draw & Guess; WePlay built-in","Party format; not in matrix",
  "Browser-dominant; few strong mobile apps",
  "Inherently social; almost no polished India mobile app",
  "WHITESPACE — chat-native draw-&-guess",
  "https://skribbl.io/"],
 ["Hand cricket / casual cricket","Hitwicket, Real Cricket (Nautilus), WCC (Nextwave), Cricket League (Miniclip)","Cricket not in matrix",
  "15M+ (Hitwicket); tens of M across titles",
  "Mostly sim/strategy; hand-cricket finger-game apps are tiny & social-less",
  "WHITESPACE for social hand-cricket; sim cricket is contested",
  ""],
 ["Antakshari / music-guess","(Eloelo had it, now vacated)","Very Indian; not in matrix",
  "No scaled owner post-Eloelo pivot",
  "Voice-room-native format with no live incumbent",
  "WHITESPACE — strong voice-room fit",
  ""],
 ["Fruit Ninja / slice arcade","Fruit Ninja (Halfbrick, 1B+)","Not in matrix",
  "1B+; nostalgic India base",
  "Single-player",
  "Low priority; single-player fortress",
  ""],
 ["Bowling / Archery / Basketball minis","Fragmented clones","Arcade minis; not in matrix",
  "Small, fragmented",
  "No social leaders",
  "Minor whitespace — bundle filler",
  ""],
 ["Bingo","= Tambola (already in matrix, Octro leader)","Already covered",
  "See tambola row",
  "Octro has voice tables",
  "COVERED — no new action",
  ""],
]

# ---------- styling ----------
title_font = Font(size=14, bold=True, color="FFFFFF")
title_fill = PatternFill("solid", fgColor="1F4E78")
band_font  = Font(size=11, bold=True, color="FFFFFF")
bandA_fill = PatternFill("solid", fgColor="C55A11")   # orange = platforms/format
bandB_fill = PatternFill("solid", fgColor="548235")   # green  = games/genres
hdr_font   = Font(size=10, bold=True, color="FFFFFF")
hdr_fill   = PatternFill("solid", fgColor="404040")
txt_font   = Font(size=10)
link_font  = Font(size=10, color="0563C1", underline="single")
note_font  = Font(size=9, italic=True, color="595959")
thin = Side(style="thin", color="D9D9D9")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
top = Alignment(vertical="top", wrap_text=True)

NCOL = 7
headers = ["Name","Owner / Company (HQ)","Type / Genre","India Scale & Status",
           "Social Features & Overlap with PlayChat","Threat / Verdict","Notes & Links"]

def set_row(r, values, section):
    for j, v in enumerate(values, start=1):
        cell = ws.cell(row=r, column=j); cell.border = border; cell.alignment = top
        if j == NCOL and v:
            if v.startswith("http"):
                label = "▶ Meta Ad Library (IN)" if "ads/library" in v else v.replace("https://","").rstrip("/")
                cell.value = label; cell.hyperlink = v; cell.font = link_font
            else:
                cell.value = v; cell.font = note_font
        elif j == 6:
            cell.value = v; cell.font = Font(size=10, bold=True,
                color="C55A11" if section=="A" else "548235")
        else:
            cell.value = v; cell.font = txt_font

r = 1
# Title
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=NCOL)
c = ws.cell(row=r, column=1, value="Gap Analysis — Competitors & Genres NOT in the original matrix (India, Aug 2026)")
c.font = title_font; c.fill = title_fill; c.alignment = Alignment(vertical="center")
ws.row_dimensions[r].height = 24; r += 1

ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=NCOL)
c = ws.cell(row=r, column=1, value="Answer: yes — two whole layers were missing. SECTION A = format/platform competitors (voice-room, live-social, community apps). SECTION B = game genres in PlayChat's 100+ catalog that the 23-game matrix never mapped. Meta Ad Library links open active India ads (switch Country to 'All' for global).")
c.font = note_font; c.alignment = Alignment(vertical="center", wrap_text=True)
ws.row_dimensions[r].height = 42; r += 1

def band(text, fill):
    global r
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=NCOL)
    c = ws.cell(row=r, column=1, value=text); c.font = band_font; c.fill = fill
    c.alignment = Alignment(vertical="center"); ws.row_dimensions[r].height = 20; r += 1

def header_row():
    global r
    for j, h in enumerate(headers, start=1):
        cell = ws.cell(row=r, column=j, value=h)
        cell.font = hdr_font; cell.fill = hdr_fill; cell.alignment = top; cell.border = border
    ws.row_dimensions[r].height = 28; r += 1

band("SECTION A — FORMAT / PLATFORM competitors missed (voice rooms, live-social, games+chat, community)", bandA_fill)
header_row()
for row in FORMAT:
    set_row(r, row, "A"); r += 1

r += 1
band("SECTION B — GAME GENRES missed (in PlayChat's 100+ catalog but absent from the 23-game matrix)", bandB_fill)
header_row()
for row in GENRE:
    set_row(r, row, "B"); r += 1

widths = [30,30,26,24,44,22,30]
for j, w in enumerate(widths, start=1):
    ws.column_dimensions[get_column_letter(j)].width = w
ws.sheet_view.showGridLines = False

# place after 'Game-by-Game Matrix'
names = wb.sheetnames
idx_target = names.index(SHEET)
want_after = names.index("Game-by-Game Matrix") if "Game-by-Game Matrix" in names else idx_target-1
wb.move_sheet(SHEET, offset=(want_after + 1) - idx_target)

wb.save(WB)
print("Saved. Sheets:", wb.sheetnames)
print("Format rows:", len(FORMAT), "| Genre rows:", len(GENRE))
