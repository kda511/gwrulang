# GoldWave Russian Localization Guide

You are translating the user interface and messages of **GoldWave**, a professional digital audio editor, from English into **natural, correct Russian**.

## Goal

Produce translations that a Russian audio engineer or home user would expect to see in a polished Russian version of GoldWave. Translate meaning, not words. Avoid machine-translation calques.

## Output format

Return **only valid JSON** (UTF-8) in this exact shape, with every input id translated:

```json
{
  "0": "Управление",
  "1": "Громкость"
}
```

Do not add comments, markdown, or explanations. Keep ids exactly as given. Every id from the input must be present exactly once.

## Hard formatting rules

These characters are functional. Their count and relative placement must be preserved exactly:

- `%0%`, `%1%`, `%2%`, `%3%`, `%d`, `%.2lf`, `%ls`, `%%` — placeholders. Never translate, remove, or add percent sequences. In `Forms`, a bare `%` is a unit (percent); keep it.
- `|` — separates message sections or a menu caption from its hint. Keep **the same number** of `|` characters in the same order. Translate each section.
- `\n` and real newlines — keep the same number of newlines in the same relative places. Translate line by line.
- `{` and `}` — start/finish marker symbols. Keep both symbols and keep them next to the relevant word (for example `маркер начала {`, `маркер конца }`).
- `&` — menu accelerator. Keep exactly one `&` where the English string has one. Put it before a sensible Russian letter (or before the same digit/symbol token). Do not add a second `&`.
- Leading and trailing spaces — preserve them if present (for example `" Play &1 "`).
- Format strings such as `%Y-%m-%d, %H:%M:%S` — leave unchanged.
- Quotes: use Russian «…» where quotes are needed, but preserve quoted UI labels/placeholders.
- Keep trailing punctuation (`:`, `...`, `?`, `!`) unless Russian grammar requires a different mark. Keep the colon in labels.

## Translation rules

1. Use **sentence case** for Russian labels and menu items: capitalize the first word only, plus proper nouns. Do not copy English Title Case.
2. Commands use the infinitive or imperative naturally: `Save` → `Сохранить`, `Close` → `Закрыть`.
3. Labels ending in a colon keep the colon: `Volume (dB):` → `Громкость (дБ):`.
4. Use `вы` (lowercase) in messages. Prefer direct, concise instructions. Omit `Пожалуйста` unless it sounds natural.
5. Do not translate product names, company names, codec/format names, file extensions, acronyms, URLs, e-mail addresses, or keyboard key names such as `Ctrl`, `Alt`, `Shift`, `Esc`, `Tab`, `Home`, `End`, `F1`.
6. Translate units: `dB` → `дБ`, `Hz` → `Гц`, `kHz` → `кГц`, `MHz` → `МГц`, `s` (seconds) → `с`, `ms` → `мс`, `bit` → `бит`, `kbps` → `кбит/с`, `fps` → `кадр/с`.
7. Use a decimal comma in ordinary Russian text and display values (`0,25`; `-2,5 дБ`). Never change numbers inside placeholders or format strings.
8. If a string is a pure number, timecode, color code, file pattern, technical identifier (for example `DopplerEffectForm`, `ShapeBox`, `MP3`, `PCM 16 bit` is *not* pure), or otherwise has no translatable words, return it unchanged.
9. If a string looks like a class/control identifier in `Caption` (CamelCase ending in `Form`, `Frame`, `Box`, `Page`), leave it unchanged unless it is clearly a display title.
10. Preset names should be short, natural Russian names (usually noun phrases), not literal word-for-word renderings.
11. Keep the meaning of the original exactly. Do not add features, warnings, or explanations.
12. Avoid anglicisms where a normal Russian term exists. Technical terms listed below are mandatory.

## Mandatory glossary

Use these translations consistently. The left column is English, the right column is the required Russian term (case may be adjusted to fit the sentence).

### Interface and editing

