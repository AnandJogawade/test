```powershell
# Requires Administrator privileges

Write-Host "[*] Checking RDP status..." -ForegroundColor Cyan

# Enable RDP if disabled
$rdpEnabled = (Get-ItemProperty `
    -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server" `
    -Name "fDenyTSConnections").fDenyTSConnections

if ($rdpEnabled -eq 1) {
    Write-Host "[+] Enabling RDP..." -ForegroundColor Yellow

    Set-ItemProperty `
        -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server" `
        -Name "fDenyTSConnections" `
        -Value 0

    Enable-NetFirewallRule -DisplayGroup "Remote Desktop" | Out-Null
}
else {
    Write-Host "[+] RDP already enabled." -ForegroundColor Green
}

Write-Host "[*] Checking Shadow RDP policy..." -ForegroundColor Cyan

$tsKey = "HKLM:\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services"

if (!(Test-Path $tsKey)) {
    New-Item -Path $tsKey -Force | Out-Null
}

try {
    $shadow = (Get-ItemProperty -Path $tsKey -Name Shadow -ErrorAction Stop).Shadow
}
catch {
    $shadow = $null
}

if ($shadow -ne 2) {
    Write-Host "[+] Enabling Shadow RDP (Full Control, No Consent)..." -ForegroundColor Yellow

    New-ItemProperty `
        -Path $tsKey `
        -Name Shadow `
        -PropertyType DWord `
        -Value 2 `
        -Force | Out-Null
}
else {
    Write-Host "[+] Shadow RDP already enabled." -ForegroundColor Green
}

Write-Host "[*] Enabling supporting firewall rules..." -ForegroundColor Cyan

Enable-NetFirewallRule -DisplayGroup "Remote Desktop" -ErrorAction SilentlyContinue | Out-Null
Enable-NetFirewallRule -DisplayGroup "File and Printer Sharing" -ErrorAction SilentlyContinue | Out-Null

gpupdate /target:computer /force | Out-Null

Write-Host ""
Write-Host "========== STATUS ==========" -ForegroundColor Cyan

$rdpStatus = (Get-ItemProperty `
    -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server" `
    -Name "fDenyTSConnections").fDenyTSConnections

$shadowStatus = (Get-ItemProperty `
    -Path $tsKey `
    -Name Shadow -ErrorAction SilentlyContinue).Shadow

Write-Host "RDP Enabled      : $([bool]($rdpStatus -eq 0))"
Write-Host "Shadow RDP Value : $shadowStatus"

switch ($shadowStatus) {
    0 { Write-Host "Shadowing Disabled" }
    1 { Write-Host "Full Control + Consent Required" }
    2 { Write-Host "Full Control + No Consent Required" }
    3 { Write-Host "View Only + Consent Required" }
    4 { Write-Host "View Only + No Consent Required" }
}

Write-Host ""
Write-Host "[+] Configuration complete." -ForegroundColor Green
```
