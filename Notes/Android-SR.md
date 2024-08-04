# My notes collection for Android Security Research

## 4. Aug 2024
- I'm following the [Android Bug Bounty Hunting](https://codered.eccouncil.org/course/android-bug-bounty-hunting-hunt-like-a-rat) program by Wesley Thijs on [eccouncil](https://codered.eccouncil.org) to get the fundamentals setup for Android Security Research.

### Tools
- Tools that have been installed for this session are the following ones: `android-studio`, `android-tools`, `genymotion`, `python-frida`, `python-frida-tools`, `python-objection`, `universal-android-ssl-pinning-bypass-with-frida`, `burpsuite`. 

### Genymotion
- With Genymotion I've downloaded the `Google Pixel XL` device emulator with Android 6.0 due to root restrictions on a personal use license of Genymotion. The reason we want root (only with 7.1 and over) is due to some certification injection we're gonna do later in the sessions, however, `Android 7.1` and over is only required due to some applications not supporting older Android versions, this should not be a problem as one is getting started.
- It's important to enable USB debugging in Developer options of the emulator. Developer options can be enabled by tabbing "Buid number" under "About phone".

### ADB & Frida
- Ensure that ADB is in your path environment (should be added automatically on linux atleast)
- Besides the tools mentioned above we also need frida-server. Before downloading the frida-server, we need to detect what version of the server we need which depends on the arch of the emulator, run `adb shell getprop ro-product.cpu.abi`, in my case it was `x86`, so I downloaded `frida-server-xxxx-android-x86.xz` and extracted it inside the `Tools` folder.
- Now we need to push frida to the device and give it permissions to execute.
 - `adb push ADB/frida-server /data/local/tmp`
 - `adb shell chmod 777 /data/local/tmp/frida-server`
 - "frida-server" being the name of the executable.

### Burpsuite
- Start burpsuite -> Proxy -> Proxy settings -> Import/export CA certificate -> Certificate in DER format -> Give name and save somewhere.
- Push the certificate onto the device with ADB, this is needed later for frida.
 - `adb push <name>.der /data/local/tmp/cert-der.crt` <-- We're renaming it to crt.

### universal-android-ssl-pinning-bypass-with-frida script
- Push the script onto the device `adb push <script> /data/local/tmp

### frida-server on the device
- Check and run frida server on the device `adb shell /data/local/tmp/frida-server &`
    `[1] 322142`

- List all the running processes on the device `frida-ps -U`
    ```
     PID  Name
----  -----------------------------------
1446  Calendar
1481  Clock
1581  Gallery
2185  Search
2129  Settings
 137  adbd
 910  android.process.acore
 287  batteryd
1040  com.android.inputmethod.latin
1647  com.android.launcher3
2031  com.android.musicfx
1081  com.android.phone
1476  com.android.providers.calendar
1568  com.android.provision
1279  com.android.smspush
 847  com.android.systemui
1970  com.android.webview:webview_service
1089  com.genymotion.genyd
1068  com.genymotion.systempatcher
 292  debuggerd
 290  diskiod
 294  drmserver
2600  frida-server
 135  gatekeeperd
 302  genybaseband
 332  healthd
   1  init
 296  installd
 297  keystore
 279  lmkd
 284  local_camera
 285  local_camera
 283  local_opengl
 654  logcat
2603  logcat
 116  logd
 286  logwrapper
 295  mediaserver
 291  netd
 288  network_profile
 136  perfprofd
 134  redis
 293  rild
 841  sdcard
 280  servicemanager
 289  settingsd
 650  sh
 298  su
 644  surfaceflinger
 618  system_server
  99  ueventd
 282  vinput
 126  vold
 793  wpa_supplicant
 299  zygote
    ```
- If the list of processes show up then everything is setup properly.

### Script injection to bypass certification pinning.

