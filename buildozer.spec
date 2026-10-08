[app]

# (str) Title of your application
title = TwinkleHub Server Selector

# (str) Package name
package.name = serverselector

# (str) Package domain (needed for android packaging)
package.domain = org.twinklehub

# (list) Source files to include (let it be relative to the dir)
source.include_exts = py,json

# (list) Directory where the source files are stored
source.dir = .

# (str) Application versioning
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pyjnius

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,BIND_VPN_SERVICE,FOREGROUND_SERVICE

# (list) target architectures
android.archs = arm64-v8a

# (bool) Automatically accept SDK license
android.accept_sdk_license = True

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use (фиксируем стабильную версию 25b для сборки pyjnius)
android.ndk = 25b

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug command)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
