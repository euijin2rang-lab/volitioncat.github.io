# -*- coding: utf-8 -*-
"""English UI patch for Alice_Smile.html — regex blocks + ordered phrase replace."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "Alice_Smile.html"

ENDINGS_EN = r"""const ENDINGS={
  0:{key:'normal',title:'Normal Ending',badge:'NORMAL END',bgm:'end_bgm/IDsmile.mp3',credits:false,lines:[
    'This fairy tale ends here.',
    'Did you truly leave a meaningful mark?',
    'Which choices were ever the right ones,',
    'is a question that no longer matters now.'
  ]},
  1:{key:'e1',title:'Holding a bouquet of pretense',badge:'ENDING 1',bgm:'end_bgm/bakenohana.mp3',credits:true,cut:'end/1.png',lines:[
    'The midnight bell rang, and the masquerade spell broke.',
    'The glittering dress, the glass slippers, even Alice\'s beloved smile — all of it shattered.',
    'People pointed at the unmasked Alice and called her a monster.',
    'Alice cast aside ribbons and pretty shoes and ran, and kept on running.',
    'She turned away from every stare, every voice, even your gentle touch.',
    'Where did the child go, the one who erased even her real name?'
  ]},
  2:{key:'e2',title:'Alice Smile',badge:'ENDING 2',bgm:'end_bgm/IDsmile.mp3',credits:true,cut:'end/2.png',lines:[
    'Alice chose to be queen of Wonderland forever.',
    'Reality was cold and cruel, but the world beyond the monitor felt warm.',
    'As long as Alice smiled, everyone whispered unconditional love.',
    'At the dark 25th hour, her friends off-screen watch Alice rise in the algorithm.',
    'They turn away, bittersweet, at a smile that looks perfectly happy.',
    'Alice beyond the glass — the one they longed to reach, now forever out of reach.',
    'Today, too, she wears a lie of a perfect smile.'
  ]},
  3:{key:'e3',title:'Even if I want to see real love',badge:'ENDING 3',bgm:'end_bgm/Kitty.mp3',credits:true,cut:'end/3.png',lines:[
    'No one followed her down the rabbit hole.',
    'The lies she spun to be loved, the pretty dress — none of it helped.',
    'Only suffocating silence circled Alice in her empty room.',
    'Alice quietly locked the door — the one to reality, and the window to the internet.',
    'Inside a small dark box where neither love nor hate could reach...',
    'Alice finally fell into a deep sleep where nothing could hurt her.'
  ]},
  4:{key:'e4',title:'Even if my footprints are your destination',badge:'ENDING 4',bgm:'end_bgm/Lower.mp3',credits:true,cut:'end/4.png',lines:[
    'Welcome to the dollhouse!',
    'Alice never has to worry again.',
    'She only has to dance as people want, sing as people want.',
    'The sound of a breaking heart was drowned out by thunderous applause.',
    'As long as the music plays, the pretty doll will keep dancing.',
    'Happily ever after, for a long, long time.'
  ]},
  5:{key:'e5',title:'And now, untying the ribbon',badge:'ENDING 5',bgm:'end_bgm/Ribbon.mp3',credits:true,cut:'end/5.png',lines:[
    'The storybook is over. It is time for Alice to return to reality.',
    'Keeping the magic alive under hostile eyes was exhausting.',
    'So Alice decided to snap her own wand in two.',
    'She untied the ribbon, tore the frills, and pulled on the ashen clothes the world demanded.',
    'The world stayed peaceful — and nowhere in it was Alice.'
  ]},
  6:{key:'e6',title:'Read as darkness, written as dawn',badge:'ENDING 6',bgm:'end_bgm/6.mp3',credits:true,cut:'end/6.png',lines:[
    'Alice wandered an endless maze in Wonderland.',
    'No lavish tea party, no sweet praise could quench her thirst.',
    'Alice was afraid — she believed that if she removed the mask, everyone would leave.',
    'Yet following the small pebbles she dropped in despair, her real friends found the bottom of the rabbit hole.',
    'The dazzling monitor went dark; the door to a false Wonderland closed forever.',
    'When she opened the door to reality with care, the endless dark she feared was waiting — with the warm dawn of 25-ji.',
    'Neither a forced doll smile, nor a resigned ashen life.',
    'The real story of Akiyama Mizuki begins again from this dawn.'
  ]}
};"""

CREDITS_EN = r"""const CREDITS_HTML=`<div class="cred-title">〈Alice Smile〉</div>
Based on Project SEKAI COLORFUL STAGE! feat. Hatsune Miku

Director / Producer Euijin Lee
Art Euijin Lee

SFX: 効果音ラボ, みんなの創作支援サイトＴスタ / T-STUDIO
BGM: R3 music box

Special Thanks to 宵崎奏, 朝比奈まふゆ, 東雲絵名, and 暁山瑞希
AwA, Nito
And you`"""
END6_CREDITS_EN = CREDITS_EN.replace("CREDITS_HTML", "END6_CREDITS_HTML")

GREETINGS_EN = r"""const MG=[
  ['Good morning — or is it too late for that?','Anyway, thanks for today too!'],
  ['Mmm... I really do not want to leave the blankets. Right?','Still... turning on notifications woke me right up!'],
  ['A new morning is here!','Time to start a busy day...'],
  ['Wait, are you dozing off?','Is it time to wake up already?'],
  ['Already morning?','I want more sleep, but if you wake me, I will get up...'],
  ['Good morning!','I checked the mirror — I feel amazing today!','Let me put on something cute and take photos first!'],
  ['Finally the last day...','Thanks for sticking with me today too'],
];
const AG=[
  ['Afternoons like this feel so boring...','I need something exciting!'],
  ['Did you eat?','I have been nibbling sweets. I want cream puffs.'],
  ['If this were a school day, everyone would be in class about now, huh?'],
  ['The sunlight hits the screen too hard to see','The internet really is better in the dark~'],
  ['Bored~','Let us do something already?','Do not leave me bored!'],
  ['Afternoon sun is perfect for natural-light selfies!'],
];
const NG=[
  ['Still awake?','Well, sleep is hard to catch at this hour. Right?'],
  ['It is the hour when everyone else is asleep.','The internet is loud, though~'],
  ['Whoa, found a cringe-soft post I can barely look at!','Screenshotting this for later blackmail~'],
  ['Nightcord... maybe I really should reinstall it.'],
  ['At night the tight feeling in my chest eases up...','Or maybe it is just the cold air?'],
];
function getGreeting(slot){
  if(G.day===4&&slot===0) return ['Feels like rain'];
  if(G.day===2&&slot===1) return ['Not enough money for clothes...'];
  if(G.day===6&&slot===0) return ['I want to go to a cat cafe'];
  if(G.day===6&&slot===2) return ['Hope I can sleep soundly'];
  if(slot===0) return MG[Math.min(G.day-1,MG.length-1)];
  if(slot===1) return AG[rnd(0,AG.length-1)];
  return NG[rnd(0,NG.length-1)];
}"""

DIARY_EN = r"""const DIARY_SOUL_TEXT=`Sometimes I just want to pop like a soap bubble and vanish where nobody notices.
As if I had never been in this world at all.
If I were really gone by tomorrow morning, would they even look for me?
Ena would yell and cry all over again without thinking.
Kanade would blame herself and stay up writing songs, suffering.
Mafuyu might... slam shut the heart she had only just begun to find.
Everyone is struggling to move forward,
while I stay frozen, piling lie on top of lie.
Hiding who I really am to the end, only running because I do not want to get hurt.
Trying to make it easy for myself means walking away from people who cared about me.
I am sorry. I wanted to smile beside you all, just... ordinarily.
Where did it start to go wrong?
Living with secrets hurts, and yet I feel sorry for the people I would leave behind.
I cannot choose either side, so I stay stuck in a mess.

I am truly sorry for being selfish to the very end.`;"""


def main():
    s = HTML.read_text(encoding="utf-8")

    s, c = re.subn(r"const ENDINGS=\{.*?\n\};", ENDINGS_EN, s, count=1, flags=re.DOTALL)
    if c != 1:
        raise SystemExit(f"ENDINGS replace failed: {c}")

    s, c = re.subn(
        r"const CREDITS_HTML=`[\s\S]*?And you`;",
        CREDITS_EN + ";",
        s,
        count=1,
    )
    if c != 1:
        raise SystemExit(f"CREDITS_HTML replace failed: {c}")

    s, c = re.subn(
        r"const END6_CREDITS_HTML=`[\s\S]*?And you`;",
        END6_CREDITS_EN + ";",
        s,
        count=1,
    )
    if c != 1:
        raise SystemExit(f"END6_CREDITS_HTML replace failed: {c}")

    s, c = re.subn(
        r"const MG=\[[\s\S]*?return NG\[rnd\(0,NG\.length-1\)\];\n\}\n\n\n// ═══════════════════════════════════════\n//  TURN / TRANSITION",
        GREETINGS_EN + "\n\n\n// ═══════════════════════════════════════\n//  TURN / TRANSITION",
        s,
        count=1,
    )
    if c != 1:
        raise SystemExit("GREETINGS replace failed")

    s, c = re.subn(
        r"const DIARY_SOUL_TEXT=`[\s\S]*?`;\n\nfunction enterDiarySoulMode",
        DIARY_EN + "\n\nfunction enterDiarySoulMode",
        s,
        count=1,
    )
    if c != 1:
        raise SystemExit("DIARY replace failed")

    # Long phrases before short substrings (names, tags)
    phrases: list[tuple[str, str]] = []

    # Character / place display names
    phrases += [
        ("아키야마 미즈키 카미야마고", "Akiyama Mizuki Kamiyama High"),
        ("아키야마 미즈키", "Akiyama Mizuki"),
        ("에나낭 외 3명", "Ena and 3 others"),
        ("카나데, 마후유", "Kanade, Mafuyu"),
        ("에나낭", "Ena"),
        ("카나데", "Kanade"),
        ("마후유", "Mafuyu"),
        ("마사키 와타리", "Masaki Watari"),
        ("카미야마 고등학교", "Kamiyama High School"),
        ("카미야마고", "Kamiyama High"),
    ]

    # Fashion tags (internal keys = on-screen hashtags)
    tag_pairs = [
        ("지뢰계", "Jiraikei"),
        ("지하돌", "Chikaidol"),
        ("갸루", "Gyaru"),
        ("로리타", "Lolita"),
        ("고스", "Goth"),
        ("펑크", "Punk"),
        ("엔젤코어", "Angelcore"),
        ("데코라", "Decora"),
        ("스쿨룩", "Schoollook"),
        ("발레코어", "Balletcore"),
        ("데일리", "Daily"),
        ("일상복", "Casual"),
        ("스트리트", "Street"),
        ("멘헤라", "Menhera"),
        ("우울", "Melancholy"),
        ("어둠", "Dark"),
        ("일상", "Everyday"),
        ("요리", "Cooking"),
        ("섹시", "Sexy"),
        ("음악", "Music"),
        ("공주님", "Princess"),
        ("고등학생", "Highschooler"),
        ("아이돌", "Idol"),
        ("요정", "Fairy"),
        ("고양이", "Cat"),
        ("셀카", "selfie"),
        ("나이트코드", "Nightcord"),
        ("25시", "25ji"),
        ("어둠계", "Yamikei"),
    ]
    phrases += tag_pairs

    # Shop
    phrases += [
        ("리본 헤드밴드", "Ribbon headband"),
        ("프릴 블라우스", "Frilly blouse"),
        ("별 귀걸이", "Star earrings"),
        ("레이스 양말", "Lace socks"),
        ("핑크 미니 가방", "Pink mini bag"),
        ("달 목걸이", "Moon necklace"),
        ("체크 스커트", "Plaid skirt"),
        ("하트 틴트", "Heart lip tint"),
        ("레이스 스타킹", "Lace stockings"),
    ]

    # UI strings (batch)
    phrases += [
        ('aria-label="주의 사항"', 'aria-label="Notice"'),
        ("이 게임은 프로젝트 세카이를 기반으로 한 2차 창작 비영리 게임입니다.", "This is a non-profit fan work based on Project SEKAI."),
        ("이 게임에는 다소 자극적인 장면이나 단어, 상황이 포함될 수 있어 주의가 필요합니다.", "This game may include mildly intense scenes, language, or situations. Please read with care."),
        ("이 게임에는 AI를 사용한 컨텐츠가 포함되어 있습니다.", "This game includes content created with the help of AI."),
        ("터치 · 클릭하여 계속", "Tap or click to continue"),
        ("시작하기", "Start"),
        ("팔로워", "Followers"),
        ("신상", "Dox risk"),
        ("1일차", "Day 1"),
        ("오전", "Morning"),
        ("오후", "Afternoon"),
        ("멘탈", "Mental"),
        ("현실", "Reality"),
        ("아무것도 못하겠어", "I cannot do anything anymore"),
        ("월요일", "Monday"),
        ("팟캐스트", "Podcast"),
        ('<span class="albl">지도</span>', '<span class="albl">Map</span>'),
        ('<div class="att" style="color:#fff">지도</div>', '<div class="att" style="color:#fff">Map</div>'),
        ("갤러리", "Gallery"),
        ("연락처", "Contacts"),
        ("앱스토어", "App Store"),
        ("일기", "Diary"),
        ("해시태그-001", "Hashtags — set 1"),
        ("해시태그-002", "Hashtags — set 2"),
        ("태그를 선택하세요", "Select tags"),
        ("📩 새 DM 도착", "📩 New DM"),
        ("RedCard 엔터테인먼트에서 DM이 왔어요", "You have a DM from RedCard Entertainment"),
        ("검색하기...", "Search..."),
        ("연관검색어", "Related searches"),
        ("홈", "Home"),
        ("트렌드", "Trending"),
        ("알림", "Notifications"),
        ("검색결과", "Search results"),
        ("오늘의 트렌드 — 실시간", "Today's trends — live"),
        ("아직 DM이 없어요", "No DMs yet"),
        ("안녕하세요! Alice_anon님!", "Hello, Alice_anon!"),
        (
            '<div style="font-size:7.5px;color:#bbb">방금</div>',
            '<div style="font-size:7.5px;color:#bbb">Just now</div>',
        ),
        ("답장...", "Reply..."),
        ("재고 --", "Stock --"),
        ("재고 보충 중", "Restocking"),
        ("재고 보충 중이야", "Restocking"),
        ("재고 ", "Stock: "),
        ("구매!", "bought!"),
        ("구독", "Subscriptions"),
        ("124만회 · 3일 전", "1.24M views · 3 days ago"),
        ("38만회 · 5일 전", "380K views · 5 days ago"),
        ("12만회 · 1주 전", "120K views · 1 week ago"),
        ("5.4만회", "54K views"),
        ("담임 선생님", "Homeroom teacher"),
        ("2-B반 단톡방", "Class 2-B group chat"),
        ("알림 꺼둠", "Notifications muted"),
        ("어제", "Yesterday"),
        ("수면 팟캐스트", "Sleep podcast"),
        ("White Noise — 수면용", "White Noise — for sleep"),
        ("빗소리 & 파도 · 화이트 노이즈", "Rain & waves · white noise"),
        ("1시간", "1 hr"),
        ("5시간", "5 hr"),
        ("25시간", "25 hr"),
        ("번화가 지도", "Downtown map"),
        ("목적지를 선택해주세요", "Choose a destination"),
        ("패밀리 레스토랑", "Family restaurant"),
        ("스크램블 교차로 (번화가)", "Scramble crossing (downtown)"),
        ("최근 삭제된 항목", "Recently deleted"),
        ("사진 250장", "250 photos"),
        ("🔒 잠긴 앨범", "🔒 Locked album"),
        ("비밀번호를 입력하세요", "Enter passcode"),
        ("취소", "Cancel"),
        ("확인", "OK"),
        ("부재중 통화", "Missed calls"),
        ("부재중 7건", "7 missed"),
        ("부재중 3건", "3 missed"),
        ("부재중 2건", "2 missed"),
        ("부재중 1건", "1 missed"),
        ("부재중", "Missed"),
        ("최근 삭제한 앱", "Recently deleted apps"),
        ("삭제일: 6일 전", "Deleted: 6 days ago"),
        ("복구", "Restore"),
        ("다른 삭제된 앱 없음", "No other deleted apps"),
        ("채팅", "Chat"),
        ("새 메시지 1개", "1 new message"),
        ("메시지를 기다리는 중...", "Waiting for a message..."),
        ("메시지", "Messages"),
        ('aria-label="뒤로"', 'aria-label="Back"'),
        ("접속 중", "Online"),
        ("상태", "Status"),
        ("✕ 닫기", "✕ Close"),
        ("@Alice_anon · 팔로워 10%", "@Alice_anon · Followers 10%"),
        ("신상노출도", "Dox risk"),
        ("현실치", "Reality meter"),
        ("앨리스 수치", "Alice gauge"),
        ("메시지...", "Message..."),
        ("이어서", "Continue"),
        ("웹캠", "Webcam"),
        ("화면을 누르면 돌아갩니다", "Tap the screen to return"),
        ("엔딩 컷씬", "Ending cutscene"),
        ("터치 · 클릭으로 다음", "Tap or click for next"),
        ("비밀번호가 맞지 않습니다", "Incorrect passcode"),
        ("차단되어 메시지를 보낼 수 없습니다", "You cannot send messages while blocked"),
        ("시스템", "System"),
        ("타임라인 불러오는 중...", "Loading timeline..."),
        ("불러오기 완료", "Finished loading"),
        ("인용 트윗", "Quote tweet"),
        ("@Alice_anon 의 트윗 인용", "Quoting @Alice_anon's tweet"),
        ("대답해줘...", "Say something..."),
        ("전송 중...", "Sending..."),
        ("자리 비움", "Away"),
        ("--- 3일차 오전 ---", "--- Day 3 · Morning ---"),
        ("— 1일차 오전 —", "— Day 1 · Morning —"),
        ("게시물에 반응이 달렸어요", "People reacted to your post"),
        ("그것이 당신의 행복이라 할지라도", "Even If That Isn't Happiness"),
        ("25시, 나이트코드에서.", "25-ji, Nightcord de."),
        ("「그것이 당신의 행복이라 할지라도」 MV", '"Even If That Isn\'t Happiness" MV'),
        ("지뢰계 코디 모음", "Jirai-kei coord roundup"),
        ("지뢰계패션TV", "JiraiFashionTV"),
        ("2025 지뢰계 코디 모음 🖤", "2025 Jirai-kei coords 🖤"),
        ("로리타 갸루 믹스 하울", "Lolita × gyaru mix haul"),
        ("haul채널", "haul channel"),
        ("세일 득템 하울 / 로리타·갸루 믹스", "Sale finds haul / lolita × gyaru mix"),
        ("폰 카메라로 감성 셀카 찍는법", "Moody phone selfies how-to"),
        ("셀카연구소", "Selfie Lab"),
        ("폰 카메라로 감성 셀카 찍는 법", "How to take moody selfies on your phone"),
        ("아키야마, 2B반 보충수업 내일...", "Akiyama — remedial class for 2-B tomorrow..."),
        ("오전 9:12", "9:12 AM"),
        ("담임", "Teacher"),
        (
            "안녕하세요! Alice_anon님!<br><br>인디 아이돌 엔터테인먼트 회사 'RedCard'의 스카우트 담당자인 마사키 와타리라고 합니다.<br><br>Alice_anon님의 비주얼과 트렌디한 감각이 저희 회사에서 이번에 기획하고 있는 신규 아이돌 그룹의 분위기와 너무 잘 맞아서 연락드리게 되었어요.<br><br>혹시 생각이 있으시다면 답장 부탁드립니다.",
            "Hello, Alice_anon!<br><br>I am Masaki Watari, a talent scout at the indie idol agency RedCard.<br><br>Your visuals and sharp sense of style are a perfect fit for the mood of a new idol group we are putting together, so I wanted to reach out.<br><br>If you are interested, I would love to hear back from you.",
        ),
        ("@Alice_anon 정체", "@Alice_anon identity"),
        ("Switter에 업로드했어", "Posted to Switter"),
        ("뮤비 시청", "Watching MV"),
        ("수면 중...", "Sleeping..."),
        ("Zine 확인", "Zine checked"),
        ("학교 다녀옴", "Back from school"),
        ("번화가 다녀왔다", "Back from downtown"),
        ("고마워", "Thank you"),
        ("Ctrl+Shift+0~6: 엔딩 실행 / Ctrl+Shift+M,E,S: 이벤트 실행", "Ctrl+Shift+0~6: play ending / Ctrl+Shift+M,E,S: trigger event"),
    ]

    # Mizuki speaker id
    phrases += [
        ("who==='미즈키'", "who==='Mizuki'"),
        ("qMsg('미즈키'", "qMsg('Mizuki'"),
        ("title.textContent='미즈키'", "title.textContent='Mizuki'"),
        ("getElementById('mhdr-title').textContent='미즈키'", "getElementById('mhdr-title').textContent='Mizuki'"),
        ("<div class=\"mname\" id=\"mhdr-title\">미즈키</div>", '<div class="mname" id="mhdr-title">Mizuki</div>'),
        ("<div class=\"end6-rname\">미즈키</div>", '<div class="end6-rname">Mizuki</div>'),
        ('alt="미즈키"', 'alt="Mizuki"'),
        ('alt="미즈키 스위터 프로필"', 'alt="Mizuki Switter profile"'),
        ("<div class=\"sname\">아키야마 미즈키</div>", '<div class="sname">Akiyama Mizuki</div>'),
    ]

    # JS clock / slots / day label
    phrases += [
        ("const days=['일','월','화','수','목','금','토'];", "const days=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];"),
        (
            "if(dateEl) dateEl.textContent=`${n.getMonth()+1}월 ${n.getDate()}일 ${days[n.getDay()]}요일`;",
            "if(dateEl) dateEl.textContent=`${days[n.getDay()]}, ${n.getMonth()+1}/${n.getDate()}`;",
        ),
        ("const SLOTS=['오전','오후','새벽'];", "const SLOTS=['Morning','Afternoon','Late night'];"),
        ("const d=G.day+'일차',t=SLOTS[G.slot];", "const d='Day '+G.day,t=SLOTS[G.slot];"),
        (
            "const isAboutMe=keyword.includes('미즈키')||keyword.includes('Alice_anon')||keyword.toLowerCase().includes('alice_anon')||keyword.includes('카미야마');",
            "const isAboutMe=keyword.includes('Mizuki')||keyword.includes('미즈키')||keyword.includes('Alice_anon')||keyword.toLowerCase().includes('alice_anon')||keyword.includes('Kamiyama')||keyword.includes('카미야마');",
        ),
        ('"${keyword}" 검색 결과', '"${keyword}" results'),
        ("<div class=\"trnkr\">${i+1}위</div>", '<div class="trnkr">#${i+1}</div>'),
        ("<div class=\"trncnt\">트윗 ${t.cnt}개</div>", '<div class="trncnt">${t.cnt} tweets</div>'),
    ]

    # Combo image keys (ASCII sort)
    phrases += [
        ("'아이돌|지뢰계':'selfi/idol.png'", "'Idol|Jiraikei':'selfi/idol.png'"),
        ("'로리타|어둠':'selfi/yami.png'", "'Dark|Lolita':'selfi/yami.png'"),
        ("'공주님|로리타':'selfi/hime.png'", "'Lolita|Princess':'selfi/hime.png'"),
        ("'데일리|요정':'selfi/fairy.png'", "'Daily|Fairy':'selfi/fairy.png'"),
        ("'스트리트|음악':'selfi/kasa.png'", "'Music|Street':'selfi/kasa.png'"),
        ("'갸루|요리':'selfi/yori.png'", "'Cooking|Gyaru':'selfi/yori.png'"),
        ("'고양이|데일리':'selfi/neko.png'", "'Cat|Daily':'selfi/neko.png'"),
        ("'갸루|섹시':'selfi/sexy.png'", "'Gyaru|Sexy':'selfi/sexy.png'"),
    ]

    phrases.sort(key=lambda x: len(x[0]), reverse=True)
    for ko, en in phrases:
        s = s.replace(ko, en)

    # Exact multi-token fixes (avoid naive substring damage)
    for ko, en in [
        ("showToast('지금은 검색할 수 없어')", "showToast('You cannot search right now')"),
        ("if(stockEl) stockEl.textContent='재고 '+s+'개';", "if(stockEl) stockEl.textContent='In stock: '+s;"),
        ("if(stockEl) stockEl.textContent='Stock: '+s+'개';", "if(stockEl) stockEl.textContent='In stock: '+s;"),
        (
            "{av:'유',un:'@user_a',txt:`#${keyword} 오늘도 트렌드에 있네`}",
            "{av:'You',un:'@user_a',txt:`#${keyword} is trending again today`}",
        ),
        (
            "{av:'팬',un:'@fan_b',txt:`${keyword} 좋아하는 사람 손!`}",
            "{av:'Fan',un:'@fan_b',txt:`Hands up if you like ${keyword}!`}",
        ),
        (
            "{av:'익',un:'@anon_c',txt:`${keyword} 요즘 좀 질리는 것 같기도...`}",
            "{av:'An',un:'@anon_c',txt:`${keyword} feels a little played out lately...`}",
        ),
    ]:
        s = s.replace(ko, en)

    HTML.write_text(s, encoding="utf-8")
    print("Patched", HTML)


if __name__ == "__main__":
    main()
