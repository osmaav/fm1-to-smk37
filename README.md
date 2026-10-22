# FM-1 → SMK-37: запустите прошивку FM-1 на SMK-37

![Прошивка FM-1 для SMK-37](assets/hero.png)

<!-- Русская версия: 1.1.0 (22.10.2026). Локализация репозитория fm1-to-smk37; при изменении обновляйте версию по SemVer. -->

> **Локализация на русский язык (версия 1.1.0, 22.10.2026):** весь набор переведён на русский язык —
> README, `AGENTS.md`, конфигурация `smk37-port.yaml`, инструменты и **вся документация в `docs/`**
> (01–08, 10) полностью переведены. Технические идентификаторы (имена файлов, команд, макросов, регистров)
> оставлены без перевода для сохранения работоспособности. При изменении документации обновляйте версию
> локализации по SemVer в версионном комментарии каждого файла.

Набор (кит) для переноса открытых прошивок M-Vave FM-1 на M-Vave SMK-37 с помощью кодирующего агента,
например Claude Code, а также для разработки под обе платы из одного исходника.

[Сайт](https://genkigenki.github.io/smk37/kit.html) ·
[Плейбук агента](AGENTS.md) · [Паттерны назначений](docs/06-mapping-patterns.md) ·
[Файл настройки](smk37-port.yaml) · [Разработка под обе платы](docs/07-develop-for-both.md) · [Подводные камни](docs/08-pitfalls.md) · [Установка портов](https://genkigenki.github.io/smk37/) · автор — **genkigenki**

## Шаги переноса

1. **Запустите [Claude Code](https://claude.com/claude-code)** в пустой папке на ПК (Windows с WSL или Linux) и вставьте подсказку.
   Агент клонирует прошивку и этот набор и настроит инструментарий; каждую команду вы подтверждаете:
   ```text
   Clone <firmware repo> and github.com/genkigenki/fm1-to-smk37, then port the firmware to the
   SMK-37. Follow fm1-to-smk37/AGENTS.md step by step.
   Ask me the setup questions first. Keep the FM-1 build byte-identical.
   Never write the protected flash ranges. Ask me before you flash the SMK-37.
   ```
   (Подсказку оставляем на английском: она рассчитана на англоязычные модели и репозитории.)
2. **Ответьте на вопросы.** Что должны делать 16 пэдов, 4 фейдера, 10 внешних клавиш, колёса и ручки? Claude
   занесёт ваши ответы в [`smk37-port.yaml`](smk37-port.yaml); варианты показывают [паттерны назначений](docs/06-mapping-patterns.md)
   и [примеры](examples/).
3. **Доверьтесь сборке.** Claude проходит по [`AGENTS.md`](AGENTS.md): базовая сборка, слой платы (коммиты SLOOP
   для форков SLOOP, коммиты Felucca для форков Felucca), хранилище, органы управления, все три модели, тесты.
   Он останавливается после каждой области, чтобы вы могли проверить результат. Сборка FM-1 остаётся байт-в-байт идентичной.
4. **Железо — ваша часть.** Сначала полная резервная копия флеш-памяти, затем установка, игра и обратная связь Claude:
   что работает, а что нет (или вставьте лог последовательного порта). Он исправляет, пересобирает — вы ставите снова.
5. **Отправьте вверх по течению.** Pull request в исходную прошивку: всё спрятано за `BOARD_SMK37`, собственное имя
   и облик проекта, нейтральный `SMK37.md` и одна строка в README. Пока PR не принят, сборка живёт в вашем форке
   оригинала с релизами там же.

Любой другой кодирующий агент, способный читать `AGENTS.md` и запускать shell, тоже подойдёт. Как всегда — на свой риск.

## Уже перенесено этим способом

| Порт | Откуда | Что добавляет SMK | Upstream |
|---|---|---|---|
| [Makkuro37](https://github.com/genkigenki/Makkuro37) | новая прошивка | пэды гейтят восемь дрон-голосов, пэд CHAOS, банки фейдеров | |
| [SLOOP, сборка SMK-37](https://github.com/genkigenki/sloop-fm1/tree/smk37) | [SLOOP](https://github.com/isod89/sloop-fm1) | пэды в цветах дорожек, выбор звука пэдом, банки фейдеров, внешние клавиши-драммы. Эталонный порт. | [isod89/sloop-fm1#112](https://github.com/isod89/sloop-fm1/pull/112) (железо), [#130](https://github.com/isod89/sloop-fm1/pull/130) (необязательный облик Snoop37, ветка [snoop37](https://github.com/genkigenki/sloop-fm1/tree/snoop37)) |
| [X0X, сборка SMK-37](https://github.com/genkigenki/fm1-x0x/tree/smk37) | [fm1-x0x](https://github.com/charlesvestal/fm1-x0x) | пэды как 16-шаговая сетка | [charlesvestal/fm1-x0x#13](https://github.com/charlesvestal/fm1-x0x/pull/13) |
| [FoMni, сборка SMK-37](https://github.com/genkigenki/fm1-fomni/tree/smk37) | [fm1-fomni](https://github.com/charlesvestal/fm1-fomni) | пэды как пластина для боя, аккорды держатся на клавиатуре | [charlesvestal/fm1-fomni#2](https://github.com/charlesvestal/fm1-fomni/pull/2) |
| [MAKU, сборка SMK-37](https://github.com/genkigenki/Felucca/tree/maku-smk37-2) | [maku](https://github.com/okumurari2/maku) | машина эмбиента: ревербы на кнопках и колёсах | [okumurari2/maku#4](https://github.com/okumurari2/maku/pull/4) |
| [Rainbow mode, сборка SMK-37](https://github.com/genkigenki/Felucca/tree/rainbow-smk37) | [felucca-rainbow](https://github.com/joshbartlettband-web/felucca-rainbow) | игрушка для детей: пэды в цветах нот, ограничение громкости на K1, без меню; полная Felucca по комбинации | [joshbartlettband-web/felucca-rainbow#1](https://github.com/joshbartlettband-web/felucca-rainbow/pull/1) |
| [GHOULBOX, сборка SMK-37](https://github.com/genkigenki/Felucca/tree/ghoulbox-smk37) | [ghoulbox-fm1-dungeon-synth](https://github.com/jasonpersinger/ghoulbox-fm1-dungeon-synth) | внешние клавиши через клавишный путь (аккорды, лаг дрона, сплиты), банки фейдеров | [jasonpersinger/ghoulbox-fm1-dungeon-synth#5](https://github.com/jasonpersinger/ghoulbox-fm1-dungeon-synth/pull/5) |
| [Felucca, сборка SMK-37](https://github.com/genkigenki/Felucca/tree/smk37) | [Felucca](https://github.com/hugelton/Felucca) | SMK-37 как целевая плата | [hugelton/Felucca#237](https://github.com/hugelton/Felucca/pull/237) |

Все они устанавливаются из браузера: **[genkigenki.github.io/smk37](https://genkigenki.github.io/smk37/)**.

## Почему это работает

У FM-1 живая сцена открытых прошивок. Всё началось с
[Felucca](https://github.com/hugelton/Felucca) работы Leo Kuroshita / Hügelton Instruments, за ней последовали форки
[SLOOP](https://github.com/isod89/sloop-fm1), [sloopDX](https://github.com/zvenson/dxsloop),
[X0X](https://github.com/charlesvestal/fm1-x0x), [FoMni-1](https://github.com/charlesvestal/fm1-fomni) и
[Melodee](https://github.com/keremimo/melodee). SMK-37 — 37-клавишный контроллер с 16 RGB-пэдами,
8 энкодерами, 4 фейдерами, колёсами питча и модуляции, цветным экраном и встроенным синтезатором. Внутри —
**тот же чип JieLi AC791N (WL82)**, что у FM-1, тот же второй стадия загрузчика, тот же загрузчик обновлений
и тот же ключ чипа. Отличается только разводка панели.

## Содержание набора

- [`AGENTS.md`](AGENTS.md) — плейбук: пошаговый порядок переноса для кодирующего агента.
- [`smk37-port.yaml`](smk37-port.yaml) — все решения одного порта в одном файле.
- [`docs/`](docs/) — документация: железо, обновление и восстановление, шаги переноса, назначения органов
  управления, реверс-инжиниринг, паттерны назначений, разработка под обе платы, подводные камни, обратный порт.
- [`examples/`](examples/) — заполненные файлы настройки для состоявшихся портов.
- [`tools/make_panels.py`](tools/make_panels.py) — рисование схем панели SMK-37 для документации.
- [`assets/`](assets/) — изображения панели и обложки.

## Лицензия

См. [LICENSE](LICENSE).
