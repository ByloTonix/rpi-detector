<h1 align="center">Raspberry Pi Camera Detector</h1>
<h4 align="center">Raspberry Pi Camera Detector - это Python-скрипт, с помощью которого можно использовать Raspberry Pi и CSI-камеру для неё в качестве детектора движения.</h4>

## Предупреждения:
- Убедитесь, что вы используете **Raspberry Pi OS Legacy**. Возможна работа на Raspberry Pi OS Bullseye при использовании Legacy-версии драйвера Pycamera. С иными дистрибутивами могут наблюдаться проблемы,
- Убедитесь, что у вас установлен **Python 3.x**.

## Требования:
- Raspberry Pi 2B и новее,
- Raspberry Pi Camera I-ого поколения и новее (подойдут и китайские клоны, и иные CSI-камеры*).

## Настройка:

- В настройках Raspberry Pi Configuration Tool включите работу камеры.

- Установите необходимые зависимости:
```sh
sudo apt install python3-opencv -y
sudo apt install git --no-install-recommends -y
```

- Скачайте сам скрипт:
```sh
git clone https://github.com/MatroCholo/rpi-detector/
cd rpi-detector
sudo chmod +x detector.py
mkdir images
```

## Использование:
- После выполнения настройки перейдите в каталог со скриптом и запустите его**:
```sh
cd ~/rpi-detector
./detector.sh
```

*При наличии в дистрибутиве нужных драйверов.

## Обратная связь:
- Telegram: https://t.me/MatroCholo
