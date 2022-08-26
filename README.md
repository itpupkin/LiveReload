# LiveReload

<div align="center">LiveReload для веб разработки написанный на Python с применением Selenium</div>

# Настройка конфига

```json
{
    "filepath": "index.html",
    "browserpath": "file:///C:/Users/D1moncheck/Desktop/index.html",
    "updatedelay": "0.15"
}
```
**filepath** отвечает за путь относительно корневой папки. Вы можете указать **полный путь**.

**Пример полного указания пути:**
```json
{
    "filepath": "C:\\Users\\D1moncheck\\Desktop\\index.html"
}
```

**browserpath** отвечает за путь к которому может отбращаться браузер.

В **updatedelay** нужно указать задержку в секундах с которой мы хотим обновлять хэш сумму файла.
