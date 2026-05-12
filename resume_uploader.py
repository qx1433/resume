# resume_uploader.py
"""
Скрипт для автоматического обновления резюме в Google Docs через API.
Требует: client_secret.json (OAuth credentials от Google Cloud Console)

Установка зависимостей:
    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

Запуск:
    python resume_uploader.py

Первый запрос откроет браузер для авторизации.
Токен сохранится в token.json для последующих запусков.
"""

import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# === НАСТРОЙКИ ===
DOCUMENT_ID = "1PWpTa22JJquulCzUj6AQ2EKvSs0MTe2mWzSA5GxLfqE"
SCOPES = ['https://www.googleapis.com/auth/documents']
CREDENTIALS_FILE = "client_secret.json"
TOKEN_FILE = "token.json"

# === ДАННЫЕ РЕЗЮМЕ ===
RESUME_DATA = {
    "title": "Людвиг Константин Анатольевич",
    "subtitle": "Инженер АСУ ТП (птицеводство) | Цифровизация производства",
    "contacts": [
        "+7 (911) 457-99-37",
        "qx1433@gmail.com",
        "Калининград (готов к переезду)",
        "qx1433.github.io/resume"
    ],
    "summary": "Обслуживаю системы микроклимата BigDutchman, Fancom, SKOV. Разрабатываю управляющую логику для ПЛК Siemens и ОВЕН (ST, LD). Создаю внутренние цифровые инструменты для производства. Расследую сложные неисправности, которые другие считают нормой.",
    "extra_info": {
        "age": "1992 г.р. (33 года)",
        "citizenship": "Российская Федерация",
        "license": "Водительское удостоверение кат. B (личный автомобиль отсутствует)",
        "salary": "от 120 000 ₽ на руки",
        "schedule": "Полный день, готов к командировкам",
        "relocation": "Готов рассмотреть"
    },
    "highlights": [
        ("5+", "лет в птицеводстве"),
        ("44", "птичника под управлением"),
        ("3", "цифровых продукта для цеха"),
        ("2", "АСУ запущены с нуля")
    ],
    "skills": [
        {
            "title": "Промышленная автоматика",
            "tag": "Основной фокус",
            "items": [
                "Системы микроклимата: BigDutchman, DACS, Fancom, SKOV — 44 объекта",
                "ПЛК: Siemens (Step7, TIA Portal, Logo), ОВЕН (CodeSys)",
                "Языки МЭК 61131-3: ST (приоритет), LD, FBD, SCL",
                "Электротехника: чтение схем, ПНР, расследование неисправностей"
            ]
        },
        {
            "title": "Цифровизация и IIoT",
            "tag": "Внутренние продукты",
            "items": [
                "PWA: складской учёт (3 склада, 44 зала), офлайн-режим",
                "Стек: Vanilla JS, Firebase, IndexedDB, REST API",
                "Интеграции: Telegram API, Google API, Bitrix24"
            ]
        },
        {
            "title": "Отрасль и менеджмент",
            "tag": "Дополнительно",
            "items": [
                "Экспертиза птицеводства: бройлеры, кормление, вентиляция",
                "Change Management: миграция 20+ специалистов на платформу MAX",
                "Обучение персонала: зоотехники, инженеры, мастера"
            ]
        }
    ],
    "experience": [
        {
            "title": "Инженер по АСУ",
            "company": "ООО «Птицеводческий комплекс «Продукты питания», г. Калининград",
            "date": "Март 2021 — н.в.",
            "items": [
                "АСУ ТП: Обслуживание и ПНР щитов управления микроклимата на 44 птичниках (SKOV, BigDutchman, Fancom). Полная замена оборудования, расследование сложных неисправностей, выявление ошибок электромонтажа.",
                "Цифровизация: Разработал с нуля PWA-приложение для складского учёта (3 склада, 44 зала). Офлайн-режим, QR-маркировка, Firebase.",
                "Внедрение изменений: Миграция 20+ специалистов на платформу MAX. Адаптация Bitrix24 под производство, обучение инженеров и мастеров.",
                "Обучение зоотехников и онбординг новых инженеров АСУ."
            ]
        },
        {
            "title": "Инженер АСУП",
            "company": "ООО «ТПК «Балтптицепром», г. Калининград",
            "date": "Апрель 2019 — Февраль 2021",
            "items": [
                "Техническое обслуживание АСУ микроклимата на производственных объектах комплекса."
            ]
        },
        {
            "title": "Слесарь КИПиА",
            "company": "ООО «ТПК «Балтптицепром», г. Калининград",
            "date": "Январь 2019 — Апрель 2019",
            "items": [
                "Текущий и профилактический ремонт технологического оборудования."
            ]
        },
        {
            "title": "Техник группы АСУТП",
            "company": "ООО «Про-Ток», г. Красноярск",
            "date": "Октябрь 2016 — Январь 2017",
            "items": [
                "Настройка пожарной сигнализации (С2000М в Bolid Pprog) на АО «Полюс Вернинское»."
            ]
        },
        {
            "title": "Электромонтажник",
            "company": "ООО «МЭС», г. Красноярск",
            "date": "Июль 2016 — Октябрь 2016",
            "items": [
                "Электромонтажные работы до и свыше 1000В."
            ]
        },
        {
            "title": "Электромонтажник-наладчик (практика)",
            "company": "ООО КПНУ «СВЭМ», г. Красноярск",
            "date": "Апрель 2015 — Июнь 2015",
            "items": [
                "ПНР с использованием выездной автолаборатории."
            ]
        }
    ],
    "education": [
        {
            "school": "Красноярский политехнический техникум",
            "meta": "2016 — Диплом с отличием",
            "detail": "Монтаж, наладка и эксплуатация электрооборудования. Квалификация: техник-электрик.",
            "extra": "Создал обучающие стенды: макет подстанции на Siemens LOGO, стенд для Simatic S7-1200."
        },
        {
            "school": "Московский технологический институт (МТИ)",
            "meta": "Студент, сентябрь 2025 — 2029 (ожидаемое окончание)",
            "detail": "27.03.04 Управление в технических системах, заочная форма.",
            "extra": "ТАУ, ПЛК-программирование, Modbus, Profibus, OPC UA, микропроцессорные системы. III группа по электробезопасности."
        }
    ],
    "languages": [
        ("Русский", "Родной"),
        ("Английский", "B1 — чтение технической документации, переписка с вендорами")
    ],
    "projects_link": "qx1433.github.io/resume",
    "ps": "Готов к диалогу. Рассматриваю позиции инженера АСУ ТП и специалиста по цифровизации в агропромышленном секторе. Готов обсудить задачи вашего производства и показать, как автоматизация + цифровизация снижают простои и повышают прозрачность процессов."
}


