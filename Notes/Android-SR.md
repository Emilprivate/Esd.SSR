# My notes collection for Android Security Research

## 4. Aug 2024
- I'm following the [Android Bug Bounty Hunting](https://codered.eccouncil.org/course/android-bug-bounty-hunting-hunt-like-a-rat) program by Wesley Thijs on [eccouncil](https://codered.eccouncil.org) to get the fundamentals setup for Android Security Research.

### Tools
- Tools that have been installed for this session are the following ones: `android-studio`, `android-tools`, `genymotion`, `python-frida`, `python-frida-tools`, `python-objection`, `universal-android-ssl-pinning-bypass-with-frida`, `burpsuite`. 

### Genymotion
- With Genymotion I've downloaded the `Google Pixel XL` device emulator with Android 6.0 due to root restrictions on a personal use license of Genymotion. The reason we want root (only with 7.1 and over) is due to some certification injection we're gonna do later in the sessions, however, `Android 7.1` and over is only required due to some applications not supporting older Android versions, this should not be a problem as one is getting started.
- It's important to enable USB debugging in Developer options of the emulator. Developer options can be enabled by tabbing x7 on "Build number" under "About phone".

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
- Push the script onto the device `adb push <script> /data/local/tmp`

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
...
```
- If the list of processes show up then everything is setup properly.

### Script injection to bypass certification pinning.
- Hook frida script into the application - `frida -U -f <application> -l <path_to_fridascript.js> --no-paus`

### Attack strategies & Bug bounty fundamentals
Now that the fundamental setup is done there are certain attack vectors that are important to know about and how bug-bounties in general are conducted.

**Bug bounty fundamentals**
- Always build a POC (proof of concept) before reporting!
- Start with VDP (vulnerability disclosure programs) to get points, they usually don't pay. This is because you can get feedback and be invited to private programs or groups + experience. Wait till the paid programs follow and apply your knowledge.

**Attack strategy**
- Static code analysis:
  - 
- Dynamic hacking
  - Running the application and seeing what requests are being sent to the server.
  - API testing is a good choice.
  - Some applications run on web-view (JS) so XSS is valid! Test on all inputs!
  - Fully explore manually and make a mind map of the application.
  - Look into swagger documentation if available for the API.
  - Read if there are any manuals.
  - Have burp suite proxy run in the background and make requests.
    - Click "target" -> "Site map" you can have a filter by clicking the bar at the top and then select "Show only parameterized requests".
    - This way we can manipulate the parameter requests or just analyze.
    - This can be done by sending post requests with postid's and check the response.
    - We could change the order of requests and see what happens.
    - Look for vulnerability and behaviour that isn't expected interms of business logic.
    - If there's a parameter in the response and not in the request, then try to send a request with that parameter and see what happens.
  - Any parameters that seems to contain a URL. If the target resolves the URL that is being entered, it might be vulnerable to SSRF.
  - There is also **automated testing**, here one could test for IDOR (research it). The goal is to essentially test for broken access control. So make sure to test ALL the privilege levels. Included in automated testing is fuzzing, try to fuzz endpoints for command injection and identify some other endpoints to attack.
  - Make sure to register to the applications with the platform information of where the bug consists to ensure not getting blacklisted or getting the target app blacklisted for spam or something similar damaging.




  
