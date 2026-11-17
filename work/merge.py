import json, sys, re

EN = 'en.lang'
OUT = 'ru.lang.new'

with open(EN, encoding='utf-8-sig') as f:
    en = json.load(f)

batch = {}
for bi in range(1, 43):
    with open(f'work/batches/batch_{bi:03d}.json', encoding='utf-8') as f:
        for o in json.load(f):
            batch[str(o['id'])] = o

tr = {}
for bi in range(1, 43):
    with open(f'work/translations/batch_{bi:03d}.json', encoding='utf-8') as f:
        for i, r in json.load(f).items():
            tr[batch[i]['text']] = r

# Manual overrides for strings whose translation depends on context or was awkward.
tr['Rate'] = 'Частота'
tr['Rate: '] = 'Частота: '
tr['Full sweep'] = 'Полная развёртка'
tr['Add Edit'] = 'Добавление правки'
tr['Plays backward'] = 'Воспроизводит в обратном направлении'
tr['Continue to finish }'] = 'Продолжить до маркера конца }'
tr['Up to finish }'] = 'До маркера конца }'
tr['Monitor input on visuals'] = 'Показывать входной сигнал на визуализациях'
tr['Encoder Not Found'] = 'Кодировщик не найден'
tr['Skip bytes'] = 'Пропуск байтов'
tr['Skip bytes:'] = 'Пропуск байтов:'

# Path-specific overrides where the same English string needs a different meaning.
path_overrides = {
    '/Forms/SpectrumFilterForm/Mode/Items.Strings/0': 'Статический',
    '/Forms/TestPlaybackForm/Sound/Items.Strings/2': 'Шум',
    '/Forms/ChannelSelectorForm/Caption': 'Выбор каналов',
    '/Forms/MultiRecorderForm/Stop/Hint': 'Останавливает запись',
    '/Forms/EncoderDownloadForm/Message/Lines.Strings/0': 'Не удаётся найти свежую 64-битную версию кодировщика MPEG Layer-3 (LAME).',
    '/Forms/EncoderDownloadForm/OpenDialog/Title': 'Расположение кодировщика',
    '/Forms/MixForm/Caption': 'Смешивание',
    '/Forms/CompareForm/ButtonOk/Caption': 'Сравнить',
    '/Forms/AppOptionsForm/Caption': 'Параметры приложения',
    '/Forms/FadeForm/FadeCurve/Caption': ' Кривая нарастания ',
    '/Forms/BlendFrame/TypeLabel/Caption': 'Кривая перехода:',
    '/Forms/CrossfadeFrame/FadeCurveBox/Caption': ' Кривые перехода ',
    '/Forms/CrossfadeFrame/LengthFader/Caption': 'Длительность',
    '/Forms/PreviewFrame/PreviewActionList/StopAction/Hint': 'Останавливает прослушивание',
    '/Forms/EvaluatorForm/SourceBox/Caption': ' Источник (wave#) ',
    '/Forms/Multiband/Band/Knee/Caption': 'Излом (дБ):',
    '/Internal/sUndoBlend': 'плавный переход у маркера',
    '/Internal/sUndoBlendStart': 'плавный переход у начала',
    '/Internal/sUndoBlendFinish': 'плавный переход у конца',
    '/Internal/sUndoCrossfade': 'кроссфейд',
    '/Internal/sUndoCueAdd': 'добавление метки',
    '/Internal/sUndoCueChange': 'изменения меток',
    '/Internal/sUndoCueDelete': 'удаление метки',
    '/Internal/sUndoCueMove': 'перемещение метки',
    '/Internal/sUndoCueTool': 'все изменения в инструменте меток',
    '/Internal/sUndoCut': 'вырезание',
    '/Internal/sUndoDelete': 'удаление',
    '/Internal/sUndoDirectEdit': 'правку мышью',
    '/Internal/sUndoMix': 'смешивание',
    '/Internal/sUndoMute': 'приглушение',
    '/Internal/sUndoOverwrite': 'перезапись',
    '/Internal/sUndoPaste': 'вставку',
    '/Internal/sUndoRecord': 'запись',
    '/Internal/sUndoReplace': 'замену',
    '/Internal/sUndoSilence': 'вставку тишины',
    '/Internal/sUndoTrim': 'обрезку',
    '/Internal/sUndoTrimSilence': 'обрезку тишины',
}

# Language metadata.
en['Language']['ISO Code'] = 'ru'
en['Language']['Display Name'] = 'Русский'
en['Language']['Date'] = '2026-11-17'
en['Language']['Copyright'] = 'Перевод на русский язык © 2026 GoldWave Inc.  Все права защищены.'
en['Language']['Revision'] = 'Перевод на русский язык'

lang_keys = {'ISO Code', 'Display Name', 'Date', 'Copyright', 'Revision'}

def translate(obj, path=''):
    if isinstance(obj, dict):
        return {k: translate(v, path + '/' + k) for k, v in obj.items()}
    if isinstance(obj, list):
        return [translate(v, path + '/' + str(i)) for i, v in enumerate(obj)]
    if path.startswith('/Language/') and path.rsplit('/', 1)[-1] in lang_keys:
        return obj
    if path in path_overrides:
        return path_overrides[path]
    return tr.get(obj, obj)

ru = translate(en)

with open(OUT, 'w', encoding='utf-8-sig', newline='\r\n') as f:
    json.dump(ru, f, ensure_ascii=False, indent=4)

print('written', OUT)