| English | Russian |
|---|---|
| Control (window) | Управление / Окно управления |
| Control Properties | Свойства управления |
| Volume | Громкость |
| Balance | Баланс |
| Speed | Скорость |
| Play | Воспроизведение / Воспроизвести |
| Pause | Пауза |
| Stop | Стоп / Остановить |
| Record | Запись / Записать |
| Rewind | Перемотка назад |
| Fast forward | Перемотка вперёд |
| Skip | Пропуск |
| Loop | Повтор |
| Looping | Повторение |
| Marker | Маркер |
| Start marker | Маркер начала |
| Finish marker | Маркер конца |
| Selection | Выделение |
| Selected | Выделенный |
| Unselected | Невыделенный / вне выделения |
| Cue point, cue | Метка |
| Cue list | Список меток |
| Waveform | Форма сигнала |
| View | Вид / Показать |
| Zoom | Масштаб |
| Zoom in | Увеличить масштаб |
| Zoom out | Уменьшить масштаб |
| Scroll | Прокрутка |
| Window | Окно |
| Toolbar | Панель инструментов |
| Status bar | Строка состояния |
| Button | Кнопка |
| Tab | Вкладка |
| Slider / fader | Регулятор |
| Check box | Флажок |
| List | Список |
| Column | Столбец |
| Grid | Сетка |
| Axis / axes | Ось / оси |
| Ruler | Линейка |
| Clipboard | Буфер обмена |
| File | Файл |
| Folder | Папка |
| Filename | Имя файла |
| Path | Путь |
| Format | Формат |
| File type | Тип файла |
| Extension | Расширение |
| Attributes | Атрибуты |
| Audio attributes | Атрибуты звука |
| Sample rate / sampling rate | Частота дискретизации |
| Bit | Бит |
| Bit depth | Разрядность |
| Channel | Канал |
| Mono | Моно |
| Stereo | Стерео |
| Left | Левый |
| Right | Правый |
| Center | Центральный |
| Front | Передний |
| Back | Задний |
| Side | Боковой |
| LFE / subwoofer | LFE / сабвуфер |
| Device | Устройство |
| Playback device | Устройство воспроизведения |
| Recording device | Устройство записи |
| Quality | Качество |
| Shared | Общий |
| Exclusive | Монопольный |
| Latency | Задержка |
| Monitor input | Мониторинг входа |
| Level activated | Активация по уровню |
| Prebuffer | Предбуфер |
| Bounded | В пределах выделения |
| Unbounded | Без ограничения |
| Auto save | Автосохранение |
| Timer | Таймер |
| Dictation mode | Режим диктовки |
| Master control | Общий уровень |
| Mute all | Отключить звук |
| Alternative initialization | Альтернативная инициализация |

### Menus and commands

| English | Russian |
|---|---|
| File | Файл |
| Edit | Правка |
| Effect | Эффект |
| View | Вид |
| Tool | Инструмент |
| Options | Параметры |
| Window | Окно |
| Help | Справка |
| New | Создать |
| Open | Открыть |
| Open URL | Открыть URL |
| Recent | Недавние |
| Close | Закрыть |
| Close All | Закрыть все |
| Information | Сведения |
| Save | Сохранить |
| Save As | Сохранить как |
| Save All | Сохранить все |
| Save Selection As | Сохранить выделение как |
| Exit | Выход |
| Undo | Отменить |
| Redo | Повторить |
| Cut | Вырезать |
| Copy | Копировать |
| Copy To | Копировать в |
| Paste | Вставить |
| Paste New | Вставить как новый |
| Mix | Смешать |
| Crossfade | Кроссфейд |
| Overwrite | Перезаписать |
| Replace | Заменить |
| Delete | Удалить |
| Trim | Обрезать |
| Trim Silence | Обрезать тишину |
| Mute | Приглушить |
| Blend At Marker | Плавный переход у маркера |
| Find | Найти |
| Insert Silence | Вставить тишину |
| Select View | Выделить видимое |
| Select All | Выделить всё |
| Set | Установить |
| Previous | Предыдущий |
| Next | Следующий |
| Move Start/Finish | Переместить начало/конец |
| Recall | Вызвать |
| Store | Сохранить |
| Snap To Zero-Crossing | Привязать к переходу через ноль |
| Add Cue | Добавить метку |
| Edit Cue Points | Изменить метки |
| Split File | Разделить файл |
| Auto Cue | Автоматические метки |
| Show Cue Lines | Показывать линии меток |
| Batch Processing | Пакетная обработка |
| Preset | Предустановка |
| Chain | Цепочка |
| Plug-in | Плагин |
| Visual | Визуализация |
| Configure | Настроить |
| Properties | Свойства |
| Settings | Настройки |
| Apply | Применить |
| Reset | Сбросить |
| Default | По умолчанию |
| Browse | Обзор |
| Proceed | Продолжить |
| Continue | Продолжить |
| Discard | Не сохранять |
| OK | ОК |
| Cancel | Отмена |
| Yes | Да |
| No | Нет |
| Close | Закрыть |
| Done | Готово |
| Retry | Повторить |
| Abort | Прервать |
| Ignore | Игнорировать |
| None | Нет |
| All | Все |
| Both | Оба |
| Other | Другой |
| Custom | Настраиваемый |
| Auto | Авто |
| Manual | Вручную |
| Normal | Обычный |
| Fixed | Фиксированный |
| Variable | Переменный |
| Linear | Линейный |
| Logarithmic | Логарифмический |
| Sine | Синусоида |
| Triangle | Треугольник |
| Square | Прямоугольник |
| Sawtooth | Пилообразный |

