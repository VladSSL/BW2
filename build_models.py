#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Генератор страниц моделей для сайта НПК Механик.

Запуск:  python3 build_models.py
Результат: models/*.html
"""

import os
import html

CDN = "https://static.tildacdn.com/"

MODELS = [
    {
        "slug": "mehanik-800",
        "name": "Механик 800",
        "kind": "Внутренняя расточка и наплавка",
        "img": "tild3230-3064-4339-b461-643437363966/800.jpg",
        "lead": "Самая крупная модель линейки: расточка и наплавка отверстий до 800 мм. "
                "Беспроводной контроллер HMI и борштанга ⌀90 мм для тяжёлых работ.",
        "specs": [
            ("Диапазон внутренней расточки", "100–800 мм"),
            ("Диапазон внутренней наплавки", "100–800 мм"),
            ("Контроллер", "Беспроводной HMI «Смарт»"),
            ("Борштанга", "90×2600 мм"),
            ("Частота вращения борштанги", "45 об/мин"),
        ],
        "highlights": [
            "Максимальный диапазон обработки в линейке",
            "Беспроводной пульт HMI со сценариями наплавки",
            "Усиленная борштанга ⌀90 мм длиной 2600 мм",
            "Телескопический наплавочный вал в комплекте",
        ],
    },
    {
        "slug": "mehanik-500-bc",
        "name": "Механик 500 ВС",
        "kind": "Внутренняя расточка и наплавка",
        "img": "tild6265-3332-4262-b534-373733636338/500_.jpg",
        "lead": "Универсальная двухскоростная модель для сервисных участков: "
                "две передачи, две борштанги в комплекте, беспроводной контроллер.",
        "specs": [
            ("Диапазон внутренней расточки", "52–600 мм"),
            ("Диапазон внутренней наплавки", "40–600 мм"),
            ("Контроллер", "Беспроводной HMI «Смарт»"),
            ("Борштанги", "50×1600 мм; 50×750 мм с конусом Морзе МТ4"),
            ("Частота вращения борштанги", "1 передача — 200 об/мин; 2 передача — 400 об/мин"),
        ],
        "highlights": [
            "Две передачи под разные диаметры и материалы",
            "Короткая борштанга с конусом Морзе МТ4 для стеснённых мест",
            "Беспроводной пульт HMI «Смарт»",
            "Секторная и цилиндрическая наплавка в автоматическом режиме",
        ],
    },
    {
        "slug": "mehanik-600",
        "name": "Механик 600",
        "kind": "Внутренняя расточка и наплавка",
        "img": "tild3732-3334-4138-a136-326166353161/600.jpg",
        "lead": "Модель с длинной борштангой ⌀60 мм и повышенными оборотами — "
                "для протяжённых соосных отверстий.",
        "specs": [
            ("Диапазон внутренней расточки", "62–600 мм"),
            ("Диапазон внутренней наплавки", "50–600 мм"),
            ("Контроллер", "Беспроводной HMI «Смарт»"),
            ("Борштанга", "60×2000 мм"),
            ("Частота вращения борштанги", "250 об/мин"),
        ],
        "highlights": [
            "Борштанга 60×2000 мм для длинных проушин",
            "250 об/мин — выше производительность точения",
            "Беспроводной контроллер HMI",
            "Автоматическая подача до 200 мм за шаг",
        ],
    },
    {
        "slug": "mehanik-300-optimum",
        "name": "Механик 300 Оптимум",
        "kind": "Внутренняя расточка и наплавка",
        "img": "tild6264-6366-4639-b266-383430396339/300_.jpg",
        "lead": "Оптимальный баланс диапазона и цены: закрывает большинство "
                "ремонтных задач по спецтехнике и промышленному оборудованию.",
        "specs": [
            ("Диапазон внутренней расточки", "52–400 мм"),
            ("Диапазон внутренней наплавки", "40–400 мм"),
            ("Контроллер", "«Смарт»"),
            ("Борштанги", "50×1600 мм; 50×750 мм"),
            ("Частота вращения борштанги", "200 об/мин"),
        ],
        "highlights": [
            "Диапазон 52–400 мм закрывает типовые ремонты",
            "Две борштанги в комплекте",
            "Контроллер «Смарт» с контролем длины расточки",
            "Измерительная головка с точностью 0,01 мм",
        ],
    },
    {
        "slug": "mehanik-250-bc",
        "name": "Механик 250 ВС",
        "kind": "Внутренняя расточка и наплавка",
        "img": "tild6231-3763-4564-b833-616662393536/250_.jpg",
        "lead": "Компактная высокооборотистая модель — 360 об/мин "
                "и беспроводной контроллер при малых габаритах станка.",
        "specs": [
            ("Диапазон внутренней расточки", "52–300 мм"),
            ("Диапазон внутренней наплавки", "40–300 мм"),
            ("Контроллер", "Беспроводной HMI «Смарт»"),
            ("Борштанги", "50×1600 мм; 50×750 мм с конусом Морзе МТ4"),
            ("Частота вращения борштанги", "360 об/мин"),
        ],
        "highlights": [
            "360 об/мин — чистая поверхность на малых диаметрах",
            "Габариты 440×250×580 мм для труднодоступных мест",
            "Беспроводной пульт HMI",
            "Конус Морзе МТ4 на короткой борштанге",
        ],
    },
    {
        "slug": "mehanik-200-pro",
        "name": "Механик 200 ПРО",
        "kind": "Внутренняя расточка и наплавка",
        "img": "tild3861-6337-4366-b764-386430666361/200_.jpg",
        "lead": "Рабочая лошадка для отверстий до 200 мм: контроллер «Смарт», "
                "борштанга 50×1600 мм, автоматическая наплавка.",
        "specs": [
            ("Диапазон внутренней расточки", "52–200 мм"),
            ("Диапазон внутренней наплавки", "40–200 мм"),
            ("Контроллер", "«Смарт»"),
            ("Борштанга", "50×1600 мм"),
            ("Частота вращения борштанги", "200 об/мин"),
        ],
        "highlights": [
            "Оптимален для проушин и посадочных мест до 200 мм",
            "Автоматическая секторная и цилиндрическая наплавка",
            "Усиленные суппорта на алюминиевых ножках",
            "Нутромер для замера без снятия борштанги",
        ],
    },
    {
        "slug": "mehanik-econom",
        "name": "Механик Эконом",
        "kind": "Внутренняя расточка и наплавка",
        "img": "tild3233-3963-4365-a334-643431613736/200_.jpg",
        "lead": "Стартовая модель с базовым контроллером и двумя борштангами — "
                "минимальный порог входа в расточку и наплавку.",
        "specs": [
            ("Диапазон внутренней расточки", "37–200 мм"),
            ("Диапазон внутренней наплавки", "50–200 мм"),
            ("Контроллер", "Базовый"),
            ("Борштанги", "50×1600 мм; 35×1200 мм"),
        ],
        "highlights": [
            "Расточка от 37 мм — самый малый диаметр в линейке",
            "Две борштанги: 50 мм и 35 мм",
            "Базовый контроллер, простое освоение",
            "Наплавочный вал в комплекте",
        ],
    },
    {
        "slug": "mehanik-nt-350",
        "name": "Механик НТ 350",
        "kind": "Наружное точение и наплавка",
        "img": "tild3635-3866-4562-a563-313062666237/D0BDD18220350.jpg",
        "lead": "Станок наружного точения: восстановление валов и осей "
                "диаметром до 350 мм с нарезанием резьбы.",
        "specs": [
            ("Диапазон наружного точения", "150–350 мм"),
            ("Диапазон наружной наплавки", "150–300 мм"),
            ("Обрабатываемая длина", "до 400 мм за проход"),
            ("Нарезание резьбы", "с шагом 1–3 мм"),
        ],
        "highlights": [
            "Обработка до 400 мм за один проход",
            "Нарезание резьбы с шагом 1–3 мм",
            "Наплавка изношенных шеек валов",
            "Работа без демонтажа детали",
        ],
    },
    {
        "slug": "mehanik-nt-200",
        "name": "Механик НТ 200",
        "kind": "Наружное точение и наплавка",
        "img": "tild3039-3931-4430-b631-393833333137/D0BDD18220200.jpg",
        "lead": "Компактная версия станка наружного точения для валов "
                "диаметром от 50 до 210 мм.",
        "specs": [
            ("Диапазон наружного точения", "50–210 мм"),
            ("Диапазон наружной наплавки", "50–160 мм"),
            ("Обрабатываемая длина", "до 300 мм за проход"),
            ("Нарезание резьбы", "с шагом 1–3 мм"),
        ],
        "highlights": [
            "Точение от 50 мм — малые валы и штоки",
            "До 300 мм за проход",
            "Нарезание резьбы с шагом 1–3 мм",
            "Малый вес и быстрая установка",
        ],
    },
    {
        "slug": "mehanik-nf",
        "name": "Механик НФ",
        "kind": "Обработка фланцев и торцов",
        "img": "tild3337-3531-4132-b939-666537373734/photo.jpg",
        "lead": "Станок для обработки фланцевых и торцевых поверхностей "
                "с чистотой Ra 1,6–3,2 по стали, нержавейке и алюминию.",
        "specs": [
            ("Диапазон диаметров обработки", "25–350 мм"),
            ("Материалы", "Углеродистая сталь, нержавеющая сталь, алюминий"),
            ("Чистота поверхности", "Ra 1,6–3,2"),
        ],
        "highlights": [
            "Чистота поверхности Ra 1,6–3,2",
            "Работа по стали, нержавейке и алюминию",
            "Диаметры обработки 25–350 мм",
            "Восстановление уплотнительных поверхностей фланцев",
        ],
    },
]

HEADER = """<header class="header">
  <div class="wrap header__inner">
    <a class="logo" href="../index.html" aria-label="НПК Механик — на главную">
      <svg class="logo__mark" viewBox="0 0 32 32" aria-hidden="true">
        <path d="M2 4h28L16 30Z" fill="#0A0A0A"/>
        <path d="M9 9h11l-6.5 12L9 9Z" fill="#fff"/>
        <path d="M13.5 9h3.5l-1.8 3.4L13.5 9Z" fill="#E11D2E"/>
      </svg>
      <span class="logo__text">
        <span class="logo__name">Механик<span>.</span></span>
        <span class="logo__sub">научно-производственная компания</span>
      </span>
    </a>
    <nav class="nav" aria-label="Основная навигация">
      <a href="../index.html#models">Модельный ряд</a>
      <a href="../index.html#features">Конструкция</a>
      <a href="../index.html#video">Видео</a>
      <a href="../index.html#options">Опции</a>
      <a href="../index.html#contacts">Контакты</a>
    </nav>
    <div class="header__actions">
      <a class="phone" href="tel:+73433455888">+7 343 345 58 88</a>
      <a class="btn btn--sm" href="#request">Получить предложение</a>
      <button class="burger" type="button" data-burger aria-expanded="false" aria-controls="mobile-nav" aria-label="Меню">
        <span></span>
      </button>
    </div>
  </div>
</header>

<div class="mobile-nav" id="mobile-nav" data-mobile-nav data-open="false">
  <a href="../index.html#models">Модельный ряд</a>
  <a href="../index.html#features">Конструкция</a>
  <a href="../index.html#video">Видео</a>
  <a href="../index.html#options">Опции</a>
  <a href="../index.html#geo">География продаж</a>
  <a href="../index.html#contacts">Контакты</a>
  <a class="btn btn--accent btn--block" href="#request">Получить предложение</a>
  <p class="mobile-nav__meta">
    <a href="tel:+73433455888">+7 343 345 58 88</a><br>
    <a href="mailto:info@maspel.ru">info@maspel.ru</a>
  </p>
</div>"""

FOOTER = """<footer class="footer">
  <div class="wrap">
    <div class="grid12 footer__grid">
      <div class="footer__brand">
        <a class="logo" href="../index.html" aria-label="НПК Механик">
          <svg class="logo__mark" viewBox="0 0 32 32" aria-hidden="true">
            <path d="M2 4h28L16 30Z" fill="#0A0A0A"/>
            <path d="M9 9h11l-6.5 12L9 9Z" fill="#fff"/>
            <path d="M13.5 9h3.5l-1.8 3.4L13.5 9Z" fill="#E11D2E"/>
          </svg>
          <span class="logo__text">
            <span class="logo__name">Механик<span>.</span></span>
            <span class="logo__sub">научно-производственная компания</span>
          </span>
        </a>
      </div>
      <div class="footer__col">
        <h4>Каталог</h4>
        <ul>{catalog_a}</ul>
      </div>
      <div class="footer__col">
        <h4>Ещё модели</h4>
        <ul>{catalog_b}</ul>
      </div>
      <div class="footer__col">
        <h4>Клиентам</h4>
        <ul>
          <li><a href="../index.html#geo">География продаж</a></li>
          <li><a href="../index.html#payment">Оплата и лизинг</a></li>
          <li><a href="../index.html#options">Опции</a></li>
          <li><a href="../index.html#contacts">Контакты</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4>Связь</h4>
        <ul>
          <li><a href="tel:+73433455888">+7 343 345 58 88</a></li>
          <li><a href="mailto:info@maspel.ru">info@maspel.ru</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__legal">
      <p>ООО «НПК Механик» · Екатеринбург</p>
      <p>Не является публичной офертой</p>
    </div>
  </div>
</footer>"""

PAGE = """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name} — характеристики и цена | НПК Механик</title>
<meta name="description" content="{meta}">
<meta name="theme-color" content="#0A0A0A">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://static.tildacdn.com">
<link rel="stylesheet" href="../assets/css/style.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Product","name":"{name}","category":"{kind}","brand":{{"@type":"Brand","name":"Механик"}},"manufacturer":{{"@type":"Organization","name":"НПК Механик"}}}}
</script>
</head>
<body>

<a class="skip-link" href="#main">Перейти к содержанию</a>

{header}

<main id="main">

  <div class="wrap">
    <nav class="crumbs" aria-label="Хлебные крошки">
      <a href="../index.html">Главная</a><span aria-hidden="true">/</span>
      <a href="../index.html#models">Модельный ряд</a><span aria-hidden="true">/</span>
      <span>{name}</span>
    </nav>
  </div>

  <section class="section section--tight">
    <div class="wrap">
      <div class="grid12 split">
        <div class="split__copy" data-reveal>
          <p class="eyebrow">{kind}</p>
          <h1 class="h1" style="margin-top:12px">{name}</h1>
          <p class="lead" style="margin-top:20px;max-width:44ch">{lead}</p>
          <div class="hero__cta">
            <a class="btn" href="#request">Запросить цену</a>
            <a class="btn btn--ghost" href="../index.html#models">Все модели</a>
          </div>
        </div>
        <figure class="split__media" data-reveal data-reveal-delay="100">
          <img src="{cdn}{img}" alt="{name} — расточно-наплавочный станок" width="800" height="600" fetchpriority="high">
        </figure>
      </div>
    </div>
  </section>

  <section class="section section--paper2">
    <div class="wrap">
      <div class="grid12">
        <div class="split__copy" data-reveal>
          <div class="section-head">
            <div><p class="eyebrow">Характеристики</p><h2 class="h2">Технические<br>параметры</h2></div>
            <span class="idx">01 / СПЕЦИФИКАЦИЯ</span>
          </div>
          <table class="spec-table">
            <caption class="sr-only">Технические характеристики {name}</caption>
            <tbody>
{spec_rows}
            </tbody>
          </table>
        </div>
        <div class="split__copy" data-reveal data-reveal-delay="100">
          <div class="section-head">
            <div><p class="eyebrow">Преимущества</p><h2 class="h2">Что даёт<br>эта модель</h2></div>
            <span class="idx">02 / ПРЕИМУЩЕСТВА</span>
          </div>
          <ul class="checklist">
{highlight_rows}
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section cta-block" id="request">
    <div class="wrap">
      <div class="grid12">
        <div class="cta__copy" data-reveal>
          <p class="eyebrow">Заявка</p>
          <h2 class="h2">Цена и сроки<br>на {name}</h2>
          <p class="lead" style="margin-top:20px">Опишите задачу — инженер подтвердит комплектацию и назовёт цену.</p>
        </div>
        <div class="cta__form" data-reveal data-reveal-delay="100">
          <form class="form" data-form novalidate>
            <div class="field">
              <label for="f-name">Имя <span class="req" aria-hidden="true">*</span></label>
              <input id="f-name" name="name" type="text" autocomplete="name" placeholder="Иван Петров" required>
              <span class="err" aria-live="polite"></span>
            </div>
            <div class="field">
              <label for="f-phone">Телефон <span class="req" aria-hidden="true">*</span></label>
              <input id="f-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" placeholder="+7 (900) 000-00-00" required>
              <span class="err" aria-live="polite"></span>
            </div>
            <div class="field field--full">
              <label for="f-task">Задача</label>
              <textarea id="f-task" name="task" rows="3" placeholder="Диаметр отверстия, длина, материал детали">{name}. </textarea>
              <span class="err" aria-live="polite"></span>
            </div>
            <div class="form__foot">
              <p class="form__note">Нажимая кнопку, вы соглашаетесь с обработкой персональных данных.</p>
              <button class="btn" type="submit">Отправить заявку</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>

  <section class="section" aria-label="Другие модели">
    <div class="wrap">
      <div class="section-head" data-reveal>
        <div><p class="eyebrow">Смотрите также</p><h2 class="h2">Другие модели</h2></div>
        <span class="idx">03 / КАТАЛОГ</span>
      </div>
      <div class="models">
{related}
      </div>
    </div>
  </section>

</main>

{footer}

<script src="../assets/js/main.js" defer></script>
</body>
</html>
"""

ARROW = ('<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">'
         '<path d="M3 8h10m0 0-4-4m4 4-4 4" stroke="currentColor" stroke-width="1.5"/></svg>')


def esc(s):
    return html.escape(s, quote=True)


def related_card(m, delay):
    first_two = "".join(
        '<div><dt>{}</dt><dd>{}</dd></div>'.format(esc(k), esc(v))
        for k, v in m["specs"][:2]
    )
    return (
        '        <article class="model" data-reveal data-reveal-delay="{d}">\n'
        '          <div class="model__media"><img src="{cdn}{img}" alt="{name}" loading="lazy" width="600" height="450"></div>\n'
        '          <div class="model__body">\n'
        '            <p class="model__kind">{kind}</p>\n'
        '            <h3 class="model__name">{name}</h3>\n'
        '            <dl class="model__specs">{specs}</dl>\n'
        '            <div class="model__foot"><a class="link-arrow" href="{slug}.html">Подробнее {arrow}</a></div>\n'
        '          </div>\n'
        '        </article>'
    ).format(d=delay, cdn=CDN, img=m["img"], name=esc(m["name"]),
             kind=esc(m["kind"]), specs=first_two, slug=m["slug"], arrow=ARROW)


def build():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
    os.makedirs(out_dir, exist_ok=True)

    cat_a = "".join('<li><a href="{}.html">{}</a></li>'.format(m["slug"], esc(m["name"]))
                    for m in MODELS[:5])
    cat_b = "".join('<li><a href="{}.html">{}</a></li>'.format(m["slug"], esc(m["name"]))
                    for m in MODELS[5:])
    footer = FOOTER.format(catalog_a=cat_a, catalog_b=cat_b)

    for i, m in enumerate(MODELS):
        spec_rows = "\n".join(
            '              <tr><th scope="row">{}</th><td>{}</td></tr>'.format(esc(k), esc(v))
            for k, v in m["specs"]
        )
        highlight_rows = "\n".join(
            '            <li>{}</li>'.format(esc(h)) for h in m["highlights"]
        )
        others = [x for x in MODELS if x["slug"] != m["slug"]][i % 4: i % 4 + 3]
        if len(others) < 3:
            others = [x for x in MODELS if x["slug"] != m["slug"]][:3]
        related = "\n".join(related_card(o, n * 60) for n, o in enumerate(others))

        meta = "{} — {}. {}".format(m["name"], m["kind"].lower(), m["lead"])

        page = PAGE.format(
            name=esc(m["name"]),
            kind=esc(m["kind"]),
            lead=esc(m["lead"]),
            meta=esc(meta[:180]),
            cdn=CDN,
            img=m["img"],
            spec_rows=spec_rows,
            highlight_rows=highlight_rows,
            related=related,
            header=HEADER,
            footer=footer,
        )

        path = os.path.join(out_dir, m["slug"] + ".html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(page)
        print("→", os.path.relpath(path))

    print("\nГотово: {} страниц.".format(len(MODELS)))


if __name__ == "__main__":
    build()
