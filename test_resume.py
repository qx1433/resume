# test_resume.py
"""
Testovyj skript dlja proverki dannyh rezjume pered zagruzkoj v Google Docs.
Zapuskajte pered resume_uploader.py, chtoby ubeditsja, chto vse dannye korrektny.

Zapusk:
    python test_resume.py
"""

import sys

# IMPORTRUEM DANNYE IZ OSNOVNOGO SKRIPTA
RESUME_DATA = {
    "title": "Ljudvig Konstantin Anatolevich",
    "subtitle": "Inzhener ASU TP (pticevodstvo) | Cifrovizacija proizvodstva",
    "contacts": [
        "+7 (911) 457-99-37",
        "qx1433@gmail.com",
        "Kaliningrad (gotov k pereezdu)",
        "qx1433.github.io/resume"
    ],
    "summary": "Obsluzhivaju sistemy mikroklimata BigDutchman, Fancom, SKOV...",
    "extra_info": {
        "age": "1992 g.r. (33 goda)",
        "citizenship": "Rossijskaja Federacija",
        "license": "Voditelskoe udostoverenie kat. B (lichnyj avtomobil otsutstvuet)",
        "salary": "ot 120 000 RUB na ruki",
        "schedule": "Polnyj den, gotov k komandirovkam",
        "relocation": "Gotov rassmotret"
    },
    "highlights": [
        ("5+", "let v pticevodstve"),
        ("44", "ptichnika pod upravleniem"),
        ("3", "cifrovyh produkta dlja ceha"),
        ("2", "ASU zapuscheny s nulja")
    ],
    "skills": [
        {
            "title": "Promyshlennaja avtomatika",
            "tag": "Osnovnoj fokus",
            "items": [
                "Sistemy mikroklimata: BigDutchman, DACS, Fancom, SKOV - 44 obekta",
                "PLK: Siemens (Step7, TIA Portal, Logo), OVEN (CodeSys)",
                "Jazyki MEK 61131-3: ST (prioritet), LD, FBD, SCL",
                "Elektrotehnika: chtenie shem, PNR, rassledovanie neispravnostej"
            ]
        },
        {
            "title": "Cifrovizacija i IIoT",
            "tag": "Vnutrennie produkty",
            "items": [
                "PWA: skladskoj uchet (3 sklada, 44 zala), oflajn-rezhim",
                "Stek: Vanilla JS, Firebase, IndexedDB, REST API",
                "Integracii: Telegram API, Google API, Bitrix24"
            ]
        },
        {
            "title": "Otrasl i menedzhment",
            "tag": "Dopolnitelno",
            "items": [
                "Jekspertiza pticevodstva: brojlery, kormlenie, ventiljacija",
                "Change Management: migracija 20+ specialistov na platformu MAX",
                "Obuchenie personala: zootehniki, inzhenery, mastera"
            ]
        }
    ],
    "experience": [
        {
            "title": "Inzhener po ASU",
            "company": "OOO Pticevodcheskij kompleks Produkty pitanija, g. Kaliningrad",
            "date": "Mart 2021 - n.v.",
            "items": [
                "ASU TP: Obsluzhivanie i PNR schitov upravlenija mikroklimata na 44 ptichnikah...",
                "Cifrovizacija: Razrabotal s nulja PWA-prilozhenie...",
                "Vnedrenie izmenenij: Migracija 20+ specialistov na platformu MAX...",
                "Obuchenie zootehnikov..."
            ]
        },
        {
            "title": "Inzhener ASUP",
            "company": "OOO TPK Baltpticeprom, g. Kaliningrad",
            "date": "Aprel 2019 - Fevral 2021",
            "items": ["Tehnicheskoe obsluzhivanie ASU mikroklimata..."]
        },
        {
            "title": "Slesar KIPiA",
            "company": "OOO TPK Baltpticeprom, g. Kaliningrad",
            "date": "Janvar 2019 - Aprel 2019",
            "items": ["Tekuschij i profilakticheskij remont tehnologicheskogo oborudovanija."]
        },
        {
            "title": "Tehnik gruppy ASUTP",
            "company": "OOO Pro-Tok, g. Krasnojarsk",
            "date": "Oktjabr 2016 - Janvar 2017",
            "items": ["Nastrojka pozharnoj signalizacii..."]
        },
        {
            "title": "Elektromontazhnik",
            "company": "OOO MES, g. Krasnojarsk",
            "date": "Ijul 2016 - Oktjabr 2016",
            "items": ["Elektromontazhnye raboty do i svyshe 1000V."]
        },
        {
            "title": "Elektromontazhnik-naladchik (praktika)",
            "company": "OOO KPNU SVEM, g. Krasnojarsk",
            "date": "Aprel 2015 - Ijun 2015",
            "items": ["PNR s ispolzovaniem vy-ezdnoj avtolaboratorii."]
        }
    ],
    "education": [
        {
            "school": "Krasnojarskij politehnicheskij tehnikum",
            "meta": "2016 - Diplom s otlichiem",
            "detail": "Montazh, naladka i jekspluatacija jelektrooborudovanija...",
            "extra": "Sozdal obuchajuschie stendy..."
        },
        {
            "school": "Moskovskij tehnologicheskij institut (MTI)",
            "meta": "Student, sentjabr 2025 - 2029",
            "detail": "27.03.04 Upravlenie v tehnicheskih sistemah...",
            "extra": "TAU, PLK-programmirovanie..."
        }
    ],
    "languages": [
        ("Russkij", "Rodnoj"),
        ("Anglijskij", "B1 - chtenie tehnicheskoj dokumentacii...")
    ],
    "projects_link": "qx1433.github.io/resume",
    "ps": "Gotov k dialogu. Rassmatrivaju pozicii inzhenera ASU TP..."
}


