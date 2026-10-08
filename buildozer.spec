[app]
title = TwinkleHub Server Selector
package.name = serverselector
package.domain = org.twinklehub
source.include_exts = py,json
source.dir = .
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE,BIND_VPN_SERVICE,FOREGROUND_SERVICE
android.archs = arm64-v8a
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.sdk = 33

[buildozer]
log_level = 2
warn_on_root = 1
