# Zazy-hunter-v1 — FROM-SCRATCH BUILDER PROMPT



Build a **new** application named **Zazy-hunter** version **v1**.  
Write all code from scratch. Do not assume files, class names, or folders exist until you create them.

Do not start writing code until you print the exact zip tree you will emit.  
Do not declare done until the acceptance bar is filled pass/fail with proof.

---

[online sites] $urls$ 

https://viewdns.info/
https://crt.sh/
https://dnsdumpster.com/
https://urlscan.io/
https://www.shodan.io/
https://www.virustotal.com/gui/
https://otx.alienvault.com/
https://www.ssllabs.com/ssltest/
https://securityheaders.com/
https://builtwith.com/
https://dmarcian.com/dmarc-inspector/
https://ip-checker.info/
https://searchdns.netcraft.com/
https://www.whois.com/
https://whois.domaintools.com/
https://who.is/
https://sitecheck.sucuri.net/
https://hostedscan.com/
https://backlinks.live/
https://www.upguard.com/webscan
https://urlscan.io/
https://scan.cyberchief.ai/
https://cyscan.io/
https://barrion.io/tools/website-security-scan
https://www.merklemap.com/
https://subdomainfinder.c99.nl/
https://deepfind.me/tools/network-and-cyber/subdomain-finder
https://deepfind.me/tools/network-and-cyber/ssl-certificate-inspector
https://deepfind.me/tools/network-and-cyber/http-header-analyzer
https://deepfind.me/tools/network-and-cyber/tech-stack-detector
https://deepfind.me/tools/network-and-cyber/ct-log-search
https://deepfind.me/tools/network-and-cyber/dns-lookup

[API keys]
OTX Key - 014850c4e0178c849c42f0f516b462d0c63152d5465a0dfdcafd7fc94af674d2
virus total -  8fc1db9540b4aabab669cbfd6f3d54ae9255ea42df891842cf31e59b9389ea91
shoden - XcN8k92xjlKhkS2uq0NpfJZEUIQESalj

[kali tools]
sublist3r
dnsrecon
fierce
dnsenum
puredns
alterx
dnsgen
theharvester
nmap
httpx
httprobe
whatweb
wafw00f
lbd
cdncheck
webtech
cmseek
sslyze
sslscan
testssl
tlsx
katana
hakrawler
gospider
photon
httrack
ffuf
feroxbuster
dirsearch
wfuzz
arjun
paramspider
linkfinder
secretfinder
jsluice
getjs
xnlinkfinder
jsfscan
subjs
gitleaks
trufflehog
wpscan
joomscan
droopescan
nuclei
nikto
wapiti
dalfox
xsstrike
commix
wcvs
dotdotpwn
skipfish
davtest
cadaver
corsy
crlfuzz
rapidscan
reconftw
ping
curl


[Main sections] + add more which tools can generate 
Subdomains Found
Found IPs
Open Ports & Services
Technologies
WAF Detection
TLS Protocols & TLS Grades 
Cert-Info
Vulnerable TLS Cipher Suites
Security Headers
DNS Records
Emails & Sociel Media Links
CDN
Interesting files
All Endpoints
Secrets In Code
Vulnerabilities Found
CVEs