### Effects and audio processing

| English | Russian |
|---|---|
| Effect | Эффект |
| Auto Gain | Автоусиление |
| Auto Offset Removal | Автоудаление смещения |
| Censor | Цензура |
| Doppler | Эффект Доплера |
| Dynamics | Динамика |
| Echo | Эхо |
| Compressor | Компрессор |
| Expander | Экспандер |
| Compressor/Expander | Компрессор/экспандер |
| Flanger | Фленджер |
| Frequency Blend | Частотное смешивание |
| Interpolate | Интерполяция |
| Invert | Инверсия |
| Mechanize | Механизация |
| MaxMatch | MaxMatch |
| Multiband Compressor | Многополосный компрессор |
| Offset | Смещение |
| Pitch | Высота тона |
| Playback Rate | Скорость воспроизведения |
| Resample | Передискретизация |
| Reverb | Реверберация |
| Reverse | Реверс |
| Time | Время |
| Noise Gate | Шумовой затвор |
| Noise Reduction | Шумоподавление |
| Spectrum Filter | Спектральный фильтр |
| Low/Highpass | ФНЧ/ФВЧ |
| Bandpass/stop | Полосовой/режекторный фильтр |
| Equalizer | Эквалайзер |
| Parametric EQ | Параметрический эквалайзер |
| Pop/Click | Щелчки и хлопки |
| Silence Reduction | Подавление тишины |
| Smoother | Сглаживание |
| Change Volume | Изменение громкости |
| Fade In | Нарастание |
| Fade Out | Затухание |
| Voice Over | Наложение голоса |
| Maximize Volume | Максимизация громкости |
| Match Volume | Согласование громкости |
| Loudness | Громкость |
| Shape Volume | Формирование громкости |
| Channel Mixer | Микшер каналов |
| Multichannel Mixer | Многоканальный микшер |
| Reduce Vocals | Подавление вокала |
| Pan | Панорамирование |
| Stereo Center | Центрирование стерео |
| Gain | Усиление |
| Fade | Затухание |
| Fade curve | Кривая затухания |
| Crossfade | Кроссфейд |
| Threshold | Порог |
| Attack | Атака |
| Release | Восстановление |
| Ratio | Соотношение |
| Multiplier | Множитель |
| Reduction | Снижение |
| Clipping | Перегрузка |
| Peak | Пик |
| Amplitude | Амплитуда |
| DC offset | Постоянное смещение |
| Frequency | Частота |
| Band | Полоса |
| Cutoff | Частота среза |
| Steepness | Крутизна |
| Dynamic | Динамический |
| Static | Статический |
| Semitone | Полутон |
| Fine tune | Точная подстройка |
| Tempo | Темп |
| Delay | Задержка |
| Feedback | Обратная связь |
| Depth | Глубина |
| Modulator | Модулятор |
| Tremolo | Тремоло |
| Vibrato | Вибрато |
| Envelope | Огибающая |
| Shape | Форма |
| Point | Точка |
| Curve | Кривая |
| Spectrum | Спектр |
| Spectrogram | Спектрограмма |
| FFT | БПФ |
| FFT size | Размер БПФ |
| FFT window | Окно БПФ |
| Overlap | Перекрытие |
| Scale | Масштаб |
| Tone | Тон |
| Noise | Шум |
| Silence | Тишина |
| Silence level | Уровень тишины |
| Pop/click | Щелчки и хлопки |
| Tolerance | Допуск |
| Cue placement | Размещение меток |
| Confidence | Достоверность |
| Loudness Range (LRA) | Диапазон громкости (LRA) |
| LUFS | LUFS |
| BPM | BPM |
| VU meter | VU-метр |
| Tone meter | Индикатор тона |
| Analog meter | Аналоговый индикатор |
| Waterfall | Водопад |
| Bars | Столбцы |
| 3D Bars | 3D-столбцы |
| Envelope | Огибающая |
| Music Staff | Нотный стан |
| Ring | Кольцо |
| Stripe | Полосы |
| Bulge | Выпуклость |
| Blank | Пусто |
| Digital Time | Цифровое время |
| LED Time | Светодиодное время |
| Time and Status | Время и состояние |
| X-Y Graph | График X-Y |
| Media Player Visualizations | Визуализации проигрывателя |
| Channel Separation | Разделение каналов |

