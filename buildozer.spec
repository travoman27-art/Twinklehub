[app]
title = TwinkleHub
package.name = twinklehub
package.domain = org.twinkle.mlbb
source.include_exts = py,png,jpg,kv,atlas
source.dir = .
version = 1.0
requirements = python3,kivy,jnius
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE,BIND_VPN_SERVICE,FOREGROUND_SERVICE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 31
android.accept_sdk_license = True
purl = 

[buildozer]
log_level = 2
warn_on_root = 1
