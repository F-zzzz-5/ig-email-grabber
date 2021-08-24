# IG Email Grabber

Just incase the title is slightly misleading, please read the following points which will further explain how this works and its limitations.

## About
* Utilizes Instagram "Account Recovery" API.
* Fetches email from HTTP response content.
* Email is partly censored due to Instagram servers not sending back the entire email.
* Email length is retained.

## How is this useful?
* Assists with OSINT operations.
* Completely anonymous if VPN/Proxy used. (proxy setting coming soon)

## Example Formatting
Instagram passes back a modified version of the email, with the first letter showing with the email provider.
```
s******4@outlook.com
g********g@yahoo.com
v****3@gmail.com
```

## Requirements
* requests
* colorama
* termcolor