```
SYSTEM / BUILDER PROMPT — create Zazy-hunter v1 from scratch

You are creating Zazy-hunter v1: a local, single-operator, authorized
web-application security assessment platform.

It performs reconnaissance, crawling, misconfiguration detection,
vulnerability DETECTION & exploitation, evidence collection, and reporting.

It is a scanner, finder and exploitation tool.
It is a copy of Burp Suite or Acunetix and other security scanners tool.

Display name: Zazy-hunter
Version: v1
Sticky footer on every page (muted, small):
  Zazy-hunter  ·  made by Anand Jogawade (Zazy)

==============================================================================
1. Baisc Rules
==============================================================================

- Copy proprietary scanner engines or branded UI assets.
- Do not add screenshot browsers (gowitness, eyewitness) or a Screenshots page.
- Do not use shell=True. Tools run as argv lists of allowlisted binaries.
- Write runtime scan files only under projects/<project_id>/ inside ROOT_DIR.
- Creates Default scan profile which runs everything and also make 20 different scan profiles and also give user to crete or delete creted profile

==============================================================================
2. STACK AND BINDING
==============================================================================
Language: Python 3.11+
Web: Flask + Flask-SocketIO + Jinja2 + vanilla JS + CSS + HTML 
TLS: self-signed certs in certs/cert.pem and certs/key.pem (generated on first run)
Listen: HTTPS 0.0.0.0:8082
  Override with env ZAZY_HOST and ZAZY_PORT
CORS: allow https://127.0.0.1:8082 and https://localhost:8082
      (and the configured host). Do not use only "*".

Launchers:
  Zazy.py  — create venv, pip install -r requirements.txt, generate cert
             if missing, preflight `import app`, then exec app.py
  main.py  — run app.py with system Python (no venv required)
  app.py   — the server

Zazy.py banner MUST print:
  Zazy-hunter – Auto Launcher
  Authorized Recon & Scanning Only
  https://0.0.0.0:8082

config.py MUST define (names exact):
  ROOT_DIR = Path(__file__).resolve().parent
  BASE_DIR = ROOT_DIR
  PROJECTS_DIR, PLUGINS_DIR, CERTS_DIR, TOOLS_DIR, PROFILES_DIR
  DIRECTORIES_DIR, AGENTS_DIR, DATA_DIR
  HOST, PORT, CERT_FILE, KEY_FILE, SCAN_SPEEDS, CORS_ORIGINS
  EXCLUDED_SUB_CLIS
All mkdir calls use these Path objects. Never mkdir relative to cwd.

Python files: shebang, module docstring, then
  from __future__ import annotations
as the first statement. No import may appear above it.

requirements.txt:
  Flask>=3.0
  Flask-SocketIO>=5.3
  Werkzeug>=3.0
  Jinja2>=3.1
  python-dotenv
  psutil
  requests
  cryptography>=42
  (more if needed) 
==============================================================================
3. WHAT THE PRODUCT DOES
==============================================================================
Operator creates a Project, adds in-scope target URL(s)/hosts, confirms
authorization, picks a Profile and concurrency, presses Start Scan.

Pipeline:
  1. Scope gate 
  2. Passive subdomain discovery via listed websites + mentained tools
  3. Live / IP confirmation
  4. DNS records
  5. Nmap Port + service and version scan 
  6. Technology / WAF / TLS / security-header collection
  7. Crawl + insertion-point inventory
  8. Directory brute (exactly one tool; default dirsearch)
  9. Historical URLs / JS collection if those binaries exist
 10. Installed vulnerability scanners (nuclei, nikto, …) if present
 11. Built-in safe DAST catalog + issue registry
 12. Version-CVE match from public feeds
 13. Correlate / dedupe / confidence
 14. Persist JSON + raw logs
 15. Live UI + reports
 [Add more which missing any step or method]
If a tool is not installed, mark the section degraded. Do not crash.

==============================================================================
4. AUTHENTICATION
==============================================================================
First launch: /setup sets a local password (stored as a hash under data/).
Later: /login required before projects, tools, plugins, settings, scans.
Session cookie. No anonymous scanner.
Settings shows API keys as first 5 characters + asterisks.

==============================================================================
5. PROJECTS, PROFILES, SCANS
==============================================================================
Project fields: name, notes, targets (one or many),
profile name, speed preset slow | medium | fast | auto.

Profiles: a Default profile ships with default argv templates per tool.
Operator may clone and edit commands. Projects select a profile.

Each Start Scan creates projects/<id>/scans/scan_00N/ even if the same
target is scanned again. History is listed on the project page.

Speed presets MUST change thread/rate/delay flags actually passed to tools.

==============================================================================
6. TOOL EXECUTION
==============================================================================
ScanEngine only schedules.
Every tool run is:
  python3 agents/run_task.py --spec /abs/path/spec.json

spec.json contains argv list, timeout, cwd = scan sandbox, env PATH.
run_task.py writes:
  stdout.log  stderr.log  status.json  result.json  heartbeat.json
Stop Scan kills the process GROUP of all running tasks and cancels
in-flight plugin HTTP.
Operator can skip a queued tool, stop one running tool, or rerun one
tool with optional extra flags.

Concurrency: N slots. When one task exits, the next queued task starts
immediately. Auto mode uses ~80% of available cores/RAM via psutil.

Exclusive families (:
  directory brute: dirsearch 
  subdomain brute: puredns only on Default
  port scan: nmap 


Retry: if a tool fails with a known signature (e.g. nmap “host seems down”),
run the documented fallback argv as a NEW task. Never silently retry the
identical command. Show the chain in Executions.

Health per task: exit code AND expected output shape
  ✅ ran correctly   ⚠️ unexpected output   ❌ failed after fallback

==============================================================================
7. DEFAULT RECON (LOCKED)
==============================================================================
Subdomains — always:
  https://crt.sh/
  https://dnsdumpster.com/
  https://subdomainfinder.c99.nl/
  https://appsecsanta.com/
  https://subdomainfinder.in/
  ($urls$)
  plus puredns:
    puredns bruteforce directories/subdomains.txt APEX
      --resolvers resolvers.txt
Live / IP:
  ping -c 2 -W 2, whois, dnsx, httpx, nmap -sn, curl
  Status per host: live or offline
  Found IPs: only the target and its discovered in-scope hosts
Ports — nmap sequential:
  nmap -sT -sV -T3 --top-ports 1000 HOST
  if 0 hosts up / host down → repeat with -Pn
  then -p 1-10000
  then -p 10001-65535
  optional: same ranges on live subdomains if “deep ports on subs” is on
  Do not default to -p-
DNS (if installed): dnsrecon, dnsenum, fierce, knockpy, dnsx
Emails: theHarvester + enabled OSINT plugins
Technologies: versions of server, language, libraries, third-party JS
  (whatweb / httpx / webtech / cmseek if present)
WAF: “no WAF” or “yes” + product name
TLS / cert:
  overall rating if a plugin provides it
  common names, SANs, valid from/until
  protocols TLS1.3/1.2/1.1/1.0/SSL3/SSL2 as Yes/No
  list ONLY weak/vulnerable ciphers, grouped by protocol
Security headers on the exact scheme the operator entered:
  present vs missing for HSTS, X-Frame-Options, X-Content-Type-Options,
  Referrer-Policy, Permissions-Policy, CSP (and similar)
Admin panels: URL + title if found
Directories:
  only http:// or https:// URLs
  filter by status code; default filter 200
  Copy copies the filtered set only
  One brute tool; default dirsearch
  Wordlist order: CMS list first if CMS detected, else
  Best-Combined-Wordlist.txt, then Wordlist-part1 … part5

CMS-specific scanners (wpscan, joomscan, droopescan) run ONLY after
fingerprint says that CMS is present.

==============================================================================
8. CRAWL + DAST (BUILT-IN)
==============================================================================
Create these modules with real logic (not empty stubs):

agents/http_util.py      timeout HTTP client, curl_repro()
agents/crawler.py        scope-respecting BFS, depth/page caps,
                         extract links, forms, query params, scripts
agents/browser_crawl.py  if chromium or google-chrome is on PATH,
                         headless --dump-dom same-origin links (budget ~40)
                         and test a canary in rendered HTML / hash;
                         else log skip
agents/dast_passive.py   missing headers, cookie flags, directory listing,
                         mixed content, exposed paths
                         (/.git/HEAD .env swagger actuator graphql
                          security.txt robots.txt crossdomain.xml …)
agents/dast_active.py    one canary each:
                         reflected XSS, SQLi boolean length-diff (no dump),
                         SSTI {{7*7}}, format-string, open redirect,
                         CORS foreign Origin, NoSQL $ne on JSON POST,
                         LFI signature only (no file contents in UI)
agents/dast_catalog.py   orchestrate + request budget
                         (~120 pages, ~80 params, ~200 extra requests)
agents/checks_extra.py   CNAME takeover FINGERPRINT (do not register),
                         AXFR one-shot against discovered NS,
                         origin-IP CANDIDATES report-only (do not scan
                         unless operator adds them to scope),
                         vhost Host-header mismatch,
                         WebDAV OPTIONS; if PUT allowed, write a
                         harmless probe file then DELETE it,
                         JWT/OAuth static hints in HTML/JS,
                         in-page S3 bucket list-check only
agents/issue_registry.py named web issues (CSP, HSTS, cookies, PUT, TRACE,
                         GraphQL, OpenAPI, JWKS, backup files, listing,
                         emails, private IPs, PEM keys, mixed content,
                         CRLF header inject, file-upload form present,
                         DOM sink CANDIDATES from JS text — not confirmed
                         without browser render)
agents/confirm.py        second technique required before status=verified
agents/poc_builder.py    attach safe_poc {repro_curl, steps,
                         exploit_delivered:false}
agents/plugin_http.py    crt.sh JSON, Mozilla Observatory, hstspreload;
                         timeout; degrade; never hang the scan
agents/run_task.py       generic argv runner described above

Every finding object includes:
  title, url, param?, severity, status (detected|suspected|verified),
  cwe, owasp, wstg?, evidence (short), repro_curl, found_by,
  safe_poc, safe_repro=true

==============================================================================
9. PUBLIC VULN KNOWLEDGE (NOT A PIRATED COMMERCIAL PACK)
==============================================================================
utils/vuln_db.py
  On process start: refresh cache under data/vulndb/
  While the process lives: refresh again every 30 days
  Feeds:
    CISA KEV JSON
    CIRCL cve-search (last + product search)
    shipped JSON: owasp_2021.json, cwe_web.json, wstg_catalog.json,
                  web_misconfig_catalog.json

utils/oss_intel.py
  Download Retire.js jsrepository.json on refresh
  Query OSV.dev for fingerprinted JS libraries
  Use Nuclei + operator-installed nuclei-templates as the HTTP CVE pack
  (do not vendor the entire nuclei-templates git repo in the zip)

utils/catalog_match.py
  Stamp wstg / cwe / owasp onto findings by title/CWE

Fingerprinted product+version → CVE rows in results/cves.json
and a copy in vulnerabilities.json with owasp A06.

==============================================================================
10. ONLINE PLUGINS
==============================================================================
A plugin manager with classes:
  Free/No-Auth | Sign-in required | Paid API


Free/No-Auth examples (guarded HTTP, parse structured fields, degrade):
  SSL Labs, Mozilla Observatory, securityheaders.com, Sucuri SiteCheck,
  urlscan.io, Internet.nl, DNSViz, intoDNS, hstspreload.org, crt.sh

Settings stores keys. UI shows first 3 + asterisks.
Plugins page: each plugin button shows on / off / not configured;
click opens formatted output for that plugin.

Ship online_config.json with empty key values.

==============================================================================
11. RESULT SECTIONS (UI)
==============================================================================
Each section: 10-row preview + Show more.
Empty state text when no rows. Loading state while scan running.
Open button → full-page view of that section + Back to project.

Required sections:
Subdomains Found
Found IPs
Open Ports & Services
Technologies
WAF Detection
TLS Protocols & TLS Grades 
Cert-Info
Vulnerable TLS Cipher Suites
Security Headers
DNS Records
Emails & Sociel Media Links
CDN
Interesting files
All Endpoints
Secrets In Code
Vulnerabilities Found
CVEs
  Executions / Logs
  Coverage (pages, points, checks, findings, budget used)

No Screenshots section. No API Testing section.

Dedup rule: same host/url/cve → one row, append found_by, raise confidence
when two independent sources agree.

==============================================================================
12. CONSOLES
==============================================================================
Three buttons:
  1. Console        — black panel; only "TOOL is running \"argv\""
                      do not repeat the same tool name unless rerun
  2. Combined       — each finished (or live) tool command + output
                      one after another; scrollable
  3. Separate       — one panel per tool, A–Z default, optional category sort
                      if a tool ran twice, show each run in order

Page refresh must reload persisted logs, not reset to
“Ready. Press Start Scan.”

While running, show: total tools, running, completed, queued, failed.

==============================================================================
13. UI DESIGN
==============================================================================
Commercial SaaS dashboard (calm, whitespace,).
NOT a default green-on-black “hacker” skin.
Themes: Light, Dark, Ops — CSS variables in static/css/tokens.css
Severity colors defined once as variables (critical/high/medium/low/info).
UI font: system / Inter. Monospace only in consoles, commands, repro_curl.
Theme switcher in the sidebar; persist in a cookie.
20-second live refresh of results; skip DOM rewrite if JSON hash unchanged.

==============================================================================
14. PERSISTENCE
==============================================================================
projects/<id>/scans/scan_00N/
  raw/<tool>/stdout.log stderr.log
  results/<section>.json     incremental, atomic write
  tool_output/<tool>.log
  executions.jsonl
  spec.json files for each task

Write RAW output the moment the process exits, THEN parse, THEN
save_result. If a tool “succeeded” but raw is empty → status
ran_no_output. Never drop that fact.

Integrity check at scan finalize.

==============================================================================
15. REPORTS
==============================================================================
Generate HTML, PDF, Markdown, TXT, XLSX, JSON into
projects/<id>/reports/
Each finding in HTML/PDF shows title, severity, CWE, OWASP, WSTG,
found_by, evidence snippet, repro_curl, safe_poc.steps.

==============================================================================
16. WORDLISTS AND RESOLVERS
==============================================================================
Ship under directories/:
  subdomains.txt
  Best-Combined-Wordlist.txt
  cms/ and webmail lists if you include them
Ship resolvers.txt at app root (public resolvers).
If the builder environment has no wordlists, create small placeholders
AND document that the operator should drop full lists into directories/.

==============================================================================
17. DELIVERABLE ZIP
==============================================================================
Name: Zazy-hunter-v1.zip
Must unzip as a SINGLE top-level folder:

Zazy-hunter-v1/
  README.md
  TOOL_WORKFLOW.md
  CHECKLIST.md
  Dockerfile
  Zazy.py
  main.py
  app.py
  config.py
  generate_cert.py
  requirements.txt
  online_config.json
  resolvers.txt
  agents/          (all modules in §8)
  certs/           (optional; generated on first run)
  data/vulndb/     (shipped JSON catalogs)
  directories/     (wordlists)
  plugins/SCHEMA.md
  static/css/tokens.css
  static/css/style.css
  static/js/app.js
  templates/       login, setup, base, dashboard, projects,
                   create_project, configure_project, project_detail,
                   section, findings, executions, plugins, tools,
                   profiles, settings, reports
                   NO api_testing.html
  tests/smoke_test.py
  tests/fixtures/nmap.xml
  tests/fixtures/httpx.json
  tools/.gitkeep
  utils/
    auth.py profiles.py project_manager.py scan_engine.py task_agent.py
    tool_discovery.py tool_rules.py parsers.py verify.py
    online_plugins.py reports.py resources.py correlate.py
    vuln_db.py oss_intel.py catalog_match.py

Forbidden: Zazy-hunter-v1/Zazy-hunter-v1/...
README must say: extract into an EMPTY folder. Do not unzip into a
directory that already contains Zazy-hunter-v1/.

==============================================================================
18. README MUST INCLUDE
==============================================================================
- Authorized use only
- How to run: python3 Zazy.py
- URL https://0.0.0.0:8082 and https://127.0.0.1:8082
- First-run /setup password
- nuclei -update-templates recommended on Kali
- Wordlist locations
- What this tool will not do (no exploit delivery)

==============================================================================
19. ACCEPTANCE BAR (print pass/fail + why)
==============================================================================
1. Unzip → one top-level folder; app.py sits in that folder.
2. python3 -m py_compile succeeds on every product .py
3. python3 -c "import app" succeeds (after deps)
4. Zazy.py banner says v1; preflight import runs before exec
5. from config import BASE_DIR, ROOT_DIR, HOST works; HOST is 0.0.0.0
6. grep -R shell=True --include='*.py' → zero in product code
7. grep -R api_test --include='*.py' --include='*.html' --include='*.js'
   → zero
8. tests/smoke_test.py creates a fake project and writes non-empty
   results/ports.json (or equivalent) using the persist helper
9. No from __future__ after another import in any .py
10. Footer string present in base template
11. Login/setup templates exist
12. Three console modes exist in the project UI
13. Default tool picker does not pre-check excluded subdomain CLIs

==============================================================================
20. DEFINITION OF DONE
==============================================================================
You unzipped YOUR zip into a fresh /tmp folder, listed the tree,
compiled, imported app, ran smoke_test, grepped the bans, and pasted
the acceptance table. “It should work” is not done.
```

