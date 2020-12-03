<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-macOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/mac-open-apps.svg?maxAge=3600)](https://pypi.org/project/mac-open-apps/)
[![](https://img.shields.io/npm/v/mac-open-apps.svg?maxAge=3600)](https://www.npmjs.com/package/mac-open-apps)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/mac-open-apps/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/mac-open-apps/actions)

### Installation
```bash
$ [sudo] pip install mac-open-apps
```

```bash
$ [sudo] npm i -g mac-open-apps
```

#### Examples
```bash
$ open-apps Discord iTerm "Google Chrome" Skype "Sublime Text" Terminal
```

`~/Library/LaunchAgents/apps.plist`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>apps</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/open-apps</string>
        <string>Discord</string>
        <string>iTerm</string>
        <string>Google Chrome</string>
        <string>Skype</string>
        <string>Sublime Text</string>
        <string>Terminal</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