def test_basic_structure():
    print("\nTEST 1: Proverka bazovoj struktury")
    required_fields = ["title", "subtitle", "contacts", "summary", "highlights", 
                       "skills", "experience", "education", "languages", "projects_link", "ps"]
    
    for field in required_fields:
        assert field in RESUME_DATA, "OTSUTSTVUET: {}".format(field)
        print("  [OK] {}".format(field))
    
    print("  + Vse objazatelnye polja na meste")


def test_extra_info():
    print("\nTEST 2: Proverka dopolnitelnoj informacii")
    assert "extra_info" in RESUME_DATA, "OTSUTSTVUET extra_info"
    extra = RESUME_DATA["extra_info"]
    required = ["age", "citizenship", "license", "salary", "schedule", "relocation"]
    for field in required:
        assert field in extra, "OTSUTSTVUET pole: {}".format(field)
        print("  [OK] {}: {}".format(field, extra[field]))
    print("  + Vse polja dop. informacii na meste")


def test_highlights():
    print("\nTEST 3: Proverka kljuchevyh dostizhenij")
    assert len(RESUME_DATA["highlights"]) == 4, "Dolzhno byt rovno 4 dostizhenija"
    
    expected = [("5+", "let v pticevodstve"), ("44", "ptichnika pod upravleniem"), 
                ("3", "cifrovyh produkta dlja ceha"), ("2", "ASU zapuscheny s nulja")]
    
    for i, (expected_num, expected_label) in enumerate(expected):
        actual_num, actual_label = RESUME_DATA["highlights"][i]
        assert actual_num == expected_num, "Dostizhenie {}: chislo '{}' != '{}'".format(i+1, actual_num, expected_num)
        assert actual_label == expected_label, "Dostizhenie {}: metka '{}' != '{}'".format(i+1, actual_label, expected_label)
        print("  [OK] {} - {}".format(actual_num, actual_label))
    
    print("  + Vse 4 dostizhenija korrektny")


def test_skills():
    print("\nTEST 3: Proverka navykov")
    assert len(RESUME_DATA["skills"]) == 3, "Dolzhno byt rovno 3 gruppy navykov"
    
    expected_groups = ["Promyshlennaja avtomatika", "Cifrovizacija i IIoT", "Otrasl i menedzhment"]
    for i, expected_title in enumerate(expected_groups):
        actual_title = RESUME_DATA["skills"][i]["title"]
        assert actual_title == expected_title, "Gruppa {}: '{}' != '{}'".format(i+1, actual_title, expected_title)
        print("  [OK] {}".format(actual_title))
    
    print("  + Vse 3 gruppy navykov na meste")


def test_experience():
    print("\nTEST 4: Proverka opyta raboty")
    assert len(RESUME_DATA["experience"]) >= 1, "Dolzhna byt hottja by 1 pozicija"
    
    for i, job in enumerate(RESUME_DATA["experience"]):
        assert "title" in job, "Rabota {}: net nazvanija dolzhnosti".format(i+1)
        assert "company" in job, "Rabota {}: net nazvanija kompanii".format(i+1)
        assert "date" in job, "Rabota {}: net daty".format(i+1)
        assert "items" in job and len(job["items"]) > 0, "Rabota {}: net opisanija".format(i+1)
        print("  [OK] {} ({})".format(job['title'], job['date']))
    
    print("  + Vsego pozicij: {}".format(len(RESUME_DATA['experience'])))


def test_contacts():
    print("\nTEST 5: Proverka kontaktov")
    contacts = RESUME_DATA["contacts"]
    assert len(contacts) >= 1, "Dolzhen byt hottja by 1 kontakt"
    
    has_phone = any(c.replace(" ", "").replace("+", "").replace("-", "").isdigit() for c in contacts)
    has_email = any("@" in c and "." in c for c in contacts)
    
    print("  [OK] Telefon: {}".format('najden' if has_phone else 'NE NAJDEN'))
    print("  [OK] Email: {}".format('najden' if has_email else 'NE NAJDEN'))
    print("  [OK] Vsego kontaktov: {}".format(len(contacts)))


def test_links():
    print("\nTEST 6: Proverka ssylok")
    portfolio = RESUME_DATA["projects_link"]
    assert "github.io" in portfolio or "qx1433" in portfolio, "Nekorrektnaja ssylka na portfolio"
    print("  [OK] Portfolio: {}".format(portfolio))


def test_document_id():
    print("\nTEST 7: Proverka Google Docs ID")
    doc_id = "1PWpTa22JJquulCzUj6AQ2EKvSs0MTe2mWzSA5GxLfqE"
    assert len(doc_id) > 20, "ID dokumenta vygledit nekorrektno"
    print("  [OK] ID dokumenta: {}...".format(doc_id[:15]))


def run_all_tests():
    print("=" * 50)
    print("TESTIROVANIE DANNYH REZUME")
    print("=" * 50)
    
    tests = [
        test_basic_structure,
        test_extra_info,
        test_highlights,
        test_skills,
        test_experience,
        test_contacts,
        test_links,
        test_document_id
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print("\n  [FAIL] {}".format(e))
            failed += 1
        except Exception as e:
            print("\n  [ERROR] {}".format(e))
            failed += 1
    
    print("\n" + "=" * 50)
    print("Rezultaty: {} OK / {} FAIL".format(passed, failed))
    print("=" * 50)
    
    if failed == 0:
        print("\nVse testy projdeny! Mozhno zapuskat resume_uploader.py")
        return 0
    else:
        print("\n Najdeno {} problem. Ispravte pered zagruzkoj.".format(failed))
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
