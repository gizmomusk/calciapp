$action = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c C:\Users\$env:Dell\run_on_boot.bat"
$trigger = New-ScheduledTaskTrigger -AtStartup
$principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount -RunLevel Highest
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
Register-ScheduledTask -TaskName "RunBatchOnBoot" -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Description "Runs a Batch script on system boot"