def get_credentials():
    """Получает или обновляет OAuth credentials."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                print(f" Файл {CREDENTIALS_FILE} не найден!")
                print("Скачайте его из Google Cloud Console → APIs & Services → Credentials → OAuth 2.0 Client ID → Download JSON")
                exit(1)

            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return creds


def clear_document(service, doc_id):
    """Очищает содержимое документа."""
    doc = service.documents().get(documentId=doc_id).execute()
    content = doc.get('body', {}).get('content', [])

    if len(content) > 1:
        end_index = content[-1].get('endIndex', 1)
        if end_index > 1:
            service.documents().batchUpdate(
                documentId=doc_id,
                body={'requests': [{'deleteContentRange': {
                    'range': {'startIndex': 1, 'endIndex': end_index}
                }}]}
            ).execute()
            print(" Документ очищен")


def insert_text(service, doc_id, text, style=None, index=1):
    """Вставляет текст с заданным стилем."""
    requests = [
        {'insertText': {'location': {'index': index}, 'text': text}}
    ]

    if style:
        end_index = index + len(text)
        requests.append({
            'updateParagraphStyle': {
                'range': {'startIndex': index, 'endIndex': end_index},
                'paragraphStyle': style,
                'fields': ','.join(style.keys())
            }
        })

    service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()
    return index + len(text)


def insert_text_run(service, doc_id, text, bold=False, italic=False, font_size=None, color=None, index=1):
    """Вставляет текст с inline-форматированием."""
    requests = [{'insertText': {'location': {'index': index}, 'text': text}}]

    end_index = index + len(text)
    text_style = {}
    if bold:
        text_style['bold'] = True
    if italic:
        text_style['italic'] = True
    if font_size:
        text_style['fontSize'] = {'magnitude': font_size, 'unit': 'PT'}
    if color:
        text_style['foregroundColor'] = {'color': {'rgb': color}}

    if text_style:
        requests.append({
            'updateTextStyle': {
                'range': {'startIndex': index, 'endIndex': end_index},
                'textStyle': text_style,
                'fields': ','.join(text_style.keys())
            }
        })

    service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()
    return end_index


def build_resume(service, doc_id):
    """Собирает резюме в документе."""
    data = RESUME_DATA
    idx = 1

    # === ЗАГОЛОВОК ===
    idx = insert_text_run(service, doc_id, data['title'] + "\n", bold=True, font_size=22, index=idx)

    # Должность
    idx = insert_text_run(service, doc_id, data['subtitle'] + "\n", bold=True, font_size=12, color={'red': 0.02, 'green': 0.59, 'blue': 0.41}, index=idx)

    # Контакты
    contacts_str = "  |  ".join(data['contacts']) + "\n"
    idx = insert_text(service, doc_id, contacts_str, index=idx)

    # Разделитель
    idx = insert_text(service, doc_id, "\n", index=idx)

    # === ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ ===
    idx = insert_text_run(service, doc_id, "ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ\n", bold=True, font_size=13, index=idx)
    extra = data['extra_info']
    idx = insert_text(service, doc_id, f"Возраст: {extra['age']}\n", index=idx)
    idx = insert_text(service, doc_id, f"Гражданство: {extra['citizenship']}\n", index=idx)
    idx = insert_text(service, doc_id, f"{extra['license']}\n", index=idx)
    idx = insert_text(service, doc_id, f"Зарплатные ожидания: {extra['salary']}\n", index=idx)
    idx = insert_text(service, doc_id, f"График: {extra['schedule']}\n", index=idx)
    idx = insert_text(service, doc_id, f"Переезд: {extra['relocation']}\n\n", index=idx)

    # === КЛЮЧЕВЫЕ ДОСТИЖЕНИЯ ===
    idx = insert_text_run(service, doc_id, "КЛЮЧЕВЫЕ ДОСТИЖЕНИЯ\n", bold=True, font_size=13, index=idx)
    highlights_str = "  |  ".join([f"{num} {label}" for num, label in data['highlights']]) + "\n"
    idx = insert_text(service, doc_id, highlights_str, index=idx)
    idx = insert_text(service, doc_id, data['summary'] + "\n\n", index=idx)

    # === НАВЫКИ ===
    idx = insert_text_run(service, doc_id, "НАВЫКИ\n", bold=True, font_size=13, index=idx)
    for skill in data['skills']:
        idx = insert_text_run(service, doc_id, skill['title'], bold=True, font_size=11, index=idx)
        idx = insert_text_run(service, doc_id, f" ({skill['tag']})\n", italic=True, font_size=9, color={'red': 0.02, 'green': 0.59, 'blue': 0.41}, index=idx)
        for item in skill['items']:
            idx = insert_text(service, doc_id, "• " + item + "\n", index=idx)
        idx = insert_text(service, doc_id, "\n", index=idx)

    # === ОПЫТ РАБОТЫ ===
    idx = insert_text_run(service, doc_id, "ОПЫТ РАБОТЫ\n", bold=True, font_size=13, index=idx)
    for job in data['experience']:
        idx = insert_text_run(service, doc_id, job['title'], bold=True, font_size=11, index=idx)
        idx = insert_text(service, doc_id, f"  |  {job['company']}  |  {job['date']}\n", index=idx)
        for item in job['items']:
            idx = insert_text(service, doc_id, "• " + item + "\n", index=idx)
        idx = insert_text(service, doc_id, "\n", index=idx)

    # === ОБРАЗОВАНИЕ ===
    idx = insert_text_run(service, doc_id, "ОБРАЗОВАНИЕ\n", bold=True, font_size=13, index=idx)
    for edu in data['education']:
        idx = insert_text_run(service, doc_id, edu['school'], bold=True, font_size=10.5, index=idx)
        idx = insert_text(service, doc_id, f"  |  {edu['meta']}\n", index=idx)
        idx = insert_text(service, doc_id, edu['detail'] + "\n", index=idx)
        if edu.get('extra'):
            idx = insert_text_run(service, doc_id, edu['extra'] + "\n", italic=True, font_size=9, color={'red': 0.4, 'green': 0.4, 'blue': 0.4}, index=idx)
        idx = insert_text(service, doc_id, "\n", index=idx)

    # === ЯЗЫКИ ===
    idx = insert_text_run(service, doc_id, "ЯЗЫКИ\n", bold=True, font_size=13, index=idx)
    for lang, level in data['languages']:
        idx = insert_text_run(service, doc_id, lang + " — ", bold=True, index=idx)
        idx = insert_text(service, doc_id, level + "\n", index=idx)
    idx = insert_text(service, doc_id, "\n", index=idx)

    # === ПРОЕКТЫ ===
    idx = insert_text_run(service, doc_id, "ПРОЕКТЫ\n", bold=True, font_size=13, index=idx)
    idx = insert_text(service, doc_id, f"Подробные кейсы и портфолио: {data['projects_link']}\n\n", index=idx)

    # === P.S. ===
    idx = insert_text(service, doc_id, data['ps'] + "\n", index=idx)

    print(" Резюме успешно обновлено в Google Docs!")
    print(f" Ссылка: https://docs.google.com/document/d/{doc_id}/edit")


def main():
    print(" Авторизация через Google OAuth...")
    creds = get_credentials()
    service = build('docs', 'v1', credentials=creds)

    print(" Очистка документа...")
    clear_document(service, DOCUMENT_ID)

    print(" Загрузка резюме...")
    build_resume(service, DOCUMENT_ID)

    print("\n Готово!")


if __name__ == "__main__":
    main()
