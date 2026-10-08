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

# (str) Application versioning (изменено для сброса старого кэша сборки)
version = 1.1

# (list) Application requirements
requirements = python3,kivy

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

[buildozer]
log_level = 2
warn_on_root = 1

# Отключаем строгую изоляцию pip внутри сборщика p4a
p4a.branch = master
