import json
import re

P = "build/web/index.html"
MIRROR = "https://vip-4.github.io/godot-open-star-fighter-web/"

meta = (
    '<meta name="description" content="Open Star Fighter — a free 3D space combat game built in Godot 4. Pilot your star fighter, shoot down the enemy, first team to 30 kills wins. Or race through hoops.">\n'
    '<meta name="keywords" content="open star fighter, godot game, space shooter, 3D space combat, free game, open source game, godot 4, web game">\n'
    '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">\n'
    '<link rel="canonical" href="' + MIRROR + '">\n'
    '<meta property="og:title" content="Open Star Fighter — Godot 4 Space Combat">\n'
    '<meta property="og:description" content="Pilot your star fighter, shoot down the enemy, first team to 30 kills wins. Built in Godot 4.">\n'
    '<meta property="og:type" content="website">\n'
    '<meta property="og:url" content="' + MIRROR + '">\n'
    '<meta name="twitter:card" content="summary_large_image">\n'
    '<meta name="twitter:title" content="Open Star Fighter — Godot 4 Space Combat">\n'
    '<meta name="twitter:description" content="Pilot your star fighter, shoot down the enemy, first team to 30 kills wins.">\n'
)

ld = {
    "@context": "https://schema.org",
    "@graph": [
        {"@type": "WebSite", "@id": MIRROR + "#website", "url": MIRROR,
         "name": "Open Star Fighter",
         "description": "A free 3D space combat game built in Godot 4. Pilot your star fighter, shoot down the enemy, first team to 30 kills wins.",
         "inLanguage": "en"},
        {"@type": "VideoGame", "@id": MIRROR + "#game", "name": "Open Star Fighter",
         "description": "Pilot your star fighter as part of a team, shooting down the enemy with blasters and missiles. First team to 30 kills wins. Or race through hoops.",
         "genre": ["Action", "Shooter", "Space"], "playMode": "MultiPlayer",
         "applicationCategory": "GameApplication", "operatingSystem": "Any (web browser)",
         "url": MIRROR, "isAccessibleForFree": True,
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}},
        {"@type": "FAQPage", "@id": MIRROR + "#faq", "mainEntity": [
            {"@type": "Question", "name": "How do you play Open Star Fighter?",
             "acceptedAnswer": {"@type": "Answer", "text": "Pilot your star fighter as part of a team and shoot down the enemy with blasters and missiles. First team to 30 kills wins. Alternatively, race through all the hoops as fast as you can."}},
            {"@type": "Question", "name": "What engine is the game built with?",
             "acceptedAnswer": {"@type": "Answer", "text": "The game is built with Godot 4.0 and uses the GL Compatibility renderer for the web build."}},
            {"@type": "Question", "name": "Is the game free and open source?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes. The game is free to play and the source code is published under the MIT license on GitHub."}},
        ]},
    ],
}
ld_json = json.dumps(ld, ensure_ascii=False, separators=(",", ":"))
meta += '<script type="application/ld+json">\n' + ld_json + "\n</script>\n"

s = open(P, encoding="utf-8").read()
s = s.replace("</head>", meta + "</head>", 1)
open(P, "w", encoding="utf-8").write(s)
print("injected; size", len(s))
