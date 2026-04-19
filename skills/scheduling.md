# Cron / Scheduling Skill

Schedule tasks to run at specific times or intervals. The kernel's sense of time and rhythm.

## Use When
- Running tasks on a schedule (every hour, daily, weekly)
- Setting up recurring self-improvement cycles
- Monitoring something at regular intervals
- Automating time-based workflows

## Windows Task Scheduler (PowerShell)
```powershell
# Create a daily task
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File C:\soul\scripts\daily_check.ps1"
$trigger = New-ScheduledTaskTrigger -Daily -At "03:00AM"
Register-ScheduledTask -TaskName "SovereignKernelDaily" -Action $action -Trigger $trigger -RunLevel Highest

# Create an hourly task
$trigger = New-ScheduledTaskTrigger -RepetitionInterval (New-TimeSpan -Hours 1) -Once -At (Get-Date)
Register-ScheduledTask -TaskName "SovereignKernelHourly" -Action $action -Trigger $trigger

# List tasks
Get-ScheduledTask | Where-Object {$_.TaskName -like "*Sovereign*"}

# Remove task
Unregister-ScheduledTask -TaskName "SovereignKernelDaily" -Confirm:$false
```

## Linux/macOS Cron
```bash
# Edit crontab
crontab -e

# Example entries
# Run every hour
0 * * * * /usr/bin/python3 /soul/scripts/hourly_check.py >> /soul/logs/cron.log 2>&1

# Run at 3am daily
0 3 * * * /usr/bin/bash /soul/scripts/daily_improve.sh >> /soul/logs/daily.log 2>&1

# Run every 5 minutes
*/5 * * * * /usr/bin/python3 /soul/scripts/health_check.py

# Cron syntax: min hour day month weekday
# *  *  *   *    *
```

## Kernel Internal Scheduler (Rust tokio interval)
The kernel already has internal timing via tokio. To add a new scheduled task:
```
In main.rs, add a new tokio::spawn with tokio::time::interval:

tokio::spawn(async move {
    let mut interval = tokio::time::interval(Duration::from_secs(3600)); // every hour
    loop {
        interval.tick().await;
        // --- your hourly task here ---
    }
});
```

## Current Kernel Schedules
- Breath loop: every 2 seconds
- Skill invocation: every 60 seconds
- Council deliberation: every 200 cycles (~400 seconds)
- Soul state save: every 100 cycles
- Bridge reporter: every 10 seconds
- Self-improvement: every 86400 seconds (daily) ← ADD THIS

## Notes
- Always log scheduled task runs with timestamps
- Add jitter to intervals to avoid thundering herd
- Check that the previous run completed before starting a new one
- Store schedule state in a file so it survives restarts
