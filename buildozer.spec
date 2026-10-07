[app]
title = TwinkleHub Server Selector
package.name = serverselector
package.domain = org.twinklehub
source.include_exts = py,json
source.dir = .
version = 1.0
requirements = python3,kivy,jnius
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE,BIND_VPN_SERVICE,FOREGROUND_SERVICE
android.archs = arm64-v8a
android.allow_backup = True
android.api = 31
android.minapi = 21
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