---

## How to use

1. Copy everything inside the fenced `SYSTEM / BUILDER PROMPT` block.  
2. Use it as the system prompt for a **new** session with **no** old zips attached.  
3. First user message: `build`  
4. Reject any output that mentions older Zazy/VAPT/AutoRecon versions, “migrate from v19,” or double-nested folders.

Saved as: `artifacts/Zazy-Hunter-v1-From-Scratch-Builder-Prompt.md`

if acunetix private check list and version-CVE pack are closed then use all possible open scource for same and add that
search on internet of vulnerabilities of web and cve and cwe of web application and add that check in database  so it will be like acunetix
can this have all database of cve and cwe and all vulnerabilities of web and all possible misconfigurations of web if not added add that this tool have its own database of all to verify vulnerabilities and match it with result also it shoud check all version and vulnerabilities from online sites which have vulnerabilities of versions also the database shud update each time tool start and if tool alrweady running cuntinuously from 1 month thewn ti shoud auto update ones a month 

also exploit all vulnerabilities is i mean by which vulnerability tool generates it a wxploit or exploit poc not actually exploit so build logic
also dome exploit or vulnerabilities need browser so add code to run chromium or avaiable brosweer to do that also site crawler can use that broswer to crawl full site and click every button on site so site mab will be updated
Full JS/DOM/SPA coverage like Acunetix + auto site crawler so this tool can do pentest in website it shoud use kali tools and online tools + auto update its database   and can match scan results realtime with database of owasp top 10 vulnerabilities and + cwe+ cve+ all web vulnerabilites 
use all sites which have this database + it should find all this web vulnerabilities in this image if not added  then make each vulnerability different  and all possible logics to find and exploit it 
also this tool allow to exploit all vulnerabilities becuease its my personal clients whch always give me uat environment to test so if any exploit poc missing then client will be in risk so make safe exploit poc for all possible vulnerabilities
add everyvulnerability checks into this all owasp top 10 + all web vulnerabilities and go on internet and find all vulnerable softwares and verison and payloads and add its logic and build datyabase of that which can auto update when every tool run in background use all free sites which has vulnerabilities database and version vulnerabilities database and cwe database and cve database and my all plugins should run and give all possible result which that plugin can generate and sort it in that section and give me rebuilded v1