### Speech and transcription

| English | Russian |
|---|---|
| Speech Converter | Преобразователь речи |
| Text To Speech | Синтез речи |
| Speech To Text | Распознавание речи |
| Transcribe | Расшифровка |
| Transcription | Расшифровка |
| Recognizer | Распознаватель |
| Voice | Голос |
| Pitch | Высота тона |
| Speed | Скорость |
| Dictate | Диктовать |
| Speak | Произнести |
| Speak To File | Произнести в файл |
| Confidence | Достоверность |
| Timestamp | Отметка времени |
| Language | Язык |

## Style examples

| English | Good Russian | Bad (avoid) |
|---|---|---|
| `Balance` | `Баланс` | `Остаток средств` |
| `Quarter (0.25)` | `Четверть (0,25)` | `Квартал (0,25)` |
| `Double (2.0)` | `Двойная скорость (2,0)` | `Двухместный (2,0)` |
| `Close` | `Закрыть` | `Близко` |
| `Help` | `Справка` | `Помогите` |
| `Load` | `Загрузить` | `Нагрузка` |
| `Delete` | `Удалить` | `Удалять` |
| `Cue point` | `Метка` | `Ключевая точка`, `Cue` |
| `Selection` | `Выделение` | `Выбор` |
| `Volume` | `Громкость` | `Объем` |
| `Pitch` | `Высота тона` | `Подача` |
| `Release (s)` | `Восстановление (с)` | `Выпуск (с)` |
| `Plays the selection` | `Воспроизводит выделение` | `Играет выбор` |
| `Selects front left channel` | `Выбирает передний левый канал` | `Выбирает фронтальный левый канал` |
| `Moves the finish } marker` | `Перемещает маркер конца }` | `Перемещает финиш} маркер` |
| `Start { marker` | `Маркер начала {` | `Начало { маркер` |
| `Intro/loop/end` | `Вступление/повтор/конец` | `Введение / цикл / конец` |
| `Voice Over` | `Наложение голоса` | `Голос за кадром` |
| `Reverse` | `Реверс` | `Обратный` |
| `Reduce Vocals` | `Подавление вокала` | `Уменьшить вокал` |
| `Noise Gate` | `Шумовой затвор` | `Шумовые ворота` |
| `Time remaining: %0% (%1%%)` | `Осталось времени: %0% (%1%%)` | must keep placeholders |

## Final check before returning

- Every input id appears exactly once.
- No English words remain unless the string is technical or a proper name.
- `%` sequences, `|`, newlines, `{`, `}`, and `&` counts match the English string.
- Leading/trailing spaces match.
- Terminology follows the glossary.
- JSON is valid (escape quotes and backslashes correctly).